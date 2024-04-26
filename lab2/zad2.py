import socket

HOST = '127.0.0.1'  # Server IP address (localhost)
PORT = 2900        # Server port

def main():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((HOST, PORT))
        print("Connected to server.")

        # Send a message to the server
        message = "Hello, server!"
        client_socket.sendall(message.encode('utf-8'))
        print("Sent:", message)

        # Receive response from the server
        response = client_socket.recv(4096)
        print("Received:", response.decode('utf-8'))

    except ConnectionRefusedError:
        print("Connection refused. Make sure the server is running and accessible.")
    except Exception as e:
        print("An error occurred:", e)

    finally:
        # Close the socket
        client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()
