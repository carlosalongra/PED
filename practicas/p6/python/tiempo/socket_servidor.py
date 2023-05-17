import socket, time

#creamos el socket con los valores por defecto
serv_socket = socket.socket()
serv_socket.bind (('localhost', 8000)) #establecemos la conexion, recibe una tupla, el primero el host, el segundo el puerto
serv_socket.listen(5) # cantidad de peticiones que puede manegar en cola el socket

timeformat = '%Y-%m-%d %H:%M:%S'

while True:
    conexion, addr = serv_socket.accept() #aceptamos las peticiones, la que devuelve dos valores, el primer valor es la conexion y el segundo valor la conexion
    print("nueva conexion establecida", addr)
   
    peticion = conexion.recv(1024)
    print(peticion)

    tiempo = time.strftime(timeformat)
    conexion.send(tiempo.encode('utf8'))
    conexion.close()

