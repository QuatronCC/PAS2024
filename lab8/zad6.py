import socket

# Adres i port serwera IMAP
HOST = '127.0.0.1'
PORT = 143

# Symulowane wiadomości e-mail
email_messages = [
    b"From: pasinf2017@infumcs.edu\r\nTo: recipient@example.com\r\nSubject: Test Message 1\r\n\r\nThis is a test message 1.\r\n",
    b"From: pasinf2017@infumcs.edu\r\nTo: recipient@example.com\r\nSubject: Test Message 2\r\n\r\nThis is a test message 2.\r\n",
    b"From: pasinf2017@infumcs.edu\r\nTo: recipient@example.com\r\nSubject: Test Message 3\r\n\r\nThis is a test message 3.\r\n"
]

def handle_client_connection(client_socket):
    while True:
        # Odbierz dane od klienta
        request = client_socket.recv(4096).decode('utf-8').strip()

        if request == 'LOGIN username password':
            client_socket.sendall(b'OK LOGIN completed.\r\n')
        elif request == 'SELECT INBOX':
            client_socket.sendall(b'OK SELECT completed.\r\n')
        elif request == 'FETCH 1 BODY[]':
            client_socket.sendall(email_messages[0])
        elif request == 'FETCH 2 BODY[]':
            client_socket.sendall(email_messages[1])
        elif request == 'FETCH 3 BODY[]':
            client_socket.sendall(email_messages[2])
        elif request == 'LOGOUT':
            client_socket.sendall(b'OK LOGOUT completed.\r\n')
            break
        else:
            client_socket.sendall(b'NO Unknown command.\r\n')

def start_imap_server():
    # Utwórz gniazdo serwera
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    print(f"IMAP server listening on {HOST}:{PORT}")

    while True:
        # Akceptuj połączenia przychodzące
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr[0]}:{addr[1]}")

        # Obsłuż połączenie z klientem
        handle_client_connection(client_socket)

        # Zamknij gniazdo klienta
        client_socket.close()

if __name__ == "__main__":
    start_imap_server()
