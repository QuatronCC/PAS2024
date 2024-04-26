import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 2901

def main():
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Connect to the server
        server_address = (SERVER_IP, SERVER_PORT)
        print("Connected to server at:", server_address)

        while True:
            # Get user input
            message = input("Enter message to send (or 'esc' to exit): ")

            # Send the message to the server
            client_socket.sendto(message.encode('utf-8'), server_address)

            # Receive response from the server
            response, _ = client_socket.recvfrom(4096)
            print("Response from server:", response.decode('utf-8'))

            if message.lower() == 'esc':
                break

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
