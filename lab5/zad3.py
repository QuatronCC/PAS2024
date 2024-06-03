import socket

UDP_SERVER_IP = '212.182.24.27'
TCP_SERVER_IP = '212.182.24.27'
TCP_PORT = 2913


def send_udp_message(port, message):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.settimeout(1)
    udp_socket.sendto(message.encode('utf-8'), (UDP_SERVER_IP, port))

    try:
        response, _ = udp_socket.recvfrom(1024)
        return response.decode('utf-8')
    except socket.timeout:
        return None
    finally:
        udp_socket.close()


def discover_udp_sequence():
    sequence = []
    for port in range(10000, 11000):  # Assuming ports are within this range
        if str(port).endswith('666'):
            response = send_udp_message(port, "PING")
            if response == "PONG":
                print(f"Port {port} is part of the sequence.")
                sequence.append(port)
                if len(sequence) == 3:  # Assuming the sequence has 3 ports
                    break
    return sequence


def connect_to_tcp_service():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.connect((TCP_SERVER_IP, TCP_PORT))

    try:
        message = tcp_socket.recv(1024).decode('utf-8')
        print(f"Received from TCP server: {message}")
    finally:
        tcp_socket.close()


def main():
    print("Discovering UDP sequence...")
    udp_sequence = discover_udp_sequence()

    if len(udp_sequence) == 3:
        print(f"Sequence discovered: {udp_sequence}")
        print("Sending port knocking sequence...")

        for port in udp_sequence:
            send_udp_message(port, "PING")

        print("Connecting to the TCP service...")
        connect_to_tcp_service()
    else:
        print("Failed to discover the complete UDP sequence.")


if __name__ == "__main__":
    main()
