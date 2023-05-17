import socket
import os
import threading

server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
nombre_chat = input("Introducir el nombre del chat: ")

if not nombre_chat:
    nombre_chat = 'chat_defecto'
if os.path.exists('/tmp/' + nombre_chat):
    os.remove('/tmp/' + nombre_chat)

server.bind('/tmp/' + nombre_chat)

server.listen(5)

clients = []
nicknames = []

def handle(client): 
    while True:
        #data, addr = server.accept()
        try:
            mensaje = client.recv(1024)#.decode("utf8")
            if mensaje:
                for client in clients:
                    #if client != data:
                    client.send(mensaje)#.encode("utf8")
        except: # al salir del chat mensaje
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            #broadcast("el cliente {} salio del chat".format(nickname).encode("utf8"))
            nicknames.remove(nickname)
            break

def receive():
    while True: 
        client, addr = server.accept()
        client.send('bienvenido al chat!!'.encode("utf8"))#mensaje para el servidor del nickname
        #client.send('NICK'.encode("utf8"))
        nickname = client.recv(1024).decode("utf8")
        nicknames.append(nickname)
        clients.append(client)
        
        print("nickname del cliente: {}".format(nickname))
        
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

        #while True:
         #   data, addr = server.accept()
          #  try:
           #     mensaje = data.recv(1024).decode("utf8")
            #    if mensaje:
             #       for client in clients:
              #          if client != data:
               #             client.send(mensaje).encode("utf8")
            #except: # al salir del chat mensaje
             #   index = clients.index(client)
              #  clients.remove(client)
               # client.close()
                #nickname = nicknames[index]
                #broadcast("el cliente {} salio del chat".format(nickname).encode("utf8"))
                #nicknames.remove(nickname)
                #break

       # broadcast("{} se unio al chat".format(nickname).encode("utf-8"))
receive()
#handle()

