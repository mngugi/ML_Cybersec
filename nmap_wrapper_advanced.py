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
    
    # 1: Run an advanced script to scan for HTTP vulnerabilities
    script = "http-vuln-*"    # Replace with the desired Nmap script
    options = "-p 80,443"  # Scan only the HTTP and HTTPS ports
    print(f"Running Nmap script '{script}' on target '{target}' with options '{options}'...")
    run_nmap(target, script, options)
    
    print(f"Running Nmap script '{script}' on target '{target}'...")
    run_nmap(target, script)

    # 2: Run a script to detect SSH host keys
    script = "ssh-hostkey"
    options = "-p 22"  # Scan only the SSH port
    print(f"Running Nmap script '{script}' on target '{target}' with options '{options}'...")
    run_nmap(target, script, options)

    # 3: Run a script to discover SMB vulnerabilities
    script = "smb-vuln-*"
    options = "-p 139,445"  # Scan SMB ports
    print(f"Running Nmap script '{script}' on target '{target}' with options '{options}'...")
    run_nmap(target, script, options)

    # 4: Run a script to enumerate DNS servers
    script = "dns-enum"
    options = "-p 53"  # Scan DNS port
    print(f"Running Nmap script '{script}' on target '{target}' with options '{options}'...")
    run_nmap(target, script, options)
