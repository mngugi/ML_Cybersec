import ctypes

# Load the shared library into ctypes
lib = ctypes.CDLL('./router_monitor.so')

# Call the monitor_network function
lib.monitor_network()
