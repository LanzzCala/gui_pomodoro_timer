import sys
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout

# Have QMainWindow be subclass to customize the window
class PomodoroWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("🍅Your Pomodoro Timer! 🍅")
        #Establish starting click amount
        self.clicks = 0
        self.button = QPushButton("Pomodoro Time 🍅", self)
        self.button.setFixedSize(180, 120)
        self.button.clicked.connect(self.pomodoro_button_clicked)

    
        self.setMinimumSize(QSize(400, 200))
        self.setMaximumSize(QSize(900, 600))
        layout = QVBoxLayout()
        layout.addWidget(self.button)

    #Connect to parent and count each click of button
    def pomodoro_button_clicked(self):
        self.clicks += 1
        self.button.setText(f"Pomodoros Clicked 🍅: {self.clicks}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PomodoroWindow()
    window.show()
    sys.exit(app.exec())