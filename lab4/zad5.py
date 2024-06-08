import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))

print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}")

while True:
    data, client_address = server_socket.recvfrom(1024)
    ip_address = data.decode('utf-8').strip()
    
    print(f"Received IP address: {ip_address} from {client_address}")

    try:
        # Odszukaj nazwę hosta dla otrzymanego adresu IP
        hostname = socket.gethostbyaddr(ip_address)[0]
        result = f"Hostname: {hostname}"
    except socket.herror:
        result = "Error: Could not resolve hostname"

    # Odeślij wynik do klienta
    server_socket.sendto(result.encode('utf-8'), client_address)
    print(f"Sent result: {result} to {client_address}")
