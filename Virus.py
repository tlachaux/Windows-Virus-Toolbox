import ctypes
import platform
import socket
import os
import time
import shutil


class Virus:


    """
    Tries to obtain informations about the hosting system to adapt it's behavior.
    """
    def __init__(self):

        self.systemInfos    = None
        self.computerName   = None
        self.userName       = None
        self.adminMode      = None

        self.informations   = ""


    """
    Tries to obtain the OS name and version.
    """
    def obtainPlatformDescription(self):

        try:
    
            self.systemInfos = (platform.system(), platform.release())
            self.informations += "OS : " + self.systemInfos[0] + "\n"
            self.informations += "Version : " + self.systemInfos[1] + "\n"

        except:

            pass


    """
    Finds out if the user is in admin mode or not.
    """
    def obtainComputerName(self):

        try:
    
            self.computerName = socket.gethostname()
            self.informations += "Computer ID : " + self.computerName + "\n"

        except:

            pass


    """
    Finds out if the user is in admin mode or not.
    """
    def obtainUserName(self):

        try:
    
            self.userName = os.getenv('username')
            self.informations += "User ID : " + self.userName + "\n"

        except:

            pass


    """
    Finds out if the user is in admin mode or not.
    """
    def obtainUserPrivileges(self):

        try:
    
            if ctypes.windll.shell32.IsUserAnAdmin() == 1:

                self.adminMode = True
                self.informations += "Admin : YES\n" 
            
            else:

                self.informations += "Admin : NO\n" 

        except:

            pass
    

    """
    Displays informations gathered for debug purposes.
    """
    def displayInformations(self):

        print(self.informations)
    

    def ensureRunAtStartup(self):

        pass
        #if os.getcwd() is not "C:\\Users\\" + self.userName + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup":

        #    shutil.copy(os.getcwd() + "\\Virus.exe", "C:\\Users\\" + self.userName + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\Virus.exe")
    


    """
    Grabs informations, then tries multiple vectors of attack.
    """
    def run(self):

        self.obtainPlatformDescription()
        self.obtainComputerName()
        self.obtainUserName()
        self.obtainUserPrivileges()

        #self.ensureRunAtStartup()


"""
-----------------------------------------------------
"""
virus = Virus()
virus.run()
virus.displayInformations()

time.sleep(5)