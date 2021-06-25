import LaserUTIL
from LaserUTIL import send
from time import sleep
from os import system
# This is not a multipurpose file. This works under various assumptions, such as the decimal placement

# These values are set by us outside of this file
host = "169.254.222.222"
port = 64000

print("Laser Demo prints formatted values")


while 1:
    _ = system('cls') # Clears screen
    print("Current Value: ")
    message = send("m0", host, port)  # sends a command, receives a string
    message = message.split(",")  # Splits the message at each ","
    message = message[1]  # takes the value from the second section of the message
    message = message.replace("+", "")  # Removes "+" from the string to make it an int
    message = (int(message))  # Converts message to int
    print(message/100)  # Prints the message as a float in mm
    sleep(0.1)  # Sleep for a period of time
