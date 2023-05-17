import socket

# Configuración del cliente
SERVER_ADDRESS = '127.0.0.1'
SERVER_PORT = 65432

# Creación del socket UDP
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    while True:
        # Solicitando la ruta del archivo al usuario
        filename = input('Introduce la ruta del archivo: ')

        # Enviando la ruta del archivo al servidor
        sock.sendto(filename.encode(), (SERVER_ADDRESS, SERVER_PORT))

        # Recibiendo la respuesta del servidor
        file_contents, address = sock.recvfrom(1024)

        if file_contents.startswith(b'El archivo'):
            # Mostrando un mensaje de error si el archivo no existe en el servidor
            print(file_contents.decode())
        else:
            # Mostrando el contenido del archivo recibido del servidor
            print(file_contents.decode())
