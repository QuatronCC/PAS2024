import socket

def get_ip(hostname):
    try:
        ip_address = socket.gethostbyname(hostname)
        print(f"The IP address for hostname {hostname} is: {ip_address}")
    except socket.gaierror:
        print("Unable to resolve IP address for the given hostname.")

if __name__ == "__main__":
    user_hostname = input("Enter a hostname: ")
    get_ip(user_hostname)
