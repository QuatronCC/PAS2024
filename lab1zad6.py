import socket

def connect_to_server(address, port):
    try:
        # Create a TCP socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        client_socket.connect((address, port))

        print("Connection successful!")

        # Close the socket connection
        client_socket.close()

    except ConnectionRefusedError:
        print("Connection refused. Check if the server is running and the port is open.")
    except socket.gaierror:
        print("Invalid address. Please provide a valid IP address or hostname.")


if __name__ == "__main__":
    server_address = input("Enter server IP address or hostname: ")
    server_port = int(input("Enter server port number: "))
    connect_to_server(server_address, server_port)
