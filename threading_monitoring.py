from scapy.all import sniff, IP
import threading
import psutil

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        if ip_dst == "127.0.0.1":
            print(f"Potential scan detected! Source: {ip_src} -> Destination: {ip_dst}")
            with open("forensic_log.txt", "a") as log_file:
                log_file.write(f"Potential scan detected! Source: {ip_src} -> Destination: {ip_dst}\n")

def detect_nmap():
    while True:
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            if 'nmap' in proc.info['name'] or 'nmap' in ' '.join(proc.info['cmdline']):
                print(f"Nmap detected! PID: {proc.info['pid']}, Command: {' '.join(proc.info['cmdline'])}")
                with open("forensic_log.txt", "a") as log_file:
                    log_file.write(f"Nmap detected! PID: {proc.info['pid']}, Command: {' '.join(proc.info['cmdline'])}\n")

# Start network monitoring in a separate thread
network_thread = threading.Thread(target=sniff, kwargs={'filter': 'tcp', 'prn': packet_callback, 'store': 0})
network_thread.start()

# Start Nmap detection
detect_nmap()

