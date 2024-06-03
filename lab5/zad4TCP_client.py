import socket
import time

HOST = '127.0.0.1'
PORT = 12345
MESSAGE = b'Hello, TCP!'

def tcp_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))

        start_time = time.time()
        client_socket.sendall(MESSAGE)
        data = client_socket.recv(1024)
        end_time = time.time()

        print(f"Received {data} in {end_time - start_time} seconds")

if __name__ == "__main__":
    tcp_client()
