import socket
from threading import Thread

new_socket = socket.socket()
new_socket.bind(('127.0.0.1', 5000))

new_socket.listen(2)

print("Server is up now!")

conn1, add1 = new_socket.accept()
print("First client is connected!")

conn2, add2 = new_socket.accept()
print("Second client is connected!")

def acceptor1():
    while True:
        a = conn1.recv(1024)
        conn2.send(a)

def acceptor2():
    while True:
        b = conn2.recv(1024)
        conn1.send(b)

tread1 = Thread(target=acceptor1)
tread2 = Thread(target=acceptor2)

tread1.start()
tread2.start()