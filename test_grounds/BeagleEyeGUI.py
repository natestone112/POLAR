import tkinter as tk
window = tk.Tk()

mainLabel = tk.Label(
    text="BeagleEye3000",
    foreground="Orange",  # Set the text color to white
    background="black",  # Set the background color to black
    width="20",
)

stopButton = tk.Button(
    text="STOP!",
    width=25,
    height=5,
    bg="red",
    fg="yellow",
)

startButton = tk.Button(
    text="START",
    width=25,
    height=5,
    bg="green",
    fg="yellow",
)

resetButton = tk.Button(
    text="Reset",
    width=25,
    height=5,
    bg="black",
    fg="yellow",
)



def beep(event):
    print("Beep!")




mainLabel.pack(side="top")
startButton.pack(side="left")
resetButton.pack(side="right")
stopButton.pack(side="right")

startButton.bind('<Button-1>', beep)



window.mainloop()
