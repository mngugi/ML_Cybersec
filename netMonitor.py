import ctypes

# Load the shared library
network_monitor = ctypes.CDLL('./network_monitor.so')

# Specify the argument types
network_monitor.monitor_network.argtypes = [ctypes.c_char_p]

# Call the network monitoring function with the desired interface
def start_monitoring(interface="eth0"):
    network_monitor.monitor_network(interface.encode('utf-8'))

# Example usage
if __name__ == "__main__":
    start_monitoring("eth0")  # Replace "eth0" with your actual network interface

