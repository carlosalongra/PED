import socket
import threading

client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
nombre_chat = input("introdicir nombre del chat: ")

try:
    client.connect('/tmp/' + nombre_chat)
except:
    print("no hay chat abierto que se llame " + nombre_chat)
    exit()

#mensaje de bienvenida
print(client.recv(1024).decode("utf8"))

nickname = input("elije un nickname: ")
client.send(nickname.encode("utf-8"))

def write():
    while True: 
        mensaje = "{}: {}".format(nickname, input(""))
        client.send(mensaje.encode("utf8"))

thread_write = threading.Thread(target=write)
thread_write.start()


