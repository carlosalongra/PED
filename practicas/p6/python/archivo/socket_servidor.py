import socket, os


socket_filename = '/fichero_socket.txt'

if os.path.exists(socket_filename):
    os.remove(socket_filename)

serv_socket = socket.socket()
serv_socket.bind(socket_filename)
serv_socket.listen(10)

print("servidor esperando conexion")

while True:
    conexion, addr = serv_socket.accept() #aceptamos las peticiones, la que devuelve dos valores, el primer valor es la conexion y el segundo valor la conexion
    print("nueva conexion establecida", addr)
    
    while True:
        data = conexion.recv(1024)
        if not data:
            break
        print("recibido", data.decode('utf8'))

        conexion.send(data)

    conexion.close()

