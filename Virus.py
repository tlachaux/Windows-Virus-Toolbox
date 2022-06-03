import socket
import time
import os
import subprocess

import pythoncom
import pywintypes
import win32api
from win32com.shell import shell


class Virus:

    def __init__(self):

        print(shell.isUserAnAdmin())

virus = Virus()
