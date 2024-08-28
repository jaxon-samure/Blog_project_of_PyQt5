from PyQt5.QtWidgets import QWidget
from components import Button, Input


class RegisterPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(400, 500)
        self.setWindowTitle("Register Page")

        self.nameInput = Input(self, 100, "Ismingizni kiriting: ")
        self.surnameInput = Input(self, 170, "Familiyangizni kiriting: ")
        self.usernameInput = Input(self, 240, "Usernameingizni kiriting: ")
        self.passwordInput = Input(self, 310, "Passwordingizni kiriting: ")

        self.registerBtn = Button("Registration", self, 400)