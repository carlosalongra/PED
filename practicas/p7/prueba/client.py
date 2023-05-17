import threading
import socket

alias = input('choose a nickname: ')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 59000))

def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf8')
            if message == 'alias?':
                client.send(alias.encode('utf8'))
            else:
                print(message)
        except:
            print('ERROR')
            client.close()
            break

def client_send():
    while True:
        message = '{}: {}'.format(alias, input(""))
        client.send(message.encode('utf8'))

receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()
