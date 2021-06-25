#!/usr/bin/env python3
# TODO: NEEDS TO BE THREADED TO WORK
import socket

HOST = 'DESKTOP-J07UD08'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
data1 = None
data2 = None
# server portion
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
    s1.bind((HOST, PORT))
    s1.listen()
    conn1, addr1 = s1.accept()
    with conn1:
        print('Connected by', addr1)
        while True:
            data1 = conn1.recv(1024)
            if not data1:
                break
            conn1.sendall(b'Data sent by Server')

# Client portion
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
    s2.connect((HOST, PORT))
    s2.sendall(b'Data sent by Client')
    data2 = s2.recv(1024)

print(repr(data2) + " was received by the Client")
print(repr(data1) + " was received by the Server")
