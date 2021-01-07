import socket
from decouple import config


HOST = '127.0.0.1'
PORT = int(config("PORT"))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    socket.connect((HOST, PORT))
    while True:
        something = input("Say something: ")
        socket.sendall(something.encode('utf-8'))
        data = socket.recv(1024)
        print('Received', repr(data)[2:-1])
