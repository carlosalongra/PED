import socket

# Configurable parameters
SERVER_ADDRESS = '/tmp/my_socket'

def get_file_contents(file_path):
    # Connect to the server and send the file path
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as sock:
        sock.connect(SERVER_ADDRESS)
        sock.send(file_path.encode())

        # Receive the file contents from the server
        data = sock.recv(1024)

        # Print the contents or the error message
        print(data.decode())

if __name__ == '__main__':
    file_path = input('Enter file path: ')
    get_file_contents(file_path)