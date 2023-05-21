import socket
import os

from request import RequestManager

class Servidor:
    
    def __init__(self):
        sok = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        path_sok = input("Introducir socket: ")

        if not path_sok:
            path_sok = 'socket_prac4'
        if os.path.exists('/tmp/' + path_sok):
            os.remove('/tmp/' + path_sok)
    
        sok.bind('/tmp/' + path_sok)
  
        while True:
            sok.listen(5)
            conn, addr = sok.accept()
            data = conn.recv(1024)
            fichero = open(data.decode('utf8').strip(), 'r')
            response = RequestManager().funcion(fichero)
            conn.send(response.encode('utf8'))
            conn.close()

Servidor()
