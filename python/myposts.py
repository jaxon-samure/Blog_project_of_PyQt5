from PyQt5.QtWidgets import QWidget
from components import Button, Input, Label, TextArea


class MyPostsPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setFixedSize(450, 600)
        self.setWindowTitle("My Post Page")

        self.label = Label("Mening postlarim", self, 30)        
        
        
        