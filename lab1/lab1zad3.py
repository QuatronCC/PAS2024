import ipaddress

def check_ip_address(ip):
    try:
        ipaddress.ip_address(ip)
        print("The given IP address is valid.")
    except ValueError:
        print("Invalid IP address.")

if __name__ == "__main__":
    user_ip = input("Enter an IP address: ")
    check_ip_address(user_ip)
