from PyQt5.QtGui import QPainter, QColor, QBrush, QPen
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer
from audio_process import Audio


class CircleWidget(QWidget):
    def __init__(self, index, parent=None):
        super(CircleWidget, self).__init__(parent)
        self.setMinimumSize(300, 350)

        self.audio = Audio(index)
        self.audio.start()

        self.circle_size = 50
        self.target_size = 50

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_circle_size)
        self.timer.start(10)

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        color = QColor(0, 0, 0)
        painter.setBrush(QBrush(color))
        painter.setPen(QPen(Qt.NoPen))

        size = int(self.circle_size)
        x = int((self.width() - size) // 2)
        y = int((self.height() - size) // 2)

        painter.drawEllipse(x, y, size, size)
        painter.end()

    def update_circle_size(self):
        audio_level = self.audio.get_audio_level()
        self.target_size = int(50 + (audio_level / 3000) * (self.width() - 50)) if audio_level > 0 else 50
        self.circle_size += (self.target_size - self.circle_size) * 0.2
        self.circle_size = max(50, min(self.circle_size, self.width() - 20))

        self.update()

    def stop(self):
        self.timer.stop()
        self.audio.stop()
