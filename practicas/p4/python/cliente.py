import socket
import os

sok = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
path_sok = input("Introducir socket: ")

try:
    sok.connect('/tmp/' + path_sok)
except:
    print("no hay socket abierto que se llame " + path_sok)
    exit()

path_fichero = input("Introducir ruta fichero: ")
sok.send(path_fichero.encode('utf8'))

while True:
    data = sok.recv(1024)
    if not data: 
        break
    print(data.decode('utf8').strip())
sok.close()
