from scapy.all import sniff, IP, TCP

# Function to process captured packets
def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        if ip_dst == "127.0.0.1":
            print(f"Potential scan detected! Source: {ip_src} -> Destination: {ip_dst}")
            with open("forensic_log.txt", "a") as log_file:
                log_file.write(f"Potential scan detected! Source: {ip_src} -> Destination: {ip_dst}\n")

# Capture only TCP packets
sniff(filter="tcp", prn=packet_callback, store=0)

