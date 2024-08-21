from ctypes import *

# Load the shared library (replace './nmap_wrapper.so' with './nmap_wrapper.dll' on Windows)
nmap_lib = CDLL('./nmap_wrapper.so')

# Specify argument types for the run_nmap_script function
nmap_lib.run_nmap_script.argtypes = [c_char_p, c_char_p]

# Function to wrap around the C function
def run_nmap(target, script):
    nmap_lib.run_nmap_script(target.encode('utf-8'), script.encode('utf-8'))

# Example usage
if __name__ == "__main__":
    target = "127.0.0.1"  # Replace with the target IP or hostname
    script = "default"    # Replace with the desired Nmap script
    
    print(f"Running Nmap script '{script}' on target '{target}'...")
    run_nmap(target, script)

