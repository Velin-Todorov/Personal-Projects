from PySide6.QtWidgets import (QFormLayout, QApplication, QLabel, QPushButton, QLineEdit, QDialog, QVBoxLayout)
from PySide6.QtCore import Qt
from PySide6.QtGui import QMovie
import sys 

class LoginForm(QDialog):
    
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.initial_screen()
        self.setStyleSheet("LoginForm {background-color: #f4f6f7 }")


    def initial_screen(self):

        #Login Form geometry
        self.setFixedSize(280, 300)

        # Username and Password fields
        self.username_field = QLineEdit()
        self.password_field = QLineEdit()

        # Login Button
        self.login_button = QPushButton("Login")

        #Lock Animation
        self.lock_label = QLabel()
        self.lock_animation = QMovie(r'C:\Users\velin\OneDrive\Desktop\VS repos\Personal-Projects\Password Manager\lock.gif')
        self.lock_label.setMovie(self.lock_animation)
        self.lock_label.setAlignment(Qt.AlignCenter)
        self.lock_animation.start()

        # Create new Account Link
        self.Make_New_Account = QLabel()
        self.Make_New_Account.setText("<a style= text-decoration:none; href='http://127.0.0.1:5500/Password%20Manager/Sign-up%20page.html'> Don't Have An Account? Click Here to Make One!</a>")
        self.Make_New_Account.setOpenExternalLinks(True)

        # Modifying the Password field
        self.password_field.setEchoMode(self.password_field.EchoMode.Password)
        self.password_field.setFixedWidth(120)
    
        # Modifying the Username field
        self.username_field.setFixedWidth(120)
        self.username_label = QLabel()
        self.username_label.setText('Username: ')

        # Modifying the Login Button and the new Create New Account Button
        self.login_button.setFixedWidth(120)
 
        # Login Layout
        self.login_form_layout = QVBoxLayout()

        login_layout = QFormLayout()
        login_layout.addRow(QLabel('Username: '), self.username_field)
        login_layout.addRow(QLabel('Password: '), self.password_field)
        login_layout.addWidget(self.login_button)
        login_layout.addRow(self.Make_New_Account)
        login_layout.addRow(QLabel())
        login_layout.addRow(self.lock_label)
        

        self.login_form_layout.setSpacing(10)
        self.login_form_layout.addLayout(login_layout)
        
        self.setLayout(self.login_form_layout)

        self.login_button.clicked.connect(self.greet)
        self.setWindowTitle('Password Manager')


    # Test to see if Login Button is Working
    def greet(self):
        print('Successful login!')
        
app = QApplication(sys.argv)
login_form= LoginForm()
app.setStyle('Fusion')
login_form.show()
app.exec()