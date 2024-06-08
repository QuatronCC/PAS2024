import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_HOST, SERVER_PORT))

print(f"Server listening on {SERVER_HOST}:{SERVER_PORT}")

while True:
    data, client_address = server_socket.recvfrom(1024)
    message = data.decode('utf-8').strip()
    
    print(f"Received message: {message} from {client_address}")

    try:
        num1, operator, num2 = message.split()
        num1 = float(num1)
        num2 = float(num2)
        
        # Oblicz wynik w zależności od operatora
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = 'Error: Division by zero'
        else:
            result = 'Error: Invalid operator'
    
    except ValueError:
        result = 'Error: Invalid numbers'
    except Exception as e:
        result = f"Error: {str(e)}"

    # Odeślij wynik do klienta
    server_socket.sendto(str(result).encode('utf-8'), client_address)
    print(f"Sent result: {result} to {client_address}")
