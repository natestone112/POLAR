import socket

HOST = 'beaglebone'
PORT = 2000      # Port to listen on (non-privileged ports are > 1023)
data1 = None
# server portion
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
    s1.bind((HOST, PORT))
    s1.listen()
    conn1, addr1 = s1.accept()
    with conn1:
        print('Connected by', addr1)
        data1 = conn1.recv(1024)
        conn1.sendall(b'Data sent by Server')
print(repr(data1))
