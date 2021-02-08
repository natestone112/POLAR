# Core for GUI
# Quick Guide: create a connected GUI object with easyGUI(startFunc, stopFunc, resetFunc)
#   ---> then RUN() gui function
import tkinter as tk
from threading import Thread
class runtimeGUI:
    # Sets all parameters for the GUI buttons, labels, etc.
    # must be run before starting the GUI
    def __init__(self, startFunc, stopFunc, resetFunc):
        self.window = tk.Tk()
        self.mainLabel = tk.Label(
            text="BeagleEye3000",
            foreground="Orange",  # Set the text color to white
            background="black",  # Set the background color to black
            width="20", # pixels
        )

        self.stopButton = tk.Button(
            text="STOP!",
            width=25,
            height=5,
            bg="red",
            fg="yellow",
        )

        self.startButton = tk.Button(
            text="START",
            width=25,
            height=5,
            bg="green",
            fg="yellow",
        )

        self.resetButton = tk.Button(
            text="Reset",
            width=25,
            height=5,
            bg="black",
            fg="yellow",
        )

        # pack() places objects within window frame
        self.mainLabel.pack(side="top")
        self.startButton.pack(side="left")
        self.resetButton.pack(side="right")
        self.stopButton.pack(side="right")

        self.connectStartButton(startFunc)
        self.connectStopButton(stopFunc)
        self.connectResetButton(resetFunc)

    # functions used to connect a button press with a certain functions
    # parameter func = function to be run when button is pressed
    # **Based on a wiring format** i.e wire button to func
    def connectStartButton(self, func):
        self.startButton.bind('<Button-1>', func)

    def connectStopButton(self, func):
        self.stopButton.bind('<Button-1>', func)

    def connectResetButton(self, func):
        self.resetButton.bind('<Button-1>', func)

    # RUN() starts the runtimeGUI
    # Connections to functions must be set before RUN()
    # runs inside a new thread, returns reference to said thread
    def RUN(self):

        thread = Thread(target = self.window.mainloop(), args = ())
        self.window.mainloop()
        return thread



def beep(self):
    print("beep!")

#tester
if(__name__ == "__main__"):
    gui = runtimeGUI(beep, beep, beep)
    gui.RUN()
