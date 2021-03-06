import ctypes
import platform
import socket
import os


"""
Class designed to grab information about the host machine.
"""
class Information:


    """
    Tries to obtain information about the hosting system to adapt it's behavior.
    """
    def __init__(self):

        self.systemInfos    = None
        self.computerName   = None
        self.userName       = None
        self.adminMode      = None
        self.information   = ""


    """
    Tries to obtain the OS name and version.
    """
    def obtainPlatformDescription(self):

        try:
    
            self.systemInfos = (platform.system(), platform.release())
            self.information += "OS : " + self.systemInfos[0] + "\n"
            self.information += "Version : " + self.systemInfos[1] + "\n"

        except:

            pass


    """
    Finds out if the user is in admin mode or not.
    """
    def obtainComputerName(self):

        try:
    
            self.computerName = socket.gethostname()
            self.information += "Computer ID : " + self.computerName + "\n"

        except:

            pass


    """
    Finds out if the user is in admin mode or not.
    """
    def obtainUserName(self):

        try:
    
            self.userName = os.getenv('username')
            self.information += "User ID : " + self.userName + "\n"

        except:

            pass


    """
    Finds out if the user is in admin mode or not.
    """
    def obtainUserPrivileges(self):

        try:
    
            if ctypes.windll.shell32.IsUserAnAdmin() == 1:

                self.adminMode = True
                self.information += "Admin : YES\n" 
            
            else:

                self.information += "Admin : NO\n" 

        except:

            pass

    """
    Gets information as formated string.
    """
    def toString(self):

        return self.information