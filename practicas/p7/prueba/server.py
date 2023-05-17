import threading
import socket

host = '127.0.0.1'
port = 59000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
aliases = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast('{} has left the chat'.format(alias).encode("utf8"))
            aliases.remove(alias)
            break

def receive():
    while True:
        print('server is running...')
        client, addr = server.accept()
        client.send('alias?'.encode('utf8'))
        alias = client.recv(1024)
        aliases.append(alias)
        clients.append(client)
        print('the alias of the client is {}'.format(alias).encode('utf8'))
        broadcast('{} has connected to the chatroom'.format(alias).encode('utf8'))
        client.send('you are connected'.encode('utf8'))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == "__main__":
    receive()

