import socket

BUFFER_SIZE = 20  # Maksymalna długość wiadomości

def pad_message(message):
    """Ensure the message is exactly BUFFER_SIZE characters long."""
    if len(message) > BUFFER_SIZE:
        return message[:BUFFER_SIZE]
    return message.ljust(BUFFER_SIZE)

def connect_to_server(address, port):
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        client_socket.connect((address, port))
        print("Connection successful!")

        message = input("Enter a message to send (max 20 characters): ")
        padded_message = pad_message(message)

        # Wyślij wiadomość do serwera
        client_socket.sendall(padded_message.encode('utf-8'))
        print(f"Sent: {padded_message}")

        # Odbierz odpowiedź od serwera
        response = client_socket.recv(BUFFER_SIZE)
        print("Received:", response.decode('utf-8'))

        # Close the socket connection
        client_socket.close()

    except ConnectionRefusedError:
        print("Connection refused. Check if the server is running and the port is open.")
    except socket.gaierror:
        print("Invalid address. Please provide a valid IP address or hostname.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    server_address = input("Enter server IP address or hostname: ")
    server_port = int(input("Enter server port number: "))
    connect_to_server(server_address, server_port)
