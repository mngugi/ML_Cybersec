from ctypes import *

# Load the shared library (replace './nmap_wrapper_advanced.so' with './nmap_wrapper_advanced.dll' on Windows)
nmap_lib = CDLL('./nmap_wrapper_advanced.so')

# Specify argument types for the run_nmap_script function
nmap_lib.run_nmap_script.argtypes = [c_char_p, c_char_p, c_char_p]

# Function to wrap around the C function
def run_nmap(target, script, options=""):
    nmap_lib.run_nmap_script(target.encode('utf-8'), script.encode('utf-8'), options.encode('utf-8'))

# Example usage with more advanced Nmap scripts
if __name__ == "__main__":
    target = "192.168.100.8"  # Replace with the target IP or hostname

    # Scan all 65,535 ports with an advanced Nmap script
    script = "http-vuln-*"
    options = "-p 1-65535 -T4 -T5 -v"  # Scanning all ports with verbose output
    print(f"Running Nmap script '{script}' on target '{target}' with options '{options}'...")
    run_nmap(target, script, options)

