#!/usr/bin/python3
from socket import *
myHost = ''
myPort= 50007

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((myHost, myPort))
sockobj.listen(5)

while True:
    connection, address = sockobj.accept()
    print('Server connected by address', address)
    while True:
        data = connection.recv(1024)
        connection.send(b'Echo ' + data)
    connection.close()