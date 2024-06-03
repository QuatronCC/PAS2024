import socket
import threading
import random

# Adres i port serwera
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345


# Funkcja obsługująca klienta
def handle_client(client_socket, secret_number):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8').strip()

            if not message:
                break  

            print(f"Received message: {message}")

            # Sprawdź, czy wiadomość jest liczbą
            if not message.isdigit():
                response = "Error: Please send a valid number."
            else:
                client_number = int(message)
                if client_number < secret_number:
                    response = "The number is too low."
                elif client_number > secret_number:
                    response = "The number is too high."
                else:
                    response = "Correct! You've guessed the number."
                    client_socket.sendall(response.encode('utf-8'))
                    break  # Zakończ połączenie, jeśli klient odgadł liczbę

            client_socket.sendall(response.encode('utf-8'))

        except Exception as e:
            print(f"An error occurred: {e}")
            break

    client_socket.close()


# Funkcja główna uruchamiająca serwer
def start_server():
    secret_number = random.randint(1, 100)
    print(f"Secret number: {secret_number}")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((SERVER_HOST, SERVER_PORT))
    server_socket.listen(5)
    print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        client_thread = threading.Thread(target=handle_client, args=(client_socket, secret_number))
        client_thread.start()


if __name__ == "__main__":
    start_server()
