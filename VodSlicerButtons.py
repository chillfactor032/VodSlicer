import time

# PySide6 Imports
from PySide6.QtWidgets import QToolButton, QToolTip
from PySide6.QtCore import Signal, QObject, Qt, QTimer
from PySide6.QtGui import QMouseEvent

class CustomButton(QToolButton):

    class Signals(QObject):
        rightclicked = Signal()
        leftclicked = Signal()
        longclickup = Signal()
        longclickdown = Signal()

    def __init__(self, *args, **kwargs):
        super(CustomButton, self).__init__(*args, **kwargs)
        self.signals = CustomButton.Signals()
        self.hold_threshold_secs = 0
        self.mouse_down_time = 0
        self.mouse_down_timer = QTimer()
        self.mouse_down_timer.timeout.connect(self.monitor_longclick)

    def setHoldThreshold(self, threshold=0):
        self.hold_threshold_secs = threshold

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.mouse_down_time = time.time()
        if QMouseEvent.button(event) == Qt.RightButton:
            self.signals.rightclicked.emit()
        if QMouseEvent.button(event) == Qt.LeftButton:
            if self.hold_threshold_secs == 0 :
                self.signals.leftclicked.emit()
            else:
                self.mouse_down_timer.start(100)
        return super().mousePressEvent(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        if self.hold_threshold_secs == 0: return
        hold_time = time.time() - self.mouse_down_time
        if hold_time >= self.hold_threshold_secs:
            self.signals.longclickup.emit()
        else:
            if QMouseEvent.button(event) == Qt.LeftButton:
                self.signals.leftclicked.emit()
        self.mouse_down_time = 0
        self.mouse_down_timer.stop()
        return super().mouseReleaseEvent(event)
    
    def monitor_longclick(self):
        hold_time = time.time() - self.mouse_down_time
        if hold_time >= self.hold_threshold_secs:
            self.signals.longclickdown.emit()
            self.mouse_down_timer.stop()
