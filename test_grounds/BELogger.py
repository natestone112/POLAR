import os
import datetime

# Code section that always creates the necesary files when imported

# Creates logs directory if it does not exist
if (not os.path.isdir("logs")):
    os.mkdir("logs")

f = open("logs\eventLog.txt", 'a+')

today = datetime.date.today()
f.write("Start of event log for: " + today.strftime("%d/%m/%Y"))
f.close()
