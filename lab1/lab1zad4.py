import socket

def get_hostname(ip):
    try:
        hostname = socket.gethostbyaddr(ip)
        print(f"The hostname for IP address {ip} is: {hostname[0]}")
    except socket.herror:
        print("Unable to resolve hostname for the given IP address.")

if __name__ == "__main__":
    user_ip = input("Enter an IP address: ")
    get_hostname(user_ip)
