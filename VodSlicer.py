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
from PySide6.QtWidgets import QApplication, QMainWindow, QStyle, QMessageBox, QLineEdit, QFileDialog, QDialog, QStyleFactory, QToolButton, QLabel, QTableWidgetItem, QHeaderView
from PySide6.QtCore import QFile, Signal, QObject, QStandardPaths, QSettings, QSize, Qt, QTextStream, QThreadPool, QRunnable, QUrl, QTimer
from PySide6.QtGui import QMouseEvent, QStandardItemModel, QStandardItem, QPixmap, QIcon, QMovie
from PySide6.QtMultimedia import QAudioOutput, QMediaFormat, QMediaPlayer
from PySide6.QtMultimediaWidgets import QVideoWidget

# VodSlicer Imports
import Resources_rc
import ui as UI

class VodSlicerApp(QMainWindow, UI.Ui_VodSlicer):
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
        download_locations = QStandardPaths.standardLocations(QStandardPaths.DownloadLocation)
        if len(download_locations) > 0:
            self.downloads_dir = download_locations[0]
        else:
            self.downloads_dir = self.documents_dir

        # Create config directory if it doesnt exist
        if not os.path.isdir(self.config_dir):
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
        if os.path.exists(self.ffmpeg_path)==False:
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
            os.chmod(self.ffmpeg_path, stat.S_IRWXU | stat.S_IRGRP | stat.S_IROTH)

        # Get Settings From Ini File
        self.settings = QSettings(self.ini_path, QSettings.IniFormat)
        self.vod_url = self.settings.value("VodSlicer/vod_url", "")
        self.vod_user = self.settings.value("VodSlicer/vod_user", "")
        self.vod_password = self.settings.value("VodSlicer/vod_password", "")
        self.previous_save_dir = self.settings.value("VodSlicer/previous_save_dir", self.documents_dir)
        self.previous_open_dir = self.settings.value("VodSlicer/previous_open_dir", self.documents_dir)
        self.volume = int(self.settings.value("VodSlicer/volume", "50"))

        #Load UI Components
        self.setupUi(self)
        self.setWindowTitle(f"{self.app_name} {self.version} by ChillFacToR")
        self.progress_dialog = ProgressDialog(self)
        self.permanent_status_label = QLabel()
        self.statusbar.addPermanentWidget(self.permanent_status_label)
        self.rewind_button = HoldButton(parent=self)
        self.rewind_button.setFixedSize(QSize(50,35))
        self.rewind_button.setIconSize(QSize(24,24))
        self.forward_button = HoldButton(parent=self)
        self.forward_button.setFixedSize(QSize(50,35))
        self.forward_button.setIconSize(QSize(24,24))
        self.video_controls_widget.layout().removeWidget(self.play_button)
        self.video_controls_widget.layout().addWidget(self.rewind_button)
        self.video_controls_widget.layout().addWidget(self.play_button)
        self.video_controls_widget.layout().addWidget(self.forward_button)

        #Get Icons
        default_icon_pixmap = QStyle.StandardPixmap.SP_FileDialogListView
        icon_pixmap = QPixmap(":resources/img/vod_slicer.ico")
        self.vodslicer_icon = QIcon(icon_pixmap)
        default_icon = self.style().standardIcon(default_icon_pixmap)
        if(self.vodslicer_icon):
            self.setWindowIcon(self.vodslicer_icon)
        else:
            self.setWindowIcon(default_icon)
            self.vodslicer_icon = default_icon
        self.rewind_icon_pixmap = QPixmap(":resources/img/rewind.svg")
        self.rewind_icon = QIcon(self.rewind_icon_pixmap)
        self.foward_icon_pixmap = QPixmap(":resources/img/fast-forward.svg")
        self.foward_icon = QIcon(self.foward_icon_pixmap)
        self.play_icon_pixmap = QPixmap(":resources/img/play.svg")
        self.pause_icon_pixmap = QPixmap(":resources/img/pause.svg")
        self.play_icon = QIcon(self.play_icon_pixmap)
        self.pause_icon = QIcon(self.pause_icon_pixmap)
        self.loading_label.setAlignment(Qt.AlignCenter)
        self.loading_gif = QMovie(":resources/img/loading.gif")
        self.loading_label.setMovie(self.loading_gif)
        self.loading_gif.start()

        # Setup Video Player
        self.volume_slider.setValue(self.volume)
        self.play_button.setEnabled(False)
        #self.rewind_button.setEnabled(False)
        #self.forward_button.setEnabled(False)
        self.save_clip_button.setEnabled(False)
        self.markers_button.setEnabled(False)
        self.audio_output = QAudioOutput()
        self.volume_slider.valueChanged.connect(self.set_volume)
        self.video_player = QMediaPlayer()
        self.video_player.setAudioOutput(self.audio_output)
        self.video_player.errorOccurred.connect(self.video_player_error)
        self.video_player.positionChanged.connect(self.position_changed)
        self.video_player.mediaStatusChanged.connect(self.media_status_change)
        self.video_player.playingChanged.connect(self.playing_changed)
        self.video_widget = QVideoWidget()
        self.video_player_widget.layout().addWidget(self.video_widget, 0, 0)
        self.video_player.setVideoOutput(self.video_widget)
        self.video_duration = 0
        self.cur_frame = 0
        self.clip_start_frame = 0
        self.clip_end_frame = 0
        self.resume_on_release = False
        self.seek_position_frame = 0
        self.cur_video_source_url = ""

        # Button Signals
        self.online_video_button.clicked.connect(self.online_video_clicked)
        self.local_video_button.clicked.connect(self.local_video_clicked)
        self.about_button.clicked.connect(self.show_about)
        self.clip_start_button.clicked.connect(self.clip_start_clicked)
        self.clip_end_button.clicked.connect(self.clip_end_clicked)
        #self.rewind_button.clicked.connect(self.rewind_clicked)
        #self.forward_button.clicked.connect(self.forward_clicked)
        self.play_button.clicked.connect(self.play_clicked)
        self.save_clip_button.clicked.connect(self.save_clip_clicked)
        self.markers_button.clicked.connect(self.markers_clicked)
        self.video_slider.sliderMoved.connect(self.video_slider_moved)
        self.video_slider.sliderPressed.connect(self.video_slider_pressed)
        self.video_slider.sliderReleased.connect(self.video_slider_released)
        self.rewind_button.setIcon(self.rewind_icon)
        self.forward_button.setIcon(self.foward_icon)

        ## ThreadPool
        self.threadpool = QThreadPool()

        geometry = self.settings.value("VodSlicer/geometry")
        window_state = self.settings.value("VodSlicer/windowState")
        if geometry and window_state:
            self.restoreGeometry(geometry) 
            self.restoreState(window_state)

    def set_volume(self):
        self.volume = self.volume_slider.value()
        self.settings.setValue("VodSlicer/volume", self.volume)
        self.audio_output.setVolume(self.volume / 100.00)
        self.statusbar.showMessage(f"Volume {self.volume}%", 1000)

    def online_video_clicked(self):
        self.video_player.pause()
        dlg = VodDialog(self, self.vod_url, self.vod_user, self.vod_password)
        result = dlg.exec()
        if result == QDialog.Accepted:
            src = dlg.selected_url
            file = dlg.selected_file
            if src is not None:
                self.permanent_status_label.setText(f"{file}")
                self.load_video(src)

    def local_video_clicked(self):
        if self.video_player.playbackState() == QMediaPlayer.PlayingState:
            self.video_player.pause()
        fileName = QFileDialog.getOpenFileName(self,"Open Video", self.previous_open_dir, "Video Files (*.mp4)")
        if len(fileName[0]) > 0: 
            self.previous_open_dir = os.path.dirname(fileName[0])
            self.settings.setValue("VodSlicer/previous_open_dir", self.previous_open_dir)
            self.permanent_status_label.setText(f"{fileName[0]}")
            self.load_video(fileName[0])

    def clip_start_clicked(self):
        self.clip_start_edit.setText(self.msToStr(self.cur_frame, True))
        self.clip_start_frame = self.cur_frame

    def clip_end_clicked(self):
        self.clip_end_edit.setText(self.msToStr(self.cur_frame, True))
        self.clip_end_frame = self.cur_frame
    
    def loading_screen(self, on=True):
        if on:
            self.video_player_stacked_widget.setCurrentIndex(1)
        else:
            self.video_player_stacked_widget.setCurrentIndex(0)


    # Video Player Functions
    def rewind_clicked(self):
        cur_pos = self.video_player.position()
        print(f"Current Position: {cur_pos}")
    
    def forward_clicked(self):
        print("Forward Button")
    
    def load_video(self, url, local=True):
        self.play_button.setEnabled(False)
        self.rewind_button.setEnabled(False)
        self.forward_button.setEnabled(False)
        self.save_clip_button.setEnabled(False)
        self.markers_button.setEnabled(False)
        self.video_player.stop()
        time.sleep(0.1)
        self.clip_start_edit.setText("00:00:00")
        self.clip_end_edit.setText("00:00:00")
        self.cur_time_label.setText("00:00:00")
        self.clip_start_frame = 0
        self.clip_end_frame = 0
        self.seek_position_frame = 0
        self.video_slider.setValue(0)
        self.cur_frame = 0
        if local:
            self.video_player.setSource(QUrl.fromLocalFile(url))
        else:
            self.video_player.setSource(QUrl(url))
        self.cur_video_source_url = url
        self.play_button.setEnabled(True)
        self.rewind_button.setEnabled(True)
        self.forward_button.setEnabled(True)
        self.save_clip_button.setEnabled(True)
        self.markers_button.setEnabled(True)
        self.audio_output.setVolume(self.volume / 100.00)
        self.video_player.play()
        self.video_player.pause()

    def media_status_change(self, status):
        print(f"Media Status: {str(status)}")
        if status == QMediaPlayer.NoMedia:
            self.loading_screen(False)
        if status == QMediaPlayer.LoadingMedia:
            self.loading_screen()
            self.statusbar.showMessage("Loading media...")
        if status == QMediaPlayer.LoadedMedia:
            self.loading_screen(False)
            self.statusbar.showMessage("Media Ready")
        if status == QMediaPlayer.StalledMedia:
            self.loading_screen(False)
        if status == QMediaPlayer.BufferingMedia:
            self.loading_screen()
            self.statusbar.showMessage("Buffering...")
        if status == QMediaPlayer.BufferedMedia:
            self.loading_screen(False)
            self.statusbar.showMessage("Media Ready")
        if status == QMediaPlayer.EndOfMedia:
            pass
        if status == QMediaPlayer.InvalidMedia:
            pass

    def duration_changed(self, duration):
        pass

    def stop_video(self):
        self.video_player.setPosition(self.video_player.duration())

    def playing_changed(self, playing):
        if playing:
            self.play_button.setIcon(self.pause_icon)
        else:
            self.play_button.setIcon(self.play_icon)

    def play_clicked(self):
        # Play or Pause
        if self.video_player.playbackState() != QMediaPlayer.PlayingState:
            self.video_player.play()
        else:
            self.video_player.pause()
    
    def position_changed(self, position):
        self.cur_frame = position
        self.cur_time_label.setText(self.msToStr(position, True))
        percent = self.cur_frame / self.video_player.duration() * 10000.0
        self.video_slider.setValue(percent)

    def video_slider_released(self):
        if self.seek_position_frame != self.cur_frame:
            self.video_player.setPosition(int(self.seek_position_frame))
        if self.resume_on_release:
            self.video_player.play()
            self.resume_on_release = False
    
    def video_slider_pressed(self):
        if self.video_player.playbackState() == QMediaPlayer.PlayingState:
            self.resume_on_release = True
            self.video_player.pause()
        self.seek_position_frame = self.cur_frame
            
    def video_slider_moved(self):
        slider = self.video_slider.value()
        percent = slider / self.video_slider.maximum()
        self.seek_position_frame = self.video_player.duration() * percent
        self.cur_time_label.setText(self.msToStr(self.seek_position_frame, True))

    def save_clip_clicked(self):
        slices = []
        clip_start_secs = self.strToSecs(self.clip_start_edit.text())
        clip_end_secs = self.strToSecs(self.clip_end_edit.text())
        if clip_end_secs <= clip_start_secs:
            QMessageBox.warning(self, "Error", "Clip start and end times are invalid.")
            return
        result = QFileDialog.getSaveFileName(self, "Clip Save Location", self.previous_save_dir, "Video (*.mp4)")
        if len(result[0]) == 0:
            return
        filename = result[0]
        self.previous_save_dir = os.path.dirname(result[0])
        self.settings.setValue("VodSlicer/previous_save_dir", self.previous_save_dir)
        self.progress_dialog = ProgressDialog(self)
        slices.append([clip_start_secs, clip_end_secs, filename])
        self.vodslicer = VodSlicer(self.ffmpeg_path, self.cur_video_source_url, self.ffmpeg_md5, self.os)
        self.vodslicer.addSlices(slices)
        self.vodslicer.signals.done.connect(self.vodslicer_done)
        self.vodslicer.signals.progress.connect(self.vodslicer_progress)
        #disable UI components during this
        self.centralwidget.setEnabled(False)
        self.threadpool.start(self.vodslicer)
        result = self.progress_dialog.exec()
        if result == QDialog.Rejected:
            self.vodslicer.abort()
            if os.path.exists(filename):
                os.remove(filename)
    
    def markers_clicked(self):
        result = QFileDialog.getOpenFileName(self, "Import Stream Markers File", self.downloads_dir, "Stream Markers (*.csv)")
        if len(result[0]) == 0:
            return
        data = self.import_markers_csv(result[0])
        if len(data) == 0:
            return
        marker_dialog = MarkersDialog(self, data)
        result = marker_dialog.exec()
        if result == QDialog.Accepted:
            clips = marker_dialog.get_clips()
            print(clips)
            # To Do get save file location
            # Do Slicing
        else:
            return

    def video_player_error(self, error, error_string):
        print(error_string, file=sys.stderr)
        ret = QMessageBox.warning(self, "Error", str(error) + "\n\n" + error_string)

    def import_markers_csv(self, path):
        if not os.path.exists(path):
            return []
        data = []
        with open(path, "r") as markers_file:
            lines = markers_file.readlines()
            for line in lines:
                parts = line.strip().split(",")
                time = "00:00:00"
                role = "Unknown"
                creator = "Unknown"
                name = "clip"
                if len(parts) > 0:
                    time = parts[0]
                    while len(time) < 8:
                        time = "0" + time
                if len(parts) > 1:
                    role = parts[1]
                if len(parts) > 2:
                    creator = parts[2]
                if len(parts) > 3:
                    name = parts[3]
                    if len(name) == 0:
                        time_str = time.replace(":", "_")
                        name = f"clip_{time_str}"
                data.append([name, time, role, creator])
        return data

    def show_about(self):
        about_info = f"VodSlicer v{self.version}\n\nAuthor: ChillFacToR032 \nchill@chillaspect.com\n\nhttps://github.com/chillfactor032/VodSlicer"
        ret = QMessageBox.about(self, "VodSlicer", about_info)

    def vodslicer_progress(self, progress_dict):
        self.progress_dialog.update_progress(progress_dict)

    def vodslicer_done(self, result, msg, file=None):
        self.progress_dialog.finish()
        self.centralwidget.setEnabled(True)
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
                        if self.os == "win":
                            os.startfile(dir)
                        else:
                            subprocess.call(["open", dir])
        else:
            QMessageBox.critical(self, "VodSlicer Failed", f"{msg}")

    def secsToStr(self, secs, ms=False):
        hours, secs = divmod(secs, 3600)
        mins, secs = divmod(secs, 60)
        if ms:
            return "{:02d}:{:02d}:{:06.3f}".format(int(hours), int(mins), secs) 
        return "{:02d}:{:02d}:{:02d}".format(int(hours), int(mins), int(secs)) 
    
    def strToSecs(self, time_str):
        split = time_str.split(":")
        hours = int(split[0])
        mins = int(split[1])
        secs = int(split[2])
        return (hours * 3600) + (mins * 60) + secs

    def msToStr(self, ms, show_ms=False):
        return self.secsToStr(ms/1000.0, show_ms)
    
    def closeEvent(self, evt):
        self.settings.setValue("VodSlicer/vod_url", self.vod_url)
        self.settings.setValue("VodSlicer/vod_user", self.vod_user)
        self.settings.setValue("VodSlicer/vod_password", self.vod_password)
        self.settings.setValue("VodSlicer/geometry", self.saveGeometry())
        self.settings.setValue("VodSlicer/windowState", self.saveState())
        self.settings.sync()

