import socket

# Configuración del servidor
HOST = '127.0.0.1'
PORT = 65432

# Creación del socket UDP
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    # Enlazando el socket con el puerto y la dirección
    sock.bind((HOST, PORT))
    print(f'Servidor escuchando en {HOST}:{PORT}...')

    # Bucle principal del servidor
    while True:
        # Recibiendo la solicitud del cliente
        data, address = sock.recvfrom(1024)
        filename = data.decode()

        try:
            # Leyendo el contenido del archivo
            with open(filename, 'r') as f:
                file_contents = f.read()
            # Enviando el contenido del archivo al cliente
            sock.sendto(file_contents.encode(), address)
            print(f'Se ha enviado el contenido del archivo "{filename}" a {address}')
        except FileNotFoundError:
            # Enviando un mensaje de error al cliente si el archivo no existe
            error_message = f'El archivo "{filename}" no existe'
            sock.sendto(error_message.encode(), address)
            print(f'No se ha encontrado el archivo "{filename}", se ha enviado un mensaje de error a {address}')
