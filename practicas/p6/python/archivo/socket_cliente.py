import socket, os


socket_filename = 'fichero_socket.txt'

cli_socket = socket.socket()
cli_socket.connect(socket_filename)

while True:
cli_socket.send(filepath)

respuesta = cli_socket.recv(1024) #para que podamos recibir los que un socket esta enviando ponemos recv(1024 - referencia al buffer 1024 bytes)

print(respuesta)
cli_socket.close()


