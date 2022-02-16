# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QLabel,
    QLineEdit, QListView, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 459)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 459))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.vod_explorer_box = QGroupBox(self.centralwidget)
        self.vod_explorer_box.setObjectName(u"vod_explorer_box")
        self.vod_explorer_box.setMinimumSize(QSize(476, 419))
        self.gridLayout_3 = QGridLayout(self.vod_explorer_box)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.vod_list_view = QListView(self.vod_explorer_box)
        self.vod_list_view.setObjectName(u"vod_list_view")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.vod_list_view.sizePolicy().hasHeightForWidth())
        self.vod_list_view.setSizePolicy(sizePolicy1)
        self.vod_list_view.setMinimumSize(QSize(415, 330))
        font = QFont()
        font.setPointSize(11)
        self.vod_list_view.setFont(font)
        self.vod_list_view.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.vod_list_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.vod_list_view.setAlternatingRowColors(False)

        self.gridLayout_2.addWidget(self.vod_list_view, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.vod_explorer_box, 0, 0, 2, 1)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy2)
        self.groupBox_3.setMinimumSize(QSize(300, 183))
        self.user_edit = QLineEdit(self.groupBox_3)
        self.user_edit.setObjectName(u"user_edit")
        self.user_edit.setGeometry(QRect(110, 80, 171, 22))
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 80, 71, 21))
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.password_edit = QLineEdit(self.groupBox_3)
        self.password_edit.setObjectName(u"password_edit")
        self.password_edit.setGeometry(QRect(110, 110, 171, 22))
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 110, 71, 21))
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 30, 251, 16))
        self.vod_url_edit = QLineEdit(self.groupBox_3)
        self.vod_url_edit.setObjectName(u"vod_url_edit")
        self.vod_url_edit.setGeometry(QRect(20, 50, 261, 22))
        self.save_button = QPushButton(self.groupBox_3)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setGeometry(QRect(189, 140, 91, 24))

        self.gridLayout.addWidget(self.groupBox_3, 0, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(300, 200))
        self.slice_button = QPushButton(self.groupBox_2)
        self.slice_button.setObjectName(u"slice_button")
        self.slice_button.setGeometry(QRect(20, 200, 261, 39))
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 49, 101, 31))
        font1 = QFont()
        font1.setPointSize(14)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.start_time_edit = QLineEdit(self.groupBox_2)
        self.start_time_edit.setObjectName(u"start_time_edit")
        self.start_time_edit.setGeometry(QRect(190, 50, 91, 31))
        self.start_time_edit.setFont(font1)
        self.start_time_edit.setAlignment(Qt.AlignCenter)
        self.end_time_edit = QLineEdit(self.groupBox_2)
        self.end_time_edit.setObjectName(u"end_time_edit")
        self.end_time_edit.setGeometry(QRect(190, 100, 91, 31))
        self.end_time_edit.setFont(font1)
        self.end_time_edit.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 99, 121, 31))
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.clip_name_edit = QLineEdit(self.groupBox_2)
        self.clip_name_edit.setObjectName(u"clip_name_edit")
        self.clip_name_edit.setGeometry(QRect(110, 161, 171, 31))
        font2 = QFont()
        font2.setPointSize(12)
        self.clip_name_edit.setFont(font2)
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 160, 91, 31))
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.groupBox_2, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.vod_explorer_box.setTitle(QCoreApplication.translate("MainWindow", u"VoD Explorer", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.user_edit.setInputMask("")
        self.user_edit.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"User Name:", None))
        self.password_edit.setInputMask("")
        self.password_edit.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Vod Index URL:", None))
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Load VoDs", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Slicer", None))
        self.slice_button.setText(QCoreApplication.translate("MainWindow", u"Slice!", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Start Time:", None))
        self.start_time_edit.setInputMask(QCoreApplication.translate("MainWindow", u"99:99:99", None))
        self.start_time_edit.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.end_time_edit.setInputMask(QCoreApplication.translate("MainWindow", u"99:99:99", None))
        self.end_time_edit.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"End Time:", None))
        self.clip_name_edit.setInputMask("")
        self.clip_name_edit.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Clip Name:", None))
    # retranslateUi



# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Progress.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QLabel,
    QProgressBar, QPushButton, QSizePolicy, QWidget)

class Ui_ProgressDialog(object):
    def setupUi(self, ProgressDialog):
        if not ProgressDialog.objectName():
            ProgressDialog.setObjectName(u"ProgressDialog")
        ProgressDialog.resize(400, 230)
        self.border_group_box = QGroupBox(ProgressDialog)
        self.border_group_box.setObjectName(u"border_group_box")
        self.border_group_box.setGeometry(QRect(10, 10, 380, 210))
        self.status_label = QLabel(self.border_group_box)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setGeometry(QRect(70, 20, 291, 16))
        self.frame_label = QLabel(self.border_group_box)
        self.frame_label.setObjectName(u"frame_label")
        self.frame_label.setGeometry(QRect(70, 50, 141, 16))
        self.label_4 = QLabel(self.border_group_box)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(210, 80, 49, 16))
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.bitrate_label = QLabel(self.border_group_box)
        self.bitrate_label.setObjectName(u"bitrate_label")
        self.bitrate_label.setGeometry(QRect(70, 110, 141, 16))
        self.label_7 = QLabel(self.border_group_box)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(210, 110, 49, 16))
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_3 = QLabel(self.border_group_box)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 80, 49, 16))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_5 = QLabel(self.border_group_box)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(210, 50, 49, 16))
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.fps_label = QLabel(self.border_group_box)
        self.fps_label.setObjectName(u"fps_label")
        self.fps_label.setGeometry(QRect(70, 80, 141, 16))
        self.speed_label = QLabel(self.border_group_box)
        self.speed_label.setObjectName(u"speed_label")
        self.speed_label.setGeometry(QRect(270, 110, 101, 16))
        self.label = QLabel(self.border_group_box)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 49, 16))
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.abort_button = QPushButton(self.border_group_box)
        self.abort_button.setObjectName(u"abort_button")
        self.abort_button.setGeometry(QRect(150, 170, 81, 24))
        self.label_6 = QLabel(self.border_group_box)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 110, 49, 16))
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.time_label = QLabel(self.border_group_box)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setGeometry(QRect(270, 50, 101, 16))
        self.progress_bar = QProgressBar(self.border_group_box)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setGeometry(QRect(10, 140, 361, 23))
        self.progress_bar.setValue(24)
        self.progress_bar.setTextVisible(True)
        self.size_label = QLabel(self.border_group_box)
        self.size_label.setObjectName(u"size_label")
        self.size_label.setGeometry(QRect(270, 80, 101, 16))
        self.label_2 = QLabel(self.border_group_box)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 50, 49, 16))
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.retranslateUi(ProgressDialog)

        QMetaObject.connectSlotsByName(ProgressDialog)
    # setupUi

    def retranslateUi(self, ProgressDialog):
        ProgressDialog.setWindowTitle(QCoreApplication.translate("ProgressDialog", u"Slicing Progress", None))
        self.border_group_box.setTitle("")
        self.status_label.setText("")
        self.frame_label.setText("")
        self.label_4.setText(QCoreApplication.translate("ProgressDialog", u"Size:", None))
        self.bitrate_label.setText("")
        self.label_7.setText(QCoreApplication.translate("ProgressDialog", u"Speed:", None))
        self.label_3.setText(QCoreApplication.translate("ProgressDialog", u"FPS:", None))
        self.label_5.setText(QCoreApplication.translate("ProgressDialog", u"Time:", None))
        self.fps_label.setText("")
        self.speed_label.setText("")
        self.label.setText(QCoreApplication.translate("ProgressDialog", u"Status:", None))
        self.abort_button.setText(QCoreApplication.translate("ProgressDialog", u"Abort", None))
        self.label_6.setText(QCoreApplication.translate("ProgressDialog", u"Bit Rate:", None))
        self.time_label.setText("")
        self.size_label.setText("")
        self.label_2.setText(QCoreApplication.translate("ProgressDialog", u"Frame:", None))
    # retranslateUi



