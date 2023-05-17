import socket

HOST = '127.0.0.1'
PORT = 8000

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

print("esperando conexion...")

while True:
    conn, addr = server.recvfrom(1024)
    if conn:
        print("recibiendo archivo: ", conn)
        #file_name = conn.strip()
    
    f = open(conn.decode('utf8').strip(), 'r')
    data = True
    while data:
        data = f.read(1024)
        server.sendto(data.encode('utf8'), addr)
        if not data:
            break
        #server.sendto(data.encode('utf8'), addr)
        #server.sendto('fin del fichero'.encode('utf8'), addr)
conn.close()
server.close()
exit()
