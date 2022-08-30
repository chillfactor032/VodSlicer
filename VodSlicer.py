from genericpath import isfile
import sys
import json
import os
import requests
import re
import urllib
import subprocess
import time
import hashlib
import platform
import stat

# PySide6 Imports
from PySide6.QtWidgets import QApplication, QMainWindow, QStyle, QMessageBox, QLineEdit, QFileDialog, QDialog, QStyleFactory, QMenu
from PySide6.QtCore import QFile, Signal, QObject, QStandardPaths, QSettings, Qt, QTextStream, QThreadPool, QRunnable, QUrl
from PySide6.QtGui import QStandardItemModel, QStandardItem, QPixmap, QIcon, QColor, QPalette, QAction, QCursor, QDesktopServices

# VodSlicer Imports
#from qt_material import apply_stylesheet
import Resources
import UI_Components as UI

class VodSlicerApp(QMainWindow, UI.Ui_MainWindow):
    def __init__(self):
        super(VodSlicerApp, self).__init__()
        
        #Read Version File From Resources
        self.app_name = "VoD Slicer"
        version_file = QFile(":version.json")
        version_file.open(QFile.ReadOnly)
        text_stream = QTextStream(version_file)
        version_file_text = text_stream.readAll()
        self.version_dict = json.loads(version_file_text)
        self.version = self.version_dict["version"]
        self.os = "win"
        ## Get Directories to Store Files
        self.temp_dir = os.path.join(QStandardPaths.writableLocation(QStandardPaths.TempLocation), "VodSlicer").replace("\\", "/")
        self.config_dir = QStandardPaths.writableLocation(QStandardPaths.ConfigLocation)
        self.documents_dir = QStandardPaths.writableLocation(QStandardPaths.DocumentsLocation)
        print(self.config_dir)
        # Create config directory if it doesnt exist
        if(not os.path.isdir(self.config_dir)):
            os.makedirs(self.config_dir, exist_ok=True)
        self.ini_path = os.path.join(self.config_dir, "VodSlicer.ini").replace("\\", "/")

        ## Copy FFMPEG to Local Config Dir
        ffmpeg_filename = "ffmpeg-win64.exe"
        if "macOS" in platform.platform(terse=1):
            #Mac Detected
            ffmpeg_filename = "ffmpeg"
            self.os = "mac"
        self.ffmpeg_path = os.path.join(self.config_dir, ffmpeg_filename).replace("\\", "/")
        self.ffmpeg_md5 = ""
        if(os.path.exists(self.ffmpeg_path)==False):
            ffmpeg_file = QFile(f":resources/files/{ffmpeg_filename}")
            ffmpeg_file.open(QFile.ReadOnly)
            data = ffmpeg_file.readAll()
            ffmpeg_bytes = data.data()
            with open(self.ffmpeg_path, "wb") as f:
                f.write(ffmpeg_bytes)
                self.ffmpeg_md5 = hashlib.md5(ffmpeg_bytes).hexdigest()
            if(os.path.exists(self.ffmpeg_path)==False):
                print("Failed to create FFMPEG Binary")
        else:
            with open(self.ffmpeg_path, 'rb') as f:
                ffmpeg_bytes = f.read()    
                self.ffmpeg_md5 = hashlib.md5(ffmpeg_bytes).hexdigest()

        #If OS not Windows, set ffmpeg binary as executable
        if self.os != "win":
            os.chmod(self.ffmpeg_path, os.stat.S_IXUSR)

        # Get Settings From Ini File
        self.settings = QSettings(self.ini_path, QSettings.IniFormat)
        self.vod_url = self.settings.value("VodSlicer/vod_url", "")
        self.vod_user = self.settings.value("VodSlicer/vod_user", "")
        self.vod_password = self.settings.value("VodSlicer/vod_password", "")
        self.previous_save_dir = self.settings.value("VodSlicer/previous_save_dir", self.documents_dir)

        #Load UI Components
        self.setupUi(self)
        self.setWindowTitle(f"{self.app_name} {self.version} by ChillFacToR")
        self.vod_list_model = QStandardItemModel()
        self.vod_list_view.setModel(self.vod_list_model)
        self.vod_list_view.setSpacing(3)
        self.vod_url_edit.setText(self.vod_url)
        self.vod_url_edit.setCursorPosition(0)
        self.user_edit.setText(self.vod_user)
        self.password_edit.setText(self.vod_password)
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.progress_dialog = ProgressDialog()
        reload_icon_pixmap = QStyle.StandardPixmap.SP_BrowserReload
        reload_icon = self.style().standardIcon(reload_icon_pixmap)
        self.save_button.setIcon(reload_icon)
        file_icon_pixmap = QStyle.StandardPixmap.SP_DirOpenIcon
        file_icon = self.style().standardIcon(file_icon_pixmap)
        self.open_file_button.setIcon(file_icon)

        #Set window Icon
        default_icon_pixmap = QStyle.StandardPixmap.SP_FileDialogListView
        lps_icon_pixmap = QPixmap(":resources/img/vod_slicer.ico")
        self.vodslicer_icon = QIcon(lps_icon_pixmap)
        default_icon = self.style().standardIcon(default_icon_pixmap)
        if(self.vodslicer_icon):
            self.setWindowIcon(self.vodslicer_icon)
        else:
            self.setWindowIcon(default_icon)
            self.vodslicer_icon = default_icon

        # Button Signals
        self.save_button.clicked.connect(self.click_save_button)
        self.slice_button.clicked.connect(self.click_slice_button)
        self.about_button.clicked.connect(self.show_about)
        self.github_button.clicked.connect(self.show_github)
        self.open_file_button.clicked.connect(self.click_open_button)


        # Add Context Menu
        self.context_menu = QMenu()
        self.action_about = QAction("About")
        self.context_menu.addAction(self.action_about)
        self.action_about.triggered.connect(self.show_about) 
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)

        ## ThreadPool
        self.threadpool = QThreadPool()

        # Initialize the vod list
        self.refresh(True)

        geometry = self.settings.value("VodSlicer/geometry")
        window_state = self.settings.value("VodSlicer/windowState")
        if(geometry and window_state):
            self.restoreGeometry(geometry) 
            self.restoreState(window_state)

    def click_open_button(self):
        dir = QFileDialog.getExistingDirectory(self, "Open MP4 Directory", self.documents_dir, QFileDialog.ShowDirsOnly | QFileDialog.DontResolveSymlinks)
        dir = dir.strip()
        if(os.path.isdir(dir)):
            self.vod_url_edit.setText(dir)
            self.refresh()

    def show_github(self):
        QDesktopServices.openUrl(QUrl("https://github.com/chillfactor032/VodSlicer"))

    def show_context_menu(self):
        self.context_menu.popup(QCursor.pos())

    def show_about(self):
        about_info = f"VodSlicer v{self.version}\n\nAuthor: ChillFacToR032 \nchill@chillaspect.com\n\nhttps://github.com/chillfactor032/VodSlicer"
        ret = QMessageBox.about(self, "VodSlicer", about_info)

    def get_selected_vod(self):
        sel_indexes = self.vod_list_view.selectedIndexes()
        if(len(sel_indexes)>0):
            return sel_indexes[0].data()
        return None

    def click_save_button(self):
        self.settings.setValue("VodSlicer/vod_url", self.vod_url_edit.text().strip())
        self.settings.setValue("VodSlicer/vod_user", self.user_edit.text().strip())
        self.settings.setValue("VodSlicer/vod_password", self.password_edit.text().strip())
        self.settings.sync()
        self.refresh()

    def refresh(self, launch=False):
        self.vod_list_model.removeRows(0, self.vod_list_model.rowCount())
        self.vod_url = self.vod_url_edit.text().strip()
        self.vod_user = self.user_edit.text().strip()
        self.vod_password = self.password_edit.text()
        self.refresh_index(launch, self.vod_url, self.vod_user, self.vod_password)
    
    def get_content_type(self, url, user="", password=""):
        try:
            if(len(user)==0 and len(password)==0):
                r = requests.head(url)
            else:
                r = requests.head(url, auth=requests.auth.HTTPBasicAuth(user, password))
            r.raise_for_status()
        except Exception as e: raise

        if("Content-Type" in r.headers.keys()):
            return r.headers["Content-Type"]
        return "Content Type Missing"
        
    def refresh_index(self, launch, url, user="", password=""):
        if(len(url)==0):
            return
        index = []
        r = None
        local_file = True
        if(len(url) >= 4 and url[:4].lower() == "http"):
            try:
                content_type = self.get_content_type(url, user, password)
                if(content_type == "video/mp4"):
                    self.set_status(f"Direct mp4 URL Saved")
                    return
                elif(content_type != "text/html"):
                    self.set_status(f"Invalid URL", 5000)
                    return

                # If content type is html, determin if its a directory listing
                if(len(user)==0 and len(password)==0):
                    r = requests.get(url)
                else:
                    r = requests.get(url, auth=requests.auth.HTTPBasicAuth(user, password))
                r.raise_for_status()
            except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError) as err:
                QMessageBox.warning(self, "VoD Slicer", f"Could not request VoDs\n\n{repr(err)}")
                return
            except requests.HTTPError as err:
                QMessageBox.warning(self, "VoD Slicer", f"HTTP Error\n\n{str(err)}")
                return

            # Content is html and we successfully have response
            index_raw = r.text

            if("Index of" not in index_raw):
                QMessageBox.warning(self, "VoD Slicer", f"URL does not appear to be a directory listing or mp4 file.\n\nEnsure the URL is of the VoD direcoty listing, or an mp4 file.")
                return

            index_lines = r.text.splitlines()
            for line in index_lines:
                regex = re.findall(r'<a href="(.+?)">', line)
                if(regex and len(regex)>0):
                    link = regex[0]
                    name = urllib.parse.unquote(link)
                    if(name[-4:]!=".mp4"):
                        continue
                    index.append({"link":f"{url}{link}", "name":name})
            index.reverse()
            self.index = index
            self.vod_list_model.clear()
            for index in self.index:
                item = QStandardItem(index["name"])
                self.vod_list_model.appendRow(item)
            if(self.vod_list_model.rowCount()>0):
                i = self.vod_list_model.index(0, 0)
                self.vod_list_view.setCurrentIndex(i)
        else:
            if(os.path.exists(url)):
                #Pass Exists: File or Dir?
                if(os.path.isdir(url)):
                    # Is Directory
                    index = []
                    for file in os.listdir(url):
                        if file.endswith(".mp4"):
                            link = os.path.join(url, file).replace("\\", "/")
                            index.append({"link": link, "name": file})
                    self.index = index
                    self.vod_list_model.clear()
                    for index in self.index:
                        item = QStandardItem(index["name"])
                        self.vod_list_model.appendRow(item)
                    if(self.vod_list_model.rowCount()>0):
                        i = self.vod_list_model.index(0, 0)
                        self.vod_list_view.setCurrentIndex(i)
                elif(os.path.isfile(url)):
                    #Its a file
                    if(len(url)>=4 and url[-4:].lower() == ".mp4"):
                        #Looks like an MP4
                        self.set_status("Local MP4 File Loaded")
                    else:
                        self.set_status("Unsupported file type", 5000)
                else:
                    self.set_status("Unsupported file type", 5000)
            else:
                self.set_status("Path does not exist", 5000)

    def click_slice_button(self):
        content_type = ""
        # Read User and Password
        self.vod_user = self.user_edit.text().strip()
        self.vod_password = self.password_edit.text()

        if(len(self.vod_user)==0):
            self.vod_user = None

        if(len(self.vod_password)==0):
            self.vod_password = None

        # Determin if link from VoD explorer or direct mp4 file
        vod_name = self.get_selected_vod()
        vod_url = None
        for ind in self.index:
            if(ind["name"] == vod_name):
                vod_url = ind["link"]
                break
        if(vod_url is None):
            vod_url = self.vod_url_edit.text().strip()
            if(vod_url.startswith("http")):
                content_type = self.get_content_type(vod_url, self.vod_user,  self.vod_password)
                if(content_type != "video/mp4"):
                    # No vod selected and link isnt mp4 file
                    QMessageBox.warning(self, "VoD Slicer", f"Invalid VoD URL\n\nURL is not link to a directory listing or direct mp4 file")
                    return
        self.vod_url = vod_url

        if(self.vod_url.startswith("http") == False):
            #If its a local file, set username and password to None
            self.vod_user = None
            self.vod_password = None

        # Get clip name and save location
        clip_name = self.clip_name_edit.text().strip()
        if(len(clip_name) == 0):
            clip_name = "clip.mp4"
        if(clip_name[-4:] != ".mp4"):
            clip_name = clip_name + ".mp4"
        default_path = os.path.join(self.previous_save_dir, clip_name).replace("\\", "/")
        response = QFileDialog.getSaveFileName(self, "Clip File Destination", default_path, "mp4 Video (*.mp4)")
        filename = response[0]
        if(len(filename) == 0):
            return
        split = os.path.split(filename)
        if(len(split)>0):
            self.previous_save_dir = split[0]
            self.settings.setValue("VodSlicer/previous_save_dir", self.previous_save_dir)
        
        start = self.start_time_edit.text().strip()
        end = self.end_time_edit.text().strip()
        self.progress_dialog = ProgressDialog()
        self.vodslicer = VodSlicer(self.ffmpeg_path, self.vod_url, self.vod_user, self.vod_password, start, end, filename, self.ffmpeg_md5, self.os)
        self.vodslicer.signals.done.connect(self.vodslicer_done)
        self.vodslicer.signals.progress.connect(self.vodslicer_progress)
        self.save_button.setEnabled(False)
        self.slice_button.setEnabled(False)
        self.threadpool.start(self.vodslicer)
        result = self.progress_dialog.exec()
        if(result == QDialog.Rejected):
            self.vodslicer.abort()

    def vodslicer_progress(self, progress_dict):
        self.progress_dialog.update_progress(progress_dict)

    def vodslicer_done(self, result, msg, file=None):
        self.progress_dialog.finish()
        self.save_button.setEnabled(True)
        self.slice_button.setEnabled(True)
        if(result):
            if(file is None):
                QMessageBox.information(self, "VodSlicer Done", f"{msg}")
            else:
                if(os.path.isfile(file)):
                    choice = QMessageBox.information(self, 
                        "VodSlicer Done", 
                        f"{msg}\n\nWould you like to open the clip location?",
                        (QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No),
                        QMessageBox.StandardButton.No)
                if(choice == QMessageBox.StandardButton.Yes):
                    dir = os.path.dirname(file)
                    if(os.path.isdir(dir)):
                        os.startfile(dir)
        else:
            QMessageBox.critical(self, "VodSlicer Failed", f"{msg}")

    def set_status(self, msg, timeout=0):
        if(timeout==0):
            self.status_msg = msg
        self.status_bar.showMessage(msg, timeout)

    def closeEvent(self, evt):
        self.settings.setValue("VodSlicer/vod_url", self.vod_url_edit.text().strip())
        self.settings.setValue("VodSlicer/vod_user", self.user_edit.text().strip())
        self.settings.setValue("VodSlicer/vod_password", self.password_edit.text().strip())
        self.settings.setValue("VodSlicer/geometry", self.saveGeometry())
        self.settings.setValue("VodSlicer/windowState", self.saveState())
        self.settings.sync()

