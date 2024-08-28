from PyQt5.QtWidgets import QWidget
from components import Button, Input


class LoginPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(400, 600)
        self.setWindowTitle("Login Page")

        self.usernameInput = Input(self, 100, "Username kiriting...")
        self.passwordInput = Input(self, 170, "Password kiriting...")

        self.loginBtn = Button("Kirish", self, 270)