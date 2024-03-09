import sys
import socket


def scan_ports(server_address):
    try:
        # Get IP address from the given hostname
        server_ip = socket.gethostbyname(server_address)
        print(f"Scanning ports on {server_address} ({server_ip}):")

        # Define range of ports to scan
        start_port = 1
        end_port = 1024

        for port in range(start_port, end_port + 1):

            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.settimeout(0.5)

            # Attempt to connect to the port
            result = client_socket.connect_ex((server_ip, port))

            if result == 0:
                print(f"Port {port} is open")

            # Close the socket connection
            client_socket.close()

    except socket.gaierror:
        print("Invalid address. Please provide a valid IP address or hostname.")


if __name__ == "__main__":

    server_address = input("Give ip address or hostname: ")

    scan_ports(server_address)
