import socket
import os

sok = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
path_sok = input("Introducir socket: ")

if not path_sok:
    path_sok = 'socket_prac4'
if os.path.exists('/tmp/' + path_sok):
    os.remove('/tmp/' + path_sok)

sok.bind('/tmp/' + path_sok)

num_lineas = 0
num_palabras = 0
    
while True:
    sok.listen(5)
    conn, addr = sok.accept()

    data = conn.recv(1024)
    try:
        fichero = open(data.decode('utf8').strip(), 'r')
        for linea in fichero:
            num_lineas += 1
            palabras = linea.split()
            num_palabras += len(palabras)
        
            
        resultado = f"Lineas: {num_lineas} \nPalabras: {num_palabras}"
        conn.send(resultado.encode('utf8'))
    except:
        resultado = "ERROR"
        conn.sendall(resultado.encode('utf8'))
    conn.close()
