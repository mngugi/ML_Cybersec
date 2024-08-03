#Python 3.10.12 (main, Jul 29 2024, 16:56:48) [GCC 11.4.0] on linux
#Type "help", "copyright", "credits" or "license()" for more information.
import socket
import random

def port_scanner(target, ports):
    open_ports = []

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        
        result = sock.connect_ex((target, port))
        if result == 0:
            open_ports.append(port)
        
        sock.close()

    return open_ports

def generate_random_ports(n):
    return random.sample(range(1, 65536), n)

if __name__ == "__main__":
    target = input("Enter the target IP address or hostname: ")
    ports = generate_random_ports(3498)
    print(f"Scanning {len(ports)} ports on {target}...")

    open_ports = port_scanner(target, ports)

    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(port)
    else:
        print("No open ports found.")
