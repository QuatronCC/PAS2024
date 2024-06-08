import socket

HOST = '212.182.24.27'  
PORT = 2908            
MAX_MSG_LENGTH = 20     

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((HOST, PORT))
        print("Connected to server.")

        message = input("Enter message (max 20 characters): ")

        message = message[:MAX_MSG_LENGTH].ljust(MAX_MSG_LENGTH)

        sent_bytes = client_socket.sendall(message.encode('utf-8'))
        print("Sent:", message)

        # Ensure that the entire message is sent
        if sent_bytes != MAX_MSG_LENGTH:
            raise RuntimeError("Failed to send the entire message.")

        response = client_socket.recv(MAX_MSG_LENGTH)

        # Ensure that the entire response is received
        if len(response) != MAX_MSG_LENGTH:
            raise RuntimeError("Received message length mismatch.")

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