class HoldButton(QToolButton):
    def __init__(self, *args, **kwargs):
        super(HoldButton, self).__init__(*args, **kwargs)
        self.mouse_down_time = 0

    def mousePressEvent(self, event: QMouseEvent) -> None:
        return super().mousePressEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        self.mouse_down_time = 0
        return super().mouseReleaseEvent(event)
    

class VodSlicer(QRunnable):

    class Signals(QObject):
        done = Signal(bool, str, str)
        progress = Signal(dict)

    def __init__(self, ffmpeg_path, url, md5hash, os):
        super(VodSlicer, self).__init__()
        self.signals = self.Signals()
        self.ffmpeg_binary_path = ffmpeg_path
        self.url = url
        self._abort = False
        self.md5hash = md5hash
        self.output = ""
        self.os = os
        self.slices = []

    def addSlices(self, slices:list):
        self.slices = slices

    def addSlice(self, start_secs, end_secs, outfile_path):
        self.slices.append([start_secs, end_secs, outfile_path])

    def run(self):
        progress_dict = {}
        progress_dict["status"] = "Verifying integrity of ffmpeg"
        self.signals.progress.emit(progress_dict)

        # Verify integrity of ffmpeg binary
        md5 = ""
        with open(self.ffmpeg_binary_path, 'rb') as f:
            ffmpeg_bytes = f.read()    
            md5 = hashlib.md5(ffmpeg_bytes).hexdigest()
        if md5 != self.md5hash:
            self.done(False, "FFMPEG file verification failed.")
            return

        errors = False
        cur_slice = 0
        for slice in self.slices:
            cur_slice += 1
            progress_dict["status"] = "Starting slicing"
            progress_dict["curclip"] = f"{cur_slice} of {len(self.slices)}"
            self.signals.progress.emit(progress_dict)
            start_secs = slice[0]
            end_secs = slice[1]
            output_file = slice[2]
            duration_secs = end_secs - start_secs

            if(duration_secs<=0):
                self.done(False, f"Invalid times specified in clip:\n{output_file}")

            cmd = [
                self.ffmpeg_binary_path,
                "-y",
                "-ss", 
                "%0.2f"%start_secs,
                "-i", self.url,
                "-t", "%0.2f"%duration_secs,
                "-map", "0", "-vcodec", "copy", "-acodec", "copy", output_file
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
                if "\r" in chunk:
                    split = chunk.split("\r")
                    chunk = split[0]
                    self.output += chunk
                    self.process_output(chunk)
                    chunk = split[1]
                if self._abort:
                    process.terminate()
                    break
                time.sleep(0.01)

            if self._abort:
                self.done(False, "Slicing Aborted")
                return
            if process.returncode != 0:
                print(self.output)
                self.done(False, f"FFMPEG error, Invalid URL?\n\n FFMPEG Return Code: {process.returncode}")
                return
        self.done(True, "Slicing Successful", output_file)

    def get_output(self):
        return self.output

    def abort(self):
        self._abort = True

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
            if element_list[x] == "time":
                print(f"Convert str to seconds: [{element_list[x+1]}]")
                elapsed = self._str_to_secs(element_list[x+1])
                percent = (elapsed / self.duration_secs)*100
                progress_dict["progress"] = round(percent,2)
        progress_dict["status"] = "Extracting video data"
        self.signals.progress.emit(progress_dict)

    def done(self, result, msg, file=None):
        self.signals.done.emit(result, msg, file)


class VodDialog(QDialog):
    
    def __init__(self, parent, url, user="", password=""):
        super().__init__(parent)
        self.url = url
        self.user = user
        self.password = password
        self.ui = UI.Ui_OpenDialog()
        self.ui.setupUi(self)
        self.loading_label = QLabel()
        self.loading_gif = QMovie(":resources/img/loading.gif")
        self.loading_label.setMovie(self.loading_gif)
        self.loading_gif.start()
        self.loading_label.setAlignment(Qt.AlignCenter)
        self.ui.main_widget.layout().addWidget(self.loading_label, 0, 0)
        self.ui.open_button.clicked.connect(self.open_clicked)
        self.ui.refresh_button.clicked.connect(self.refresh_clicked)
        self.vod_list_model = QStandardItemModel()
        self.ui.vod_list_view.setModel(self.vod_list_model)
        self.ui.vod_list_view.setSpacing(3)
        self.ui.url_edit.setText(self.url)
        self.ui.url_edit.setCursorPosition(0)
        self.ui.user_edit.setText(self.user)
        self.ui.password_edit.setText(self.password)
        self.ui.password_edit.setEchoMode(QLineEdit.Password)
        self.selected_url = None
        self.selected_file = ""
        self.loading_screen()
        QTimer.singleShot(1000, self.refresh)

    def loading_screen(self, on=True):
        self.ui.url_edit.setEnabled(not on)
        self.ui.user_edit.setEnabled(not on)
        self.ui.password_edit.setEnabled(not on)
        #self.ui.vod_list_view.setVisible(not on)
        self.loading_label.setVisible(on)

    def refresh_clicked(self):
        self.loading_screen()
        self.refresh()

    def open_clicked(self):
        vod = self.get_selected_vod()
        self.selected_file = vod
        if vod is not None:
            prefix = "https"
            host = ""
            parts = self.url.split("//")
            if len(parts) >= 2:
                prefix = parts[0]
                host = parts[1]
            if self.user is not None:
                self.selected_url = f"{prefix}//{self.user}:{self.password}@{host}/{vod}"
            else:
                self.selected_url = f"{self.url}/{vod}"
            self.accept()
    
    def refresh(self, launch=False):
        self.vod_list_model.removeRows(0, self.vod_list_model.rowCount())
        self.url = self.ui.url_edit.text().strip()
        self.user = self.ui.user_edit.text().strip()
        self.password = self.ui.password_edit.text()
        self.refresh_index(launch, self.url, self.user, self.password)
        self.loading_screen(False)
    
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
        if len(url)==0:
            return
        index = []
        r = None
        try:
            content_type = self.get_content_type(url, user, password)
            if content_type == "video/mp4":
                return
            elif content_type != "text/html":
                return

            # If content type is html, determin if its a directory listing
            if len(user)==0 and len(password)==0:
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
            self.ui.vod_list_view.setCurrentIndex(i)

    def get_selected_vod(self):
        sel_indexes = self.ui.vod_list_view.selectedIndexes()
        if(len(sel_indexes)>0):
            return sel_indexes[0].data()
        return None
    
class ProgressDialog(QDialog):

    class Signals(QObject):
        abort = Signal()
    
    def __init__(self, parent):
        super().__init__(parent)
        #self.setWindowFlags(Qt.FramelessWindowHint)
        self.signals = self.Signals()
        self.ui = UI.Ui_ProgressDialog()
        self.ui.setupUi(self)
        self.ui.abort_button.clicked.connect(self.abort)
        self.ui.progress_bar.setMinimum(0)
        self.ui.progress_bar.setMaximum(0)
        self.ui.progress_bar.setValue(0)
        self.ui.border_group_box.setStyleSheet("QGroupBox { border: 2px solid rgb(42, 130, 218);  border-radius: 3px; }")
        self.cur_clip = 1
        self.clip_count = 1
        self.ui.clip_count_label.setText(f"{self.cur_clip} of {self.clip_count}")

    def update_cur_clip(self, clip, clip_count=0):
        self.cur_clip = clip
        if clip_count > 0:
            self.clip_count = clip_count
        self.ui.clip_count_label.setText(f"{self.cur_clip} of {self.clip_count}")

    def update_progress(self, progress_dict):
        if "frame" in progress_dict.keys():
            self.ui.frame_label.setText(progress_dict["frame"])
        if "fps" in progress_dict.keys():
            self.ui.fps_label.setText(progress_dict["fps"])
        if "size" in progress_dict.keys():
            s = progress_dict["size"].replace("kB", "")
            kB = int(s)
            if(kB > 1024):
                kB = round(kB/1024, 1)
                s = f"{kB} MB"
            else:
                s = f"{kB} KB"
            self.ui.size_label.setText(s)
        if "time" in progress_dict.keys():
            self.ui.time_label.setText(progress_dict["time"])
        if "bitrate" in progress_dict.keys():
            self.ui.bitrate_label.setText(progress_dict["bitrate"])
        if "speed" in progress_dict.keys():
            self.ui.speed_label.setText(progress_dict["speed"])
        if "status" in progress_dict.keys():
            self.ui.status_label.setText(progress_dict["status"])
        if "progress" in progress_dict.keys():
            self.ui.progress_bar.setMaximum(100)
            self.ui.progress_bar.setValue(progress_dict["progress"])
        if "curclip" in progress_dict.keys():
            self.ui.clip_count_label.setText(progress_dict["curclip"])

    
    def finish(self):
        self.done(QDialog.Accepted)

    def abort(self):
        self.done(QDialog.Rejected)

class MarkersDialog(QDialog):
    
    def __init__(self, parent, marker_data:list):
        super().__init__(parent)
        self.clips = []
        self.marker_data = marker_data
        self.ui = UI.Ui_MarkersDialog()
        self.ui.setupUi(self)
        self.ui.cancel_button.clicked.connect(self.cancel_button_clicked)
        self.ui.create_button.clicked.connect(self.create_button_clicked)
        self.ui.marker_count_label.setText(str(len(marker_data)))
        self.ui.marker_table.setRowCount(len(marker_data))
        header = self.ui.marker_table.horizontalHeader()       
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.Stretch)
        for x in range(len(marker_data)):
            clip_name_item = QTableWidgetItem(marker_data[x][0])
            clip_time_item = QLineEdit("00:00:00")
            clip_time_item.setInputMask("99:99:99")
            clip_time_item.setMaxLength(8)
            clip_time_item.setText(marker_data[x][1])
            clip_role_item = QTableWidgetItem(marker_data[x][2])
            clip_creator_item = QTableWidgetItem(marker_data[x][3])
            self.ui.marker_table.setItem(x, 0, clip_name_item)
            self.ui.marker_table.setCellWidget(x, 1, clip_time_item)
            self.ui.marker_table.setItem(x, 2, clip_role_item)
            self.ui.marker_table.setItem(x, 3, clip_creator_item)

    def get_clips(self):
        return self.clips
    
    def strToSecs(self, time_str):
        split = time_str.split(":")
        hours = int(split[0])
        mins = int(split[1])
        secs = int(split[2])
        return (hours * 3600) + (mins * 60) + secs
    
    def cancel_button_clicked(self):
        self.clips = []
        self.reject()
    
    def create_button_clicked(self):
        self.clips = []
        secs_before = int(self.ui.clip_before_edit.text())
        secs_after = int(self.ui.clip_after_edit.text())
        for x in range(self.ui.marker_table.rowCount()):
            clip_name = self.ui.marker_table.item(x, 0).data(Qt.DisplayRole)
            clip_time_str = self.ui.marker_table.cellWidget(x, 1).text()
            clip_time_secs = self.strToSecs(clip_time_str)
            clip_start_secs = clip_time_secs-secs_before
            if clip_start_secs < 0:
                clip_start_secs = 0
            clip_end_secs = clip_time_secs+secs_after
            self.clips.append([clip_start_secs, clip_end_secs, clip_name])
        self.accept()

if __name__ == "__main__":
    app_name = "VodSlicer"
    org_name = "ChillAspect"
    app = QApplication(sys.argv)
    app.setOrganizationName(org_name)
    app.setApplicationName(app_name)
    app.setStyle(QStyleFactory.create("Fusion"))
    window = VodSlicerApp()
    window.show()
    sys.exit(app.exec())
