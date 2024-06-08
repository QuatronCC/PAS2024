import socket

SERVER_IP = '212.182.24.27'  
SERVER_PORT = 2906          

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        client_ip = socket.gethostbyname(socket.gethostname())

        server_address = (SERVER_IP, SERVER_PORT)
        print("Connected to server at:", server_address)

        client_socket.sendto(client_ip.encode('utf-8'), server_address)

        response, _ = client_socket.recvfrom(4096)
        hostname = response.decode('utf-8')
        print("Hostname received from server:", hostname)

    except ConnectionRefusedError:
        print("Connection refused. Make sure the server is running and accessible.")
    except Exception as e:
        print("An error occurred:", e)

    finally:
        client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()
