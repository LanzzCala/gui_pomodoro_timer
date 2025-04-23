import sys
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton

# Have QMainWindow be subclass to customize the window
class PomodoroWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("🍅Your Pomodoro Timer! 🍅")

        self.number_times_clicked = 0

        self.button = QPushButton("Pomodoro Time 🍅")
        self.button.clicked.connect(self.pomodoro_button_clicked)
        self.setCentralWidget(self.button)

        

        self.setMinimumSize(QSize(400, 200))
        self.setMaximumSize(QSize(900, 600))

    def pomodoro_button_clicked(self):
        count = self.number_times_clicked
        new_count = count + 1
        print(f"Number of clicks: {new_count}")


application = QApplication(sys.argv)

window = PomodoroWindow()
window.show()
application.exec()