from PyQt5.QtWidgets import QLabel, QPushButton, QWidget, QApplication,QLineEdit, QMessageBox
from os import system
from db import createTable, insert
system("clear")


class DB_UI(QWidget):
    def __init__(self) -> None:
        super().__init__()
        createTable()
        
        self.setWindowTitle("DB_Manager")
        self.resize(400,500)
        
        label_ID = QLabel("ID", self)
        label_ID.setGeometry(40, 80, 100, 20)
        
        label_DoriName = QLabel("Dori nomi", self)
        label_DoriName.setGeometry(170, 80, 100, 20)
        
        label_DoriName = QLabel("price", self)
        label_DoriName.setGeometry(320, 80, 100, 20)
        
        self.line_ID = QLineEdit(self)
        self.line_ID.setGeometry(10, 100, 100, 30)
        
        self.line_DoriName = QLineEdit( self)
        self.line_DoriName.setGeometry(150, 100, 100, 30)
        
        self.line_pirce = QLineEdit( self)
        self.line_pirce.setGeometry(300, 100, 100, 30)
        
        
        btn = QPushButton("Submit", self)
        btn.setGeometry(160, 200, 40, 50)
        btn.adjustSize()
        
        
        btn.clicked.connect(self.bosdi)
        
        self.show()
    
    def bosdi(self):
        id_text = self.line_ID.text().strip()
        line_doriname_text = self.line_DoriName.text().strip()
        line_price_text = self.line_pirce.text().strip()
        
        if id_text and line_doriname_text and line_price_text:
            insert(id_text, line_doriname_text, line_price_text)
        else:
            self.isEmpty()
        
        
    def isEmpty(self):
        
        msg =  QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Iltimos barcha maydonlarni to'ldiring!")
        msg.setWindowTitle("Xatolik")
        msg.exec_()
    
            
        
app = QApplication([])
window = DB_UI()
app.exec_()
        
        
        
        
        
    
    
    
    
    