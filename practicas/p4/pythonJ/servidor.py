import socket
import os

# Configurable parameters
SOCKET_PATH = '/tmp/my_socket'

def handle_request(conn):
    # Receive the file path from the client
    file_path = conn.recv(1024).decode().strip()

    # Check if the file exists
    if os.path.exists(file_path):
        # Open the file and send its contents to the client
        with open(file_path, 'rb') as f:
            data = f.read()
            conn.send(data)
    else:
        # Send an error message to the client
        conn.send(b'Error: file not found')

def start_server():
    # Create a socket and bind it to the specified address
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.bind(SOCKET_PATH)

    # Listen for incoming connections
    sock.listen(5)

    # Handle incoming connections
    while True:
        conn, addr = sock.accept()
        handle_request(conn)
        conn.close()

if __name__ == '__main__':
    start_server()