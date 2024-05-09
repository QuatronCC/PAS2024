import socket

def connect_to_server(address, port):
    try:
        # Create a TCP socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        client_socket.connect((address, port))

        # Get service name associated with the port
        service_name = socket.getservbyport(port)

        print(f"Connection successful! Service running on port {port}: {service_name}")

        # Close the socket connection
        client_socket.close()

    except ConnectionRefusedError:
        print("Connection refused. Check if the server is running and the port is open.")
    except socket.gaierror:
        print("Invalid address. Please provide a valid IP address or hostname.")
    except OSError as e:
        print(f"Failed to connect: {e}")


if __name__ == "__main__":
    server_address = input("Enter server IP address or hostname: ")
    server_port = int(input("Enter server port number: "))
    connect_to_server(server_address, server_port)
