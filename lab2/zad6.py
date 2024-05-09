import socket

SERVER_IP = '212.182.24.27'
SERVER_PORT = 2902

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:

        server_address = (SERVER_IP, SERVER_PORT)
        print("Connected to server at:", server_address)

        # Get user input for number, operator, and another number
        num1 = input("Enter the first number: ")
        operator = input("Enter the operator (+, -, *, /): ")
        num2 = input("Enter the second number: ")

        # Construct the message to send to the server
        message = f"{num1} {operator} {num2}"

        # Send the message to the server
        client_socket.sendto(message.encode('utf-8'), server_address)

        # Receive response from the server
        response, _ = client_socket.recvfrom(4096)
        print("Response from server:", response.decode('utf-8'))

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
