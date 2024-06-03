import socket

SERVER_IP = '212.182.24.27'
SERVER_PORT = 2912

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((SERVER_IP, SERVER_PORT))
        print("Connected to server.")

        while True:
            user_input = input("Enter a number to guess (or 'quit' to exit): ")

            if user_input.lower() == 'quit':
                break

            try:
                # Validate user input is a number
                guess = int(user_input)
            except ValueError:
                print("Please enter a valid number.")
                continue

            client_socket.sendall(str(guess).encode('utf-8'))
            print(f"Sent: {guess}")

            response = client_socket.recv(4096).decode('utf-8')
            print(f"Received: {response}")

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
