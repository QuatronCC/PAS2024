import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 1234

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))

print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}")

while True:
    data, client_address = server_socket.recvfrom(1024)
    hostname = data.decode('utf-8').strip()
    
    print(f"Received hostname: {hostname} from {client_address}")

    try:
        # Odszukaj adres IP dla otrzymanej nazwy hosta
        ip_address = socket.gethostbyname(hostname)
        result = f"IP Address: {ip_address}"
    except socket.gaierror:
        result = "Error: Could not resolve IP address"

    # Odeślij wynik do klienta
    server_socket.sendto(result.encode('utf-8'), client_address)
    print(f"Sent result: {result} to {client_address}")
