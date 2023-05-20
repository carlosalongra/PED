import socket, time, os, sys
from request import RequestManager

class Servidor:

    def __init__(self):
        self.sok = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.path_sok = input("Introducir socket: ")

        if not self.path_sok:
            self.path_sok = 'socket_prac4'
        if os.path.exists('/tmp/' + self.path_sok):
            os.remove('/tmp/' + self.path_sok)

        self.sok.bind('/tmp/' + self.path_sok)
    
        while True:
            self.sok.listen(1)
            ns, addr = self.sok.accept()
            request = ns.recv(1024)
            response = RequestManager().responder(request)
            ns.send(response.encode('utf8'))

Servidor()
