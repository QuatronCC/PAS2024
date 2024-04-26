import socket

SERVER_IP = '212.182.24.27'
SERVER_PORT = 2901            

def main():
    # Utwórz obiekt gniazda UDP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        message = input("Wpisz wiadomość do wysłania: ")

        client_socket.sendto(message.encode('utf-8'), (SERVER_IP, SERVER_PORT))

        response, server_address = client_socket.recvfrom(4096)
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
