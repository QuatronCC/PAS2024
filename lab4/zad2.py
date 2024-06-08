import socket
import threading

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 1234

def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break 

            print(f"Received data: {data.decode('utf-8').strip()}")

            # Odeślij dane z powrotem do klienta
            client_socket.sendall(data)

        except Exception as e:
            print(f"An error occurred: {e}")
            break
          
    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(5)
    print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    start_server()
