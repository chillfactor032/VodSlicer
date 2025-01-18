# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QListView, QMainWindow, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 460)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 460))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.vod_explorer_box = QGroupBox(self.centralwidget)
        self.vod_explorer_box.setObjectName(u"vod_explorer_box")
        self.vod_explorer_box.setMinimumSize(QSize(476, 419))
        self.gridLayout_3 = QGridLayout(self.vod_explorer_box)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
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

        self.gridLayout_2.addWidget(self.vod_list_view, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(self.vod_explorer_box)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.vod_url_edit = QLineEdit(self.vod_explorer_box)
        self.vod_url_edit.setObjectName(u"vod_url_edit")

        self.horizontalLayout.addWidget(self.vod_url_edit)

        self.save_button = QPushButton(self.vod_explorer_box)
        self.save_button.setObjectName(u"save_button")

        self.horizontalLayout.addWidget(self.save_button)

        self.open_file_button = QPushButton(self.vod_explorer_box)
        self.open_file_button.setObjectName(u"open_file_button")

        self.horizontalLayout.addWidget(self.open_file_button)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_2)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)


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
        self.user_edit.setGeometry(QRect(110, 30, 171, 22))
        self.label_4 = QLabel(self.groupBox_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 30, 71, 21))
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.password_edit = QLineEdit(self.groupBox_3)
        self.password_edit.setObjectName(u"password_edit")
        self.password_edit.setGeometry(QRect(110, 60, 171, 22))
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 60, 71, 21))
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 110, 261, 20))
        self.github_button = QPushButton(self.groupBox_3)
        self.github_button.setObjectName(u"github_button")
        self.github_button.setGeometry(QRect(210, 150, 75, 24))
        self.about_button = QPushButton(self.groupBox_3)
        self.about_button.setObjectName(u"about_button")
        self.about_button.setGeometry(QRect(20, 150, 101, 24))
        self.line = QFrame(self.groupBox_3)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(20, 90, 261, 16))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.groupBox_3, 0, 1, 1, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(300, 200))
        self.verticalLayoutWidget_2 = QWidget(self.groupBox_2)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(9, 19, 281, 211))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 10, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.startTimeLabel = QLabel(self.verticalLayoutWidget_2)
        self.startTimeLabel.setObjectName(u"startTimeLabel")
        font1 = QFont()
        font1.setPointSize(18)
        self.startTimeLabel.setFont(font1)
        self.startTimeLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.startTimeLabel)

        self.start_time_edit = QLineEdit(self.verticalLayoutWidget_2)
        self.start_time_edit.setObjectName(u"start_time_edit")
        self.start_time_edit.setFont(font1)
        self.start_time_edit.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.start_time_edit)

        self.endTimeLabel = QLabel(self.verticalLayoutWidget_2)
        self.endTimeLabel.setObjectName(u"endTimeLabel")
        self.endTimeLabel.setFont(font1)
        self.endTimeLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.endTimeLabel)

        self.end_time_edit = QLineEdit(self.verticalLayoutWidget_2)
        self.end_time_edit.setObjectName(u"end_time_edit")
        self.end_time_edit.setFont(font1)
        self.end_time_edit.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.end_time_edit)

        self.clipNameLabel = QLabel(self.verticalLayoutWidget_2)
        self.clipNameLabel.setObjectName(u"clipNameLabel")
        self.clipNameLabel.setFont(font1)
        self.clipNameLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.clipNameLabel)

        self.clip_name_edit = QLineEdit(self.verticalLayoutWidget_2)
        self.clip_name_edit.setObjectName(u"clip_name_edit")
        self.clip_name_edit.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.clip_name_edit)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.slice_button = QPushButton(self.verticalLayoutWidget_2)
        self.slice_button.setObjectName(u"slice_button")
        self.slice_button.setMinimumSize(QSize(0, 40))

        self.verticalLayout_2.addWidget(self.slice_button)


        self.gridLayout.addWidget(self.groupBox_2, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.status_bar = QStatusBar(MainWindow)
        self.status_bar.setObjectName(u"status_bar")
        MainWindow.setStatusBar(self.status_bar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.vod_explorer_box.setTitle(QCoreApplication.translate("MainWindow", u"VoD Explorer", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"URL:", None))
        self.save_button.setText("")
        self.open_file_button.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.user_edit.setInputMask("")
        self.user_edit.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"User Name:", None))
        self.password_edit.setInputMask("")
        self.password_edit.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Password:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Check GitHub for updated releases", None))
        self.github_button.setText(QCoreApplication.translate("MainWindow", u"View Github", None))
        self.about_button.setText(QCoreApplication.translate("MainWindow", u"About VodSlicer", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Slicer", None))
        self.startTimeLabel.setText(QCoreApplication.translate("MainWindow", u"Start Time:", None))
        self.start_time_edit.setInputMask(QCoreApplication.translate("MainWindow", u"99:99:99", None))
        self.start_time_edit.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.endTimeLabel.setText(QCoreApplication.translate("MainWindow", u"End Time:", None))
        self.end_time_edit.setInputMask(QCoreApplication.translate("MainWindow", u"99:99:99", None))
        self.end_time_edit.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.clipNameLabel.setText(QCoreApplication.translate("MainWindow", u"Clip Name:", None))
        self.slice_button.setText(QCoreApplication.translate("MainWindow", u"Slice!", None))
    # retranslateUi



# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MarkersDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MarkersDialog(object):
    def setupUi(self, MarkersDialog):
        if not MarkersDialog.objectName():
            MarkersDialog.setObjectName(u"MarkersDialog")
        MarkersDialog.resize(544, 467)
        self.marker_count_label = QLabel(MarkersDialog)
        self.marker_count_label.setObjectName(u"marker_count_label")
        self.marker_count_label.setGeometry(QRect(300, 430, 61, 31))
        font = QFont()
        font.setPointSize(12)
        self.marker_count_label.setFont(font)
        self.label = QLabel(MarkersDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 430, 161, 31))
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_3 = QLabel(MarkersDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 10, 111, 31))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.clip_before_edit = QLineEdit(MarkersDialog)
        self.clip_before_edit.setObjectName(u"clip_before_edit")
        self.clip_before_edit.setGeometry(QRect(120, 10, 61, 31))
        self.clip_before_edit.setFont(font)
        self.clip_before_edit.setCursorPosition(4)
        self.label_4 = QLabel(MarkersDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(270, 10, 161, 31))
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.clip_after_edit = QLineEdit(MarkersDialog)
        self.clip_after_edit.setObjectName(u"clip_after_edit")
        self.clip_after_edit.setGeometry(QRect(440, 10, 61, 31))
        self.clip_after_edit.setFont(font)
        self.clip_after_edit.setMaxLength(5)
        self.clip_after_edit.setCursorPosition(4)
        self.marker_table = QTableWidget(MarkersDialog)
        if (self.marker_table.columnCount() < 4):
            self.marker_table.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.marker_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.marker_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.marker_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.marker_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.marker_table.setObjectName(u"marker_table")
        self.marker_table.setGeometry(QRect(10, 50, 521, 371))
        self.marker_table.setAlternatingRowColors(False)
        self.marker_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.marker_table.setWordWrap(False)
        self.marker_table.setCornerButtonEnabled(False)
        self.marker_table.horizontalHeader().setMinimumSectionSize(50)
        self.marker_table.horizontalHeader().setDefaultSectionSize(107)
        self.create_button = QPushButton(MarkersDialog)
        self.create_button.setObjectName(u"create_button")
        self.create_button.setGeometry(QRect(430, 430, 101, 30))
        self.cancel_button = QPushButton(MarkersDialog)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setGeometry(QRect(10, 430, 101, 30))

        self.retranslateUi(MarkersDialog)

        QMetaObject.connectSlotsByName(MarkersDialog)
    # setupUi

    def retranslateUi(self, MarkersDialog):
        MarkersDialog.setWindowTitle(QCoreApplication.translate("MarkersDialog", u"Stream Markers", None))
        self.marker_count_label.setText(QCoreApplication.translate("MarkersDialog", u"9999", None))
        self.label.setText(QCoreApplication.translate("MarkersDialog", u"Markers Imported:", None))
        self.label_3.setText(QCoreApplication.translate("MarkersDialog", u"Clip Before:", None))
        self.clip_before_edit.setInputMask(QCoreApplication.translate("MarkersDialog", u"99:99", None))
        self.clip_before_edit.setText(QCoreApplication.translate("MarkersDialog", u"00:30", None))
        self.label_4.setText(QCoreApplication.translate("MarkersDialog", u"Clip After:", None))
        self.clip_after_edit.setInputMask(QCoreApplication.translate("MarkersDialog", u"99:99", None))
        self.clip_after_edit.setText(QCoreApplication.translate("MarkersDialog", u"00:30", None))
        ___qtablewidgetitem = self.marker_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MarkersDialog", u"Clip Name", None));
        ___qtablewidgetitem1 = self.marker_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MarkersDialog", u"Time", None));
        ___qtablewidgetitem2 = self.marker_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MarkersDialog", u"Role", None));
        ___qtablewidgetitem3 = self.marker_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MarkersDialog", u"Creator", None));
        self.create_button.setText(QCoreApplication.translate("MarkersDialog", u"Create Clips", None))
        self.cancel_button.setText(QCoreApplication.translate("MarkersDialog", u"Cancel", None))
    # retranslateUi



# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OpenDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QGridLayout,
    QLabel, QLineEdit, QListView, QPushButton,
    QSizePolicy, QToolButton, QWidget)
import Resources_rc

class Ui_OpenDialog(object):
    def setupUi(self, OpenDialog):
        if not OpenDialog.objectName():
            OpenDialog.setObjectName(u"OpenDialog")
        OpenDialog.resize(482, 421)
        self.label = QLabel(OpenDialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, 41, 20))
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.url_edit = QLineEdit(OpenDialog)
        self.url_edit.setObjectName(u"url_edit")
        self.url_edit.setGeometry(QRect(50, 10, 291, 20))
        self.refresh_button = QToolButton(OpenDialog)
        self.refresh_button.setObjectName(u"refresh_button")
        self.refresh_button.setGeometry(QRect(350, 15, 40, 40))
        icon = QIcon()
        icon.addFile(u":/resources/img/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.refresh_button.setIcon(icon)
        self.refresh_button.setIconSize(QSize(24, 24))
        self.open_button = QPushButton(OpenDialog)
        self.open_button.setObjectName(u"open_button")
        self.open_button.setGeometry(QRect(400, 15, 71, 40))
        self.label_2 = QLabel(OpenDialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 40, 41, 21))
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_3 = QLabel(OpenDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(160, 40, 61, 21))
        self.user_edit = QLineEdit(OpenDialog)
        self.user_edit.setObjectName(u"user_edit")
        self.user_edit.setGeometry(QRect(50, 40, 101, 20))
        self.password_edit = QLineEdit(OpenDialog)
        self.password_edit.setObjectName(u"password_edit")
        self.password_edit.setGeometry(QRect(220, 40, 121, 20))
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.main_widget = QWidget(OpenDialog)
        self.main_widget.setObjectName(u"main_widget")
        self.main_widget.setGeometry(QRect(10, 70, 461, 341))
        self.gridLayout = QGridLayout(self.main_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.vod_list_view = QListView(self.main_widget)
        self.vod_list_view.setObjectName(u"vod_list_view")
        self.vod_list_view.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.gridLayout.addWidget(self.vod_list_view, 0, 0, 1, 1)


        self.retranslateUi(OpenDialog)

        QMetaObject.connectSlotsByName(OpenDialog)
    # setupUi

    def retranslateUi(self, OpenDialog):
        OpenDialog.setWindowTitle(QCoreApplication.translate("OpenDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("OpenDialog", u"URL:", None))
        self.refresh_button.setText(QCoreApplication.translate("OpenDialog", u"...", None))
        self.open_button.setText(QCoreApplication.translate("OpenDialog", u"Open", None))
        self.label_2.setText(QCoreApplication.translate("OpenDialog", u"User:", None))
        self.label_3.setText(QCoreApplication.translate("OpenDialog", u"Password:", None))
    # retranslateUi



# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Progress.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
        self.label_8 = QLabel(self.border_group_box)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 170, 49, 31))
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.clip_count_label = QLabel(self.border_group_box)
        self.clip_count_label.setObjectName(u"clip_count_label")
        self.clip_count_label.setGeometry(QRect(70, 170, 71, 31))

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
        self.label_8.setText(QCoreApplication.translate("ProgressDialog", u"Clip:", None))
        self.clip_count_label.setText(QCoreApplication.translate("ProgressDialog", u"0 / 0", None))
    # retranslateUi



# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Settings.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.resize(473, 176)
        self.groupBox = QGroupBox(SettingsDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 451, 121))
        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(90, 20, 351, 20))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 61, 21))
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(90, 50, 161, 20))
        self.lineEdit_3 = QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(90, 80, 161, 20))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 50, 61, 21))
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 80, 61, 21))
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.pushButton = QPushButton(SettingsDialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(380, 140, 75, 23))

        self.retranslateUi(SettingsDialog)

        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("SettingsDialog", u"Default Web Vod Location", None))
        self.label.setText(QCoreApplication.translate("SettingsDialog", u"URL:", None))
        self.label_2.setText(QCoreApplication.translate("SettingsDialog", u"Username:", None))
        self.label_3.setText(QCoreApplication.translate("SettingsDialog", u"Password:", None))
        self.pushButton.setText(QCoreApplication.translate("SettingsDialog", u"Save", None))
    # retranslateUi



# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VodSlicer.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenuBar,
    QSizePolicy, QSlider, QSpacerItem, QStackedWidget,
    QStatusBar, QToolButton, QVBoxLayout, QWidget)
import Resources_rc
import Resources_rc

class Ui_VodSlicer(object):
    def setupUi(self, VodSlicer):
        if not VodSlicer.objectName():
            VodSlicer.setObjectName(u"VodSlicer")
        VodSlicer.resize(865, 641)
        self.centralwidget = QWidget(VodSlicer)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(865, 600))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.video_player_stacked_widget = QStackedWidget(self.widget)
        self.video_player_stacked_widget.setObjectName(u"video_player_stacked_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.video_player_stacked_widget.sizePolicy().hasHeightForWidth())
        self.video_player_stacked_widget.setSizePolicy(sizePolicy1)
        self.video_player_stacked_widget.setStyleSheet(u"")
        self.video_player_widget = QWidget()
        self.video_player_widget.setObjectName(u"video_player_widget")
        self.video_player_widget.setStyleSheet(u"background-color:black;")
        self.gridLayout = QGridLayout(self.video_player_widget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.video_player_stacked_widget.addWidget(self.video_player_widget)
        self.loading_page = QWidget()
        self.loading_page.setObjectName(u"loading_page")
        self.loading_page.setStyleSheet(u"background-color: black")
        self.gridLayout_2 = QGridLayout(self.loading_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.loading_label = QLabel(self.loading_page)
        self.loading_label.setObjectName(u"loading_label")
        self.loading_label.setPixmap(QPixmap(u":/resources/img/loading.gif"))
        self.loading_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.loading_label, 0, 0, 1, 1)

        self.video_player_stacked_widget.addWidget(self.loading_page)
        self.no_media_page = QWidget()
        self.no_media_page.setObjectName(u"no_media_page")
        self.no_media_page.setStyleSheet(u"background-color:black")
        self.gridLayout_3 = QGridLayout(self.no_media_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_4 = QLabel(self.no_media_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u":/resources/img/vod_slicer.ico"))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)

        self.no_media_label = QLabel(self.no_media_page)
        self.no_media_label.setObjectName(u"no_media_label")
        font = QFont()
        font.setPointSize(20)
        self.no_media_label.setFont(font)
        self.no_media_label.setLayoutDirection(Qt.LeftToRight)
        self.no_media_label.setStyleSheet(u"color: white")
        self.no_media_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.no_media_label, 2, 0, 1, 1)

        self.label_5 = QLabel(self.no_media_page)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)

        self.video_player_stacked_widget.addWidget(self.no_media_page)

        self.verticalLayout_5.addWidget(self.video_player_stacked_widget)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy2)
        self.widget_4.setMinimumSize(QSize(0, 100))
        self.verticalLayout_4 = QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.video_slider = QSlider(self.widget_4)
        self.video_slider.setObjectName(u"video_slider")
        self.video_slider.setMaximum(9999)
        self.video_slider.setPageStep(100)
        self.video_slider.setOrientation(Qt.Horizontal)
        self.video_slider.setTickPosition(QSlider.TicksAbove)
        self.video_slider.setTickInterval(500)

        self.verticalLayout_4.addWidget(self.video_slider)

        self.widget_7 = QWidget(self.widget_4)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_14 = QWidget(self.widget_7)
        self.widget_14.setObjectName(u"widget_14")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_14.sizePolicy().hasHeightForWidth())
        self.widget_14.setSizePolicy(sizePolicy3)
        self.widget_14.setMinimumSize(QSize(200, 115))
        self.widget_14.setMaximumSize(QSize(200, 115))
        self.verticalLayout_2 = QVBoxLayout(self.widget_14)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_12 = QWidget(self.widget_14)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.clip_start_button = QToolButton(self.widget_12)
        self.clip_start_button.setObjectName(u"clip_start_button")
        self.clip_start_button.setMinimumSize(QSize(77, 30))
        icon = QIcon()
        icon.addFile(u":/resources/img/flag.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.clip_start_button.setIcon(icon)
        self.clip_start_button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_8.addWidget(self.clip_start_button)

        self.clip_start_edit = QLineEdit(self.widget_12)
        self.clip_start_edit.setObjectName(u"clip_start_edit")
        font1 = QFont()
        font1.setPointSize(15)
        self.clip_start_edit.setFont(font1)

        self.horizontalLayout_8.addWidget(self.clip_start_edit)


        self.verticalLayout_2.addWidget(self.widget_12)

        self.widget_13 = QWidget(self.widget_14)
        self.widget_13.setObjectName(u"widget_13")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_13)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.clip_end_button = QToolButton(self.widget_13)
        self.clip_end_button.setObjectName(u"clip_end_button")
        self.clip_end_button.setMinimumSize(QSize(77, 30))
        self.clip_end_button.setIcon(icon)
        self.clip_end_button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.horizontalLayout_9.addWidget(self.clip_end_button)

        self.clip_end_edit = QLineEdit(self.widget_13)
        self.clip_end_edit.setObjectName(u"clip_end_edit")
        self.clip_end_edit.setFont(font1)

        self.horizontalLayout_9.addWidget(self.clip_end_edit)


        self.verticalLayout_2.addWidget(self.widget_13)

        self.widget_2 = QWidget(self.widget_14)
        self.widget_2.setObjectName(u"widget_2")
        self.gridLayout_5 = QGridLayout(self.widget_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.about_button = QToolButton(self.widget_2)
        self.about_button.setObjectName(u"about_button")
        icon1 = QIcon()
        icon1.addFile(u":/resources/img/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.about_button.setIcon(icon1)
        self.about_button.setIconSize(QSize(24, 24))

        self.gridLayout_5.addWidget(self.about_button, 0, 2, 1, 1)

        self.save_clip_button = QToolButton(self.widget_2)
        self.save_clip_button.setObjectName(u"save_clip_button")
        self.save_clip_button.setMinimumSize(QSize(0, 30))
        icon2 = QIcon()
        icon2.addFile(u":/resources/img/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.save_clip_button.setIcon(icon2)
        self.save_clip_button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.gridLayout_5.addWidget(self.save_clip_button, 0, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_3, 0, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.widget_2)


        self.horizontalLayout_3.addWidget(self.widget_14)

        self.horizontalSpacer = QSpacerItem(109, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.widget_11 = QWidget(self.widget_7)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(280, 115))
        self.widget_11.setMaximumSize(QSize(200, 115))
        self.verticalLayout = QVBoxLayout(self.widget_11)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.video_controls_widget = QWidget(self.widget_11)
        self.video_controls_widget.setObjectName(u"video_controls_widget")
        self.video_controls_layout = QHBoxLayout(self.video_controls_widget)
        self.video_controls_layout.setObjectName(u"video_controls_layout")
        self.video_controls_layout.setContentsMargins(0, 0, 0, 14)
        self.play_button = QToolButton(self.video_controls_widget)
        self.play_button.setObjectName(u"play_button")
        self.play_button.setMinimumSize(QSize(50, 35))
        self.play_button.setMaximumSize(QSize(50, 35))
        icon3 = QIcon()
        icon3.addFile(u":/resources/img/play.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.play_button.setIcon(icon3)
        self.play_button.setIconSize(QSize(24, 24))

        self.video_controls_layout.addWidget(self.play_button)


        self.verticalLayout.addWidget(self.video_controls_widget)

        self.cur_time_label = QLabel(self.widget_11)
        self.cur_time_label.setObjectName(u"cur_time_label")
        self.cur_time_label.setFont(font)
        self.cur_time_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.cur_time_label)


        self.horizontalLayout_3.addWidget(self.widget_11)

        self.horizontalSpacer_2 = QSpacerItem(108, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.widget_6 = QWidget(self.widget_7)
        self.widget_6.setObjectName(u"widget_6")
        sizePolicy3.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy3)
        self.widget_6.setMinimumSize(QSize(200, 115))
        self.widget_6.setMaximumSize(QSize(200, 115))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.widget_6)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy3.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy3)
        self.widget_5.setMinimumSize(QSize(0, 115))
        self.widget_5.setMaximumSize(QSize(16777215, 115))
        self.verticalLayout_3 = QVBoxLayout(self.widget_5)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 3, -1, -1)
        self.online_video_button = QToolButton(self.widget_5)
        self.online_video_button.setObjectName(u"online_video_button")
        sizePolicy3.setHeightForWidth(self.online_video_button.sizePolicy().hasHeightForWidth())
        self.online_video_button.setSizePolicy(sizePolicy3)
        self.online_video_button.setMinimumSize(QSize(120, 30))
        self.online_video_button.setMaximumSize(QSize(120, 30))
        icon4 = QIcon()
        icon4.addFile(u":/resources/img/download.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.online_video_button.setIcon(icon4)
        self.online_video_button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_3.addWidget(self.online_video_button)

        self.local_video_button = QToolButton(self.widget_5)
        self.local_video_button.setObjectName(u"local_video_button")
        sizePolicy3.setHeightForWidth(self.local_video_button.sizePolicy().hasHeightForWidth())
        self.local_video_button.setSizePolicy(sizePolicy3)
        self.local_video_button.setMinimumSize(QSize(120, 30))
        self.local_video_button.setIcon(icon4)
        self.local_video_button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_3.addWidget(self.local_video_button)

        self.markers_button = QToolButton(self.widget_5)
        self.markers_button.setObjectName(u"markers_button")
        sizePolicy3.setHeightForWidth(self.markers_button.sizePolicy().hasHeightForWidth())
        self.markers_button.setSizePolicy(sizePolicy3)
        self.markers_button.setMinimumSize(QSize(120, 30))
        self.markers_button.setMaximumSize(QSize(120, 30))
        icon5 = QIcon()
        icon5.addFile(u":/resources/img/twitch.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.markers_button.setIcon(icon5)
        self.markers_button.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.verticalLayout_3.addWidget(self.markers_button)


        self.horizontalLayout_2.addWidget(self.widget_5)

        self.widget_3 = QWidget(self.widget_6)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy4)
        self.widget_3.setMinimumSize(QSize(30, 115))
        self.widget_3.setMaximumSize(QSize(30, 115))
        self.verticalLayout_6 = QVBoxLayout(self.widget_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.volume_slider = QSlider(self.widget_3)
        self.volume_slider.setObjectName(u"volume_slider")
        self.volume_slider.setMinimumSize(QSize(20, 0))
        self.volume_slider.setValue(50)
        self.volume_slider.setOrientation(Qt.Vertical)
        self.volume_slider.setTickPosition(QSlider.NoTicks)

        self.verticalLayout_6.addWidget(self.volume_slider)

        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy5)
        self.label.setMinimumSize(QSize(20, 0))
        self.label.setPixmap(QPixmap(u":/resources/img/volume.svg"))

        self.verticalLayout_6.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.widget_3)


        self.horizontalLayout_3.addWidget(self.widget_6)


        self.verticalLayout_4.addWidget(self.widget_7)


        self.verticalLayout_5.addWidget(self.widget_4)


        self.horizontalLayout.addWidget(self.widget)

        VodSlicer.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(VodSlicer)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 865, 21))
        VodSlicer.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(VodSlicer)
        self.statusbar.setObjectName(u"statusbar")
        VodSlicer.setStatusBar(self.statusbar)

        self.retranslateUi(VodSlicer)

        self.video_player_stacked_widget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(VodSlicer)
    # setupUi

    def retranslateUi(self, VodSlicer):
        VodSlicer.setWindowTitle(QCoreApplication.translate("VodSlicer", u"MainWindow", None))
        self.loading_label.setText("")
        self.label_4.setText("")
        self.no_media_label.setText(QCoreApplication.translate("VodSlicer", u"No Media Loaded", None))
        self.label_5.setText("")
        self.clip_start_button.setText(QCoreApplication.translate("VodSlicer", u"Clip Start", None))
        self.clip_start_edit.setInputMask(QCoreApplication.translate("VodSlicer", u"99:99:99", None))
        self.clip_start_edit.setText(QCoreApplication.translate("VodSlicer", u"00:00:00", None))
        self.clip_start_edit.setPlaceholderText(QCoreApplication.translate("VodSlicer", u"00:00:00", None))
        self.clip_end_button.setText(QCoreApplication.translate("VodSlicer", u"Clip End", None))
        self.clip_end_edit.setInputMask(QCoreApplication.translate("VodSlicer", u"99:99:99", None))
        self.clip_end_edit.setText(QCoreApplication.translate("VodSlicer", u"00:00:00", None))
        self.clip_end_edit.setPlaceholderText(QCoreApplication.translate("VodSlicer", u"00:00:00", None))
        self.about_button.setText(QCoreApplication.translate("VodSlicer", u"About", None))
        self.save_clip_button.setText(QCoreApplication.translate("VodSlicer", u"Save Clip", None))
        self.play_button.setText(QCoreApplication.translate("VodSlicer", u"...", None))
        self.cur_time_label.setText(QCoreApplication.translate("VodSlicer", u"00:00:00.000", None))
        self.online_video_button.setText(QCoreApplication.translate("VodSlicer", u"Online Video", None))
        self.local_video_button.setText(QCoreApplication.translate("VodSlicer", u"Local Video", None))
        self.markers_button.setText(QCoreApplication.translate("VodSlicer", u"Stream Markers", None))
        self.label.setText("")
    # retranslateUi



