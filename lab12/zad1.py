import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

def handle_client(client_socket, client_address):
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                print(f"Connection from {client_address[0]}:{client_address[1]} closed.")
                break

            print(f"Received from {client_address[0]}:{client_address[1]}: {message.decode('utf-8')}")

            client_socket.sendall(message)
        except ConnectionResetError:
            print(f"Connection from {client_address[0]}:{client_address[1]} was reset.")
            break
          
    client_socket.close()

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Echo server listening on {HOST}:{PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        
        # Utwórz nowy wątek do obsługi klienta
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    start_server()
