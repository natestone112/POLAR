import ftplib

# ************UNFINISHED SCRIPT******************
# Intended to download all measurements over ethernet ftp protocol



# Open the FTP connection
host = "beagleboard"
ftp = ftplib.FTP(host)
ftp.login("debian", "temppwd")
ftp.cwd('/measurements')


filenames = ftp.nlst()

print("----Measurement File Download Tool----\n\n")
print("Connected to: " + host + "\n\n")
print("Which database would you like to download?")
database = input()
print("Files in the database: ")
for i in filenames:
    print(i)

print("\n")
print("Type the name of the file you wish to download, or 'all' to download all")
filename = input
if filename == "all":
    for filename in filenames:
        with open(filename, 'wb') as file:
            ftp.retrbinary('RETR %s' % filename, file.write)

elif filename in filenames:
    with open(filename, 'wb') as file:
        ftp.retrbinary('RETR %s' % filename, file.write)

else:
    print("File does not exist: Spelling IS case sensitive")