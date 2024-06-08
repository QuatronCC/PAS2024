import socket

SERVER_HOST = '212.182.24.27'  
SERVER_PORT = 2900             
BUFFER_SIZE = 20               

def pad_message(message):
    """Ensure the message is exactly BUFFER_SIZE characters long."""
    if len(message) > BUFFER_SIZE:
        return message[:BUFFER_SIZE]
    return message.ljust(BUFFER_SIZE)

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        print("Connected to server.")
        
        message = input("Enter a message to send: ")
        message = pad_message(message)

        client_socket.sendall(message.encode('utf-8'))
        print(f"Sent: {message}")

        # Odbierz odpowiedź od serwera
        response = client_socket.recv(BUFFER_SIZE)
        print("Received:", response.decode('utf-8'))
    
    except ConnectionRefusedError:
        print("Connection refused. Make sure the server is running and accessible.")
    except Exception as e:
        print("An error occurred:", e)
    
    finally:
        # Zamknij połączenie
        client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()
