import socket
from decouple import config
import sys

HOST = '127.0.0.1'
PORT = int(config("PORT"))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket:
    socket.connect((HOST, PORT))
    # something = input("Say something: ")
    request = ''
    for arg in sys.argv:
        if '.py' not in arg:
            request += str(arg) + ' '

    socket.sendall(request.strip().encode('utf-8'))
    data = socket.recv(1024)
    print('Received', repr(data)[2:-1])
    socket.close()