class VodSlicer(QRunnable):

    class Signals(QObject):
        done = Signal(bool, str, str)
        progress = Signal(dict)

    def __init__(self, ffmpeg_path, url, user, password, start, end, outfile_path, md5hash, os):
        super(VodSlicer, self).__init__()
        self.signals = self.Signals()
        self.ffmpeg_binary_path = ffmpeg_path
        self.set_url(url, user, password)
        self.set_times(start, end)
        self.output_file = outfile_path
        self._abort = False
        self.md5hash = md5hash
        self.output = ""
        self.os = os

    def set_output_file(self, outfile):
        self.output_file = outfile

    def set_times(self, start, end):
        if(type(start) == int or type(start) == float):
            self.start_secs = start
        else:
            self.start_secs = self._str_to_secs(start)
        if(type(end) == int or type(end) == float):
            self.end_secs = end
        else:
            self.end_secs = self._str_to_secs(end)
        self.duration_secs = self.end_secs - self.start_secs

    def set_url(self, url, user=None, password=None):
        if(user is None or password is None):
            self.url = url
        else:
            self.url = url
            split = url.split("//")
            http = split[0] + "//"
            base_url = split[1]
            self.url = f"{http}{user}:{password}@{base_url}"

    def _str_to_secs(self, time_str):
        hours = 0
        mins = 0
        secs = 0
        try:
            ms = 0
            split = time_str.split(":")
            if(len(split)==3):
                hours = int(int(split[0]))
                mins = int(split[1])
                secs = float(split[2])
            elif(len(split)==2):
                mins = int(split[0])
                secs = float(split[1])
        except Exception as e:
            return 0
        return (hours * 60 * 60) + (mins * 60) + secs

    def run(self):
        if(self.duration_secs<=0):
            self.done(False, "Invalid times specified.")

        progress_dict = {}
        progress_dict["status"] = "Verifying integrity of ffmpeg"
        self.signals.progress.emit(progress_dict)

        # Verify integrity of ffmpeg binary
        md5 = ""
        with open(self.ffmpeg_binary_path, 'rb') as f:
            ffmpeg_bytes = f.read()    
            md5 = hashlib.md5(ffmpeg_bytes).hexdigest()
        if(md5 != self.md5hash):
            self.done(False, "FFMPEG file verification failed.")

        cmd = [
            self.ffmpeg_binary_path,
            "-y",
            "-ss", 
            "%0.2f"%self.start_secs,
            "-i", self.url,
            "-t", "%0.2f"%self.duration_secs,
            "-map", "0", "-vcodec", "copy", "-acodec", "copy", self.output_file
        ]
        
        progress_dict["status"] = "Analyzing MP4 Atoms"
        self.signals.progress.emit(progress_dict)

        # Run FFMPEG To extract video data from timestamps
        if self.os == "win":
            si = subprocess.STARTUPINFO()
            si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            process = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdin=subprocess.PIPE, startupinfo=si)
        else:
            process = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        process.stdin.write("?q".encode("utf-8"))
        chunk = ""
        while process.poll() is None:
            chunk += process.stderr.read(16).decode("utf-8")
            
            if("\r" in chunk):
                split = chunk.split("\r")
                chunk = split[0]
                self.output += chunk
                self.process_output(chunk)
                chunk = split[1]
            if(self._abort):
                process.terminate()
                break
            time.sleep(0.01)

        if(self._abort):
            self.done(False, "Slicing Aborted")
            return
        else:
            if(process.returncode == 0):
                self.done(True, "Slicing Successful", self.output_file)
            else:
                print(self.output)
                self.done(False, f"FFMPEG exe error, Invalid URL?\n\n FFMPEG Return Code: {process.returncode}")

    def get_output(self):
        return self.output

    def abort(self):
        self._abort = True

    def process_output(self, line):
        percent = 0
        msg = ""
        line = line.strip()
        if(line[0:6] != "frame="):
            return
        progress_dict = {}
        element_list = []
        split = line.split("=")
        for x in range(0, len(split)):
            split[x] = split[x].strip()
            split2 = split[x].split(" ")
            if(len(split2)>1):
                element_list.extend(split2)
            else:
                element_list.append(split[x])
        if(len(element_list)%2==1):
            return
        for x in range(0, len(element_list), 2):
            progress_dict[element_list[x]] = element_list[x+1]
            if(element_list[x] == "time"):
                elapsed = self._str_to_secs(element_list[x+1])
                percent = (elapsed / self.duration_secs)*100
                progress_dict["progress"] = round(percent,2)
        progress_dict["status"] = "Extracting video data"
        self.signals.progress.emit(progress_dict)

    def done(self, result, msg, file=None):
        self.signals.done.emit(result, msg, file)


