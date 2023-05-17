import socket

HOST = '127.0.0.1'
PORT = 8000

clien = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

filename = input("Introdice el nombre del fichero a enviar: ")

clien.sendto(filename.encode('utf8'), (HOST, PORT))

f = open(filename, 'r')
while True:
    data, addr = clien.recvfrom(1024)
    if not data:
        break
    print(data.decode('utf8').strip())
clien.close()
