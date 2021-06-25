#!/usr/bin/env python3

import socket

HOST = '169.254.61.147'  # The server's hostname or IP address
PORT = 2505        # The port used by the server
data2 = None
# Client portion
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
    s2.connect((HOST, PORT))
    s2.sendall(b'Data sent by Client')
    data2 = s2.recv(1024)


print(repr(data2))