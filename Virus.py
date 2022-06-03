import ctypes
import platform


class Virus:



    """
    Tries to obtain informations about the hosting system to adapt it's behavior.
    """
    def __init__(self):

        self.systemInfos    = None
        self.adminMode      = None

        self.obtainPlatformDescription()
        self.obtainUserPrivileges()


    """
    Tries to obtain the OS name and version.
    """
    def obtainPlatformDescription(self):

        try:
    
            self.systemInfos = (platform.system(), platform.release())

        except:

            pass


    """
    Finds out if the user is in admin mode or not.
    """
    def obtainUserPrivileges(self):

        try:
    
            self.adminMode = (ctypes.windll.shell32.IsUserAnAdmin() == 1)

        except:

            pass
    

    """
    Displays informations gathered for debug purposes.
    """
    def displayInformations(self):

        print(self.systemInfos)
        print(self.adminMode)


"""
-----------------------------------------------------
"""
virus = Virus()
virus.displayInformations()
