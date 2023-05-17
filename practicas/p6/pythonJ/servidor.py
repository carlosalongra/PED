import socket

# Configuración del servidor
HOST = '127.0.0.1'
PORT = 65432

# Creación del socket TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Enlazando el socket con el puerto y la dirección
    sock.bind((HOST, PORT))
    sock.listen()
    print(f'Servidor escuchando en {HOST}:{PORT}...')

    # Bucle principal del servidor
    while True:
        # Aceptando la conexión del cliente
        conn, address = sock.accept()
        print(f'Cliente conectado desde {address}')

        # Recibiendo la solicitud del cliente
        data = conn.recv(1024)
        filename = data.decode()

        try:
            # Leyendo el contenido del archivo
            with open(filename, 'r') as f:
                file_contents = f.read()
            # Enviando el contenido del archivo al cliente
            conn.sendall(file_contents.encode())
            print(f'Se ha enviado el contenido del archivo "{filename}" a {address}')
        except FileNotFoundError:
            # Enviando un mensaje de error al cliente si el archivo no existe
            error_message = f'El archivo "{filename}" no existe'
            conn.sendall(error_message.encode())
            print(f'No se ha encontrado el archivo "{filename}", se ha enviado un mensaje de error a {address}')
        
        # Cerrando la conexión con el cliente
        conn.close()
        print(f'Conexión con {address} cerrada')
