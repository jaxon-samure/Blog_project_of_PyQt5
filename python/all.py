import sys
from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QTextEdit, QWidget, QVBoxLayout

class ListWidgetWithTextArea(QListWidget):
    def __init__(self):
        super().__init__()


    def addTextAreaItem(self, text: str, oyna: QWidget):        
        layout = QVBoxLayout()
        
        text_edit = QTextEdit()
        text_edit.setText(text)
        text_edit.setEnabled(False)
        
        layout.addWidget(text_edit)
        
        oyna.setLayout(layout)
        
        item = QListWidgetItem()
        item.setSizeHint(oyna.sizeHint())
        
        self.addItem(item)
        self.setItemWidget(item, oyna)
        
