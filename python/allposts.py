from PyQt5.QtWidgets import QWidget
from components import Button, TextArea


class AllPostsPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(450, 600)
        self.setWindowTitle("My Post Page")


        self.writePostBtn = Button("Post yozish", self, 0)
        self.myPostsBtn = Button("Mening postlarim", self, 0)

        self.writePostBtn.move(20, 50)
        self.myPostsBtn.move(210, 50)