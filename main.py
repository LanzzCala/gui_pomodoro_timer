import sys
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

# Have QMainWindow be subclass to customize the window
class PomodoroWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("🍅Your Pomodoro Timer! 🍅")

        self.setMinimumSize(QSize(400, 200))
        self.setMaximumSize(QSize(900, 600))


application = QApplication(sys.argv)

window = PomodoroWindow()
window.show()
application.exec()