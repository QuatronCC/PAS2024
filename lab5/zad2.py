import socket
import random

HOST = '127.0.0.1'  
PORT = 2912         

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f"Server started, listening on {HOST}:{PORT}")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    print(f"Secret number: {secret_number}")

    try:
        while True:
            # Receive data from the client
            data = conn.recv(1024).decode('utf-8').strip()
            if not data:
                break

            # Check if the data is a number
            if not data.isdigit():
                response = "Error: Please send a valid number."
            else:
                # Convert the data to an integer
                guess = int(data)

                # Compare the guess with the secret number
                if guess < secret_number:
                    response = "Your guess is too low."
                elif guess > secret_number:
                    response = "Your guess is too high."
                else:
                    response = "Congratulations! You've guessed the number."
                    conn.sendall(response.encode('utf-8'))
                    break

            conn.sendall(response.encode('utf-8'))

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        conn.close()
        print("Connection closed.")

if __name__ == "__main__":
    main()
