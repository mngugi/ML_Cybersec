import ctypes

# Load the shared library into ctypes
lib = ctypes.CDLL('./router_monitor.so')

# Set the function signature (optional but recommended)
lib.monitor_network.restype = None

# Call the monitor_network function
lib.monitor_network()
