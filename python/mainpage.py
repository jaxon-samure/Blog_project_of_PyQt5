from PyQt5.QtWidgets import QWidget, QLabel, QPushButton
from components import Button, Input

class MainPage(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedSize(400, 500)
        self.setWindowTitle("Bosh sahifa")

        self.label = QLabel("Bosh sahifa", self)
        self.label.setStyleSheet("font-size: 26px;")
        self.label.adjustSize()
        self.label.move((self.width() - self.label.width()) // 2, 100)

        self.loginBtn = Button("Tizimga kirish", self, 200)
        self.registerBtn = Button("Ro'yxatdan o'tish", self, 270)

        self.loginBtn.changeSize()
        self.registerBtn.changeSize()