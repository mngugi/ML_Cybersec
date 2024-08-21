import psutil
import time

def detect_nmap():
    while True:
        for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
            if 'nmap' in proc.info['name'] or 'nmap' in ' '.join(proc.info['cmdline']):
                print(f"Nmap detected! PID: {proc.info['pid']}, Command: {' '.join(proc.info['cmdline'])}")
                with open("forensic_log.txt", "a") as log_file:
                    log_file.write(f"Nmap detected! PID: {proc.info['pid']}, Command: {' '.join(proc.info['cmdline'])}\n")
        time.sleep(1)

detect_nmap()

