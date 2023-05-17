import socket

cli_socket = socket.socket()
cli_socket.connect( ('localhost', 8000) )


mensaje = "hora mandada"
cli_socket.send(mensaje.encode('utf8'))

respuesta = cli_socket.recv(1024) #para que podamos recibir los que un socket esta enviando ponemos recv(1024 - referencia al buffer 1024 bytes)

print(respuesta)
cli_socket.close()
