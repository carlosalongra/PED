import socket, time, os, sys
import threading

class Servidor:

    def __init__(self):
        self.sok = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.path_sok = input("Introducir socket: ")

        if not self.path_sok:
            self.path_sok = 'socket_prac4'
        if os.path.exists('/tmp/' + self.path_sok):
            os.remove('/tmp/' + self.path_sok)

        self.sok.bind('/tmp/' + self.path_sok)

    def hora(self):
        #mensaje = conexion.recv(1024)
        horaformat = '%H:%M:%S'
        while True:
            self.sok.listen(1)
            conexion, addr = self.sok.accept()
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
        dateformat = '%m-%d-%Y'
        while True:
            self.sok.listen(1)
            conexion, addr = self.sok.accept()
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

servidor = Servidor()

#while True:
hora_thread = threading.Thread(target=servidor.hora)
fecha_thread = threading.Thread(target=servidor.fecha)

hora_thread.start()
fecha_thread.start()

hora_thread.join()
fecha_thread.join()
