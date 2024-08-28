from PyQt5.QtWidgets import QApplication, QMessageBox, QListWidget, QWidget, QVBoxLayout, QTextEdit, QListWidgetItem

from mainpage import MainPage
from loginpage import LoginPage
from registerpage import RegisterPage
from myposts import MyPostsPage
from addpost import AddPostPage
from allposts import AllPostsPage

from components import TextArea

from database import Database
from errors import UsernameAlreadyExistsError
from os import system



system("clear")


class ListWidgetWithTextArea(QListWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setGeometry(50, 120, 350, 450)

    def addTextAreaItem(self, text: str):        
        widget = QWidget()
        
        layout = QVBoxLayout()
        
        text_edit = TextArea(widget, 0)
        text_edit.setText(text)
        text_edit.setEnabled(False)
        
        layout.addWidget(text_edit)
        
        widget.setLayout(layout)
        
        item = QListWidgetItem()
        
        item.setSizeHint(widget.sizeHint())
        
        self.addItem(item)
        
        self.setItemWidget(item, widget)




class App:
    USER = None
    ALL_POSTS = []

    def __init__(self) -> None:
        self.boshSahifaOyna = MainPage()
        self.loginOyna = LoginPage()
        self.registerOyna = RegisterPage()
        self.meningPostlarimOyna = MyPostsPage()
        self.postQoshishOyna = AddPostPage()
        self.hammaPostlarOyna = AllPostsPage()

        self.database = Database()
        self.postsCollectionLW = ListWidgetWithTextArea(self.hammaPostlarOyna)
        self.postsCollectionLW2 = ListWidgetWithTextArea(self.meningPostlarimOyna)

        self.boshSahifaOyna.loginBtn.clicked.connect(self.showLoginPage)
        self.boshSahifaOyna.registerBtn.clicked.connect(self.showRegisterPage)

        self.loginOyna.loginBtn.clicked.connect(self.loginFunction)
        self.registerOyna.registerBtn.clicked.connect(self.registerFunction)
        
        self.postQoshishOyna.addPostBtn.clicked.connect(self.addPostPage)
        self.hammaPostlarOyna.writePostBtn.clicked.connect(self.writePost)
        self.hammaPostlarOyna.myPostsBtn.clicked.connect(self.mypostview)
        self.boshSahifaOyna.show()
        


    def loginFunction(self):
        username = self.loginOyna.usernameInput.text()
        password = self.loginOyna.passwordInput.text()

        foundUser = self.database.login(username, password)

        if not foundUser:
            return self.alert("Foydalanuvchi nomi topilmadi!")
    
        self.USER = foundUser
        
        self.showAllPostsPage()

    
    def registerFunction(self):
        try:
            name = self.registerOyna.nameInput.text().strip()
            surname = self.registerOyna.surnameInput.text().strip()
            username = self.registerOyna.usernameInput.text().strip()
            password = self.registerOyna.passwordInput.text().strip()

            new_user = self.database.register(name, surname, username, password)
            self.USER = new_user

            return self.showAllPostsPage()
        except UsernameAlreadyExistsError as message:
            errorMessage = message.args[0]
            return self.alert(errorMessage)
    

    def alert(self, text: str):
        msgbox = QMessageBox()
        msgbox.setIcon(QMessageBox.Warning)
        msgbox.setText(text)
        msgbox.setStandardButtons(QMessageBox.Ok)

        return msgbox.exec()


    def showLoginPage(self):
        self.loginOyna.show()
        self.boshSahifaOyna.close()


    def showRegisterPage(self):
        self.registerOyna.show()
        self.boshSahifaOyna.close()


    def showAllPostsPage(self):
        self.ALL_POSTS = self.database.selectAllPosts()

        for POST in self.ALL_POSTS:
            self.postsCollectionLW.addTextAreaItem(POST['text'])

        self.hammaPostlarOyna.show()
        self.loginOyna.close()
        self.registerOyna.close()
        
        
    def writePost(self):
        self.hammaPostlarOyna.close()
        self.postQoshishOyna.show()
        
    def addPostPage(self):
        self.post_text = self.postQoshishOyna.postTextArea.toPlainText()
        self.ALL_POSTS = self.database.selectAllPosts()
        self.post_ID = self.ALL_POSTS[-1]['id'] + 1
        self.user_ID = self.USER['id']
        self.database.addPost(self.user_ID, self.post_text)
        self.post_text = ""
        self.postQoshishOyna.postTextArea.setText(self.post_text)
        
    def mypostview(self):
        self.ALL_POSTS = self.database.selectAllPosts()
        self.user_ID = self.ALL_POSTS[-1]['user_id']
        print(self.ALL_POSTS[3]['text'])
        for POST in self.ALL_POSTS:
            if POST['user_id'] == self.USER["id"]:
                self.postsCollectionLW2.addTextAreaItem(POST['text'])

        self.meningPostlarimOyna.show()
        self.hammaPostlarOyna.close()
    
        
      
        
        





app = QApplication([])

dastur = App()

app.exec()