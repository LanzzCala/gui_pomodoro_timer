import sys
from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget

# Have QMainWindow be subclass to customize the window
class PomodoroWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("🍅Your Pomodoro Timer! 🍅")
        #Establish starting click amount
        self.clicks = 0
        self.pomodoro_button = QPushButton("Pomodoro Time 🍅", self)
        self.pomodoro_button.clicked.connect(self.pomodoro_button_clicked)

        self.short_break_button = QPushButton("Short Break 😪", self)

    
        self.setMinimumSize(QSize(400, 200))
        self.setMaximumSize(QSize(900, 600))
        layout = QHBoxLayout()
        layout.addWidget(self.pomodoro_button)
        layout.addWidget(self.short_break_button)

        # Dummy widget to use CentralWidget and setLayout
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    #Connect to parent and count each click of button
    def pomodoro_button_clicked(self):
        self.clicks += 1
        self.pomodoro_button.setText(f"Pomodoros Clicked 🍅: {self.clicks}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PomodoroWindow()
    window.show()
    sys.exit(app.exec())