import os
import subprocess
import platform


def get_gateway_ip():
    # This command works for both Windows and Unix-like systems
    if platform.system() == "Windows":
        command = "ipconfig"
    else:
        command = "route -n"

    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    output = result.stdout

    # Parse the output to find the gateway
    if platform.system() == "Windows":
        for line in output.splitlines():
            if "Default Gateway" in line:
                gateway_ip = line.split()[-1]
                return gateway_ip
    else:
        for line in output.splitlines():
            if line.startswith('0.0.0.0'):
                gateway_ip = line.split()[1]
                return gateway_ip

    return None


def ping_sweep(gateway_ip):
    network_prefix = '.'.join(gateway_ip.split('.')[:-1])
    active_ips = []

    # Ping each address in the subnet
    for i in range(1, 255):
        ip = f"{network_prefix}.{i}"
        response = os.system(f"ping -{'n' if platform.system() == 'Windows' else 'c'} 1 -w 1000 {ip} > /dev/null 2>&1")

        if response == 0:
            active_ips.append(ip)

    return active_ips


gateway_ip = get_gateway_ip()
if gateway_ip:
    print(f"Gateway IP: {gateway_ip}")
    active_ips = ping_sweep(gateway_ip)
    print("Active IP Addresses:")
    for ip in active_ips:
        print(ip)
else:
    print("Unable to determine the gateway IP address.")
