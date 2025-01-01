# Detecting out-of-range network traffic
network_traffic = [100, 50, 2000, 80, 45]  # Packet sizes in bytes
acceptable_range = (40, 1500)  # Normal packet size range

# Check if each packet is within the acceptable range
anomalies = [pkt for pkt in network_traffic if pkt < acceptable_range[0] or pkt > acceptable_range[1]]

print("Anomalies Detected:", anomalies)
