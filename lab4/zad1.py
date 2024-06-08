import socket
import threading
from datetime import datetime

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 1234

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8').strip()
            
            if not message:
                break

            print(f"Received message: {message}")

            # Pobierz aktualną datę i czas
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Wyślij aktualną datę i czas do klienta
            client_socket.sendall(current_datetime.encode('utf-8'))
        
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
