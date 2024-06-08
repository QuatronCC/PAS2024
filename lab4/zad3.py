import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 1234

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}")

    while True:
        # Odbierz dane od klienta
        data, client_address = server_socket.recvfrom(1024)
        print(f"Received data from {client_address}: {data.decode('utf-8').strip()}")

        # Odeślij dane z powrotem do klienta
        server_socket.sendto(data, client_address)
        print(f"Sent data back to {client_address}")

if __name__ == "__main__":
    start_server()