class ProgressDialog(QDialog):

    class Signals(QObject):
        abort = Signal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.signals = self.Signals()
        self.ui = UI.Ui_ProgressDialog()
        self.ui.setupUi(self)
        self.ui.abort_button.clicked.connect(self.abort)
        self.ui.progress_bar.setMinimum(0)
        self.ui.progress_bar.setMaximum(0)
        self.ui.progress_bar.setValue(0)
        self.ui.border_group_box.setStyleSheet("QGroupBox { border: 2px solid rgb(42, 130, 218);  border-radius: 3px; }")

    def update_progress(self, progress_dict):
        if("frame" in progress_dict.keys()):
            self.ui.frame_label.setText(progress_dict["frame"])
        if("fps" in progress_dict.keys()):
            self.ui.fps_label.setText(progress_dict["fps"])
        if("size" in progress_dict.keys()):
            s = progress_dict["size"].replace("kB", "")
            kB = int(s)
            if(kB > 1024):
                kB = round(kB/1024, 1)
                s = f"{kB} MB"
            else:
                s = f"{kB} KB"
            self.ui.size_label.setText(s)
        if("time" in progress_dict.keys()):
            self.ui.time_label.setText(progress_dict["time"])
        if("bitrate" in progress_dict.keys()):
            self.ui.bitrate_label.setText(progress_dict["bitrate"])
        if("speed" in progress_dict.keys()):
            self.ui.speed_label.setText(progress_dict["speed"])
        if("status" in progress_dict.keys()):
            self.ui.status_label.setText(progress_dict["status"])
        if("progress" in progress_dict.keys()):
            self.ui.progress_bar.setMaximum(100)
            self.ui.progress_bar.setValue(progress_dict["progress"])
    
    def finish(self):
        self.done(QDialog.Accepted)

    def abort(self):
        self.done(QDialog.Rejected)

if __name__ == "__main__":
    app_name = "VodSlicer"
    org_name = "ChillAspect"
    app = QApplication(sys.argv)
    app.setOrganizationName(org_name)
    app.setApplicationName(app_name)
    app.setStyle(QStyleFactory.create("Fusion"))
    palette = QPalette()
    background_color = QColor(21,32,43)
    background_alt_color = QColor(34,48,60)
    button_color = QColor(136, 153, 166)
    disabledColor = QColor(127,127,127)
    palette.setColor(QPalette.Window, background_color)
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(18,18,18))
    palette.setColor(QPalette.AlternateBase, background_alt_color)
    palette.setColor(QPalette.ToolTipBase, Qt.white)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Disabled, QPalette.Text, disabledColor)
    palette.setColor(QPalette.Button, button_color)
    palette.setColor(QPalette.ButtonText, background_color)
    palette.setColor(QPalette.Disabled, QPalette.ButtonText, disabledColor)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    palette.setColor(QPalette.Disabled, QPalette.HighlightedText, disabledColor)
    app.setPalette(palette)
    app.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
    window = VodSlicerApp()
    window.show()
    sys.exit(app.exec())