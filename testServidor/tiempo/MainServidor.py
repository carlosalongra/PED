import socket, time, os

class Servidor:

    sok = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    path_sok = input("Introducir socket: ")

    if not path_sok:
        path_sok = 'socket_prac4'
    if os.path.exists('/tmp/' + path_sok):
        os.remove('/tmp/' + path_sok)

    sok.bind('/tmp/' + path_sok)

    horaformat = '%H:%M:%S'
    dateformat = '%m-%d-%Y'
    
    while True:
        sok.listen(1)
        conexion, addr = sok.accept()
        mensaje = conexion.recv(1024)

    def hora(self):
        mensaje = conexion.recv(1024)

        try:
            hora = time.strftime(horaformat)
            if mensaje.decode('utf8') == 'hora':
                conexion.send(hora.encode('utf8'))
            else:
                conexion.send('error'.encode('utf8'))
        except:
            conexion.send('consulta no existe'.encode('utf8'))
        conexion.close()

    def fecha(self):
        mensaje = conexion.recv(1024)

        try:
            fecha = time.strftime(dateformat)
            if mensaje.decode('utf8') == 'fecha':
                conexion.send(fecha.encode('utf8'))
            else:
                conexion.send('error'.encode('utf8'))
        except:
            conexion.send('consulta no existe'.encode('utf8'))

        conexion.close()

