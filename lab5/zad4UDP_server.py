import socket

HOST = '127.0.0.1'
PORT = 12346

def udp_server():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
        server_socket.bind((HOST, PORT))
        print("UDP server is listening...")

        while True:
            data, addr = server_socket.recvfrom(1024)
            if not data:
                break
            server_socket.sendto(data, addr)

if __name__ == "__main__":
    udp_server()
