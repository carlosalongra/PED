import socket
import os

sok = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
path_sok = input("Introducir socket: ")

if not path_sok:
    path_sok = 'socket_prac4'
if os.path.exists('/tmp/' + path_sok):
    os.remove('/tmp/' + path_sok)

sok.bind('/tmp/' + path_sok)

while True:
    sok.listen(5)
    conn, addr = sok.accept()

    data = conn.recv(1024)
    try: 
        fichero = open(data.decode('utf8').strip(), 'r')
        leer = fichero.readline()
        while leer != '':
            conn.send(leer.encode('utf8'))
            leer = fichero.readline()
        print("enviando fichero")
    except:    
        conn.send("fichero no existe.".encode('utf8'))
    conn.close()
