# Laser Interface Utilities
# Communicates with IL series Lasers over the TCP/IP module
import socket


# Object representing a connection to the DL-EN1 and connected lasers
class LaserArray:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        # This next line fixes an issue that occurs when more lasers are addded
        connected = send("SR,00,077", host, port)  # ***IMPORTANT*** Forces system to update # of connected lasers

        message = send('m0', host, port)  # m0 command: gets all laser measurements
        message = message.split(",")  # Splits the message at each ","
        if message[0] == "ER":
            raise LaserError
        else:
            print("Connection with lasers successful")
            print("Host: " + self.host + " Port: " + str(port))

    # gets all data relating to ALL lasers currently connected
    def getData(self):
        try:

            message = send("m0", self.host, self.port)
            if message.split(",")[0] == "ER":
                raise LaserError(message)
            return message
        except:
            raise LaserError("Failed to retrieve laser data- Connection failure")

    # gets laser measurement data of corresponding to a SPECIFIC laser
    # laser_number is an int
    def getIndividual(self, laser_number):
        full_data = self.getData()
        if laser_number < len(full_data) - 1:
            return full_data[laser_number + 1]
        else:
            raise LaserError("The laser you are attempting to access does not exist")


class LaserError(Exception):
    pass


# sends a command over tcp/ip
def send(command, host, port):
    message = bytes(command, "ascii")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(message + b"\r\n")  # all tcp/ip messages need to be terminated by \r\n
        data = repr(s.recv(1024))  # repacks the binary data received
        s.close()
    return data


if __name__ == "__main__":
    host = "169.254.222.222"
    port = 64000
    print("DEMOING")

    EN1 = LaserArray(host, port)
    print(EN1.getData())
    print(EN1.getIndividual(2))
