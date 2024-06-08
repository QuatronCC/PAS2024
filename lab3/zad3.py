import socket

HOST = '127.0.0.1'
PORT = 2900

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((HOST, PORT))
        print("Connected to server.")

        while True:

            message = input("Wpisz wiadomość (lub wpisz 'esc' aby wyjść): ")

            if message.lower() == 'esc':
                break

            # Send message to server
            client_socket.sendall(message.encode('utf-8'))

            # Receive message from server
            response = client_socket.recv(4096)
            print("Odpowiedź od serwera:", response.decode('utf-8'))

    except ConnectionRefusedError:
        print("Połączenie zostało odrzucone. Upewnij się, że serwer działa i jest dostępny.")
    except Exception as e:
        print("Wystąpił błąd:", e)

    finally:
        client_socket.close()
        print("Zamknięto połączenie.")

if __name__ == "__main__":
    main()
