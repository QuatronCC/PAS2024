import socket
import time

HOST = '127.0.0.1'
PORT = 12346
MESSAGE = b'Hello, UDP!'

def udp_client():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
        start_time = time.time()
        client_socket.sendto(MESSAGE, (HOST, PORT))
        data, addr = client_socket.recvfrom(1024)
        end_time = time.time()

        print(f"Received {data} in {end_time - start_time} seconds")

if __name__ == "__main__":
    udp_client()
