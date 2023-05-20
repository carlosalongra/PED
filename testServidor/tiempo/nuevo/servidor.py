import socket, time, os, sys
import threading
from request import *

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

class RequestManager:

    def responder(self, peticion):
        if peticion == 'hora':
            hora = time.strftime('%H:%M:%S')
            return hora
        elif peticion == 'fecha':
            fecha = time.strftime('m%-%d-%Y')
            return fecha
        else:
            return 'error'

    if __name__ == '__main__':
        unittest.main()







