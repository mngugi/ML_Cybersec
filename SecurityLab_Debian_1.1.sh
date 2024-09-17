#!/bin/bash

# Author: Peter Mwangi Ngugi
# This is a bash script program to install a Security lab on Pop!_OS

# Ensure script is run with superuser privileges
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root or use sudo for package installations."
  exit 1
fi

# Trap to handle script interruption
trap "echo 'Script interrupted. Cleaning up...'; exit 1" SIGINT SIGTERM

# Log file for recording errors
LOGFILE="/var/log/security_lab_install.log"
echo "Starting installation..." | tee -a "$LOGFILE"
echo "Installation started at $(date)" | tee -a "$LOGFILE"

# Update system packages
echo "Updating system packages..." | tee -a "$LOGFILE"
apt update && apt upgrade -y >> "$LOGFILE" 2>&1
if [ $? -ne 0 ]; then
  echo "System update failed. Check $LOGFILE for details." | tee -a "$LOGFILE"
  exit 1
fi

# Function to install a package
install_package() {
  local package=$1
  local description=$2
  echo "Installing $package: $description" | tee -a "$LOGFILE"
  
  if apt install -y "$package" >> "$LOGFILE" 2>&1; then
    echo "$package installed successfully." | tee -a "$LOGFILE"
  else
    echo "Error installing $package. Check $LOGFILE for details." | tee -a "$LOGFILE"
    exit 1
  fi
}

# Install necessary security tools
echo "Installing security packages..." | tee -a "$LOGFILE"

declare -A PACKAGES=(
  [etherape]="Graphical network monitor"
  [ettercap-graphical]="Suite for man-in-the-middle attacks"
  [wireshark]="Network traffic analyzer"
  [medusa]="Login brute-forcer"
  [nmap]="Network discovery and security auditing tool"
  [scap-workbench]="SCAP scanner with GUI"
  [skipfish]="Active web application security reconnaissance tool"
  [sqlninja]="SQL Injection vulnerability testing tool"
  [yersinia]="Exploit weaknesses in network protocols"
  [hydra]="Login cracker supporting various protocols"
  [aircrack-ng]="Wireless network security toolset"
  [john]="Password cracker"
  [nikto]="Web server scanner"
  [ncrack]="Network authentication cracker"
  [burpsuite]="Web vulnerability scanning tool"
  [hashcat]="GPU-based password cracking tool"
  [lynis]="Security auditing tool"
  [tcpdump]="Network packet analyzer"
  [gobuster]="Brute-forcer for directories, files, and DNS subdomains"
  [openvas]="Vulnerability scanner"
)

# Loop through packages and install each one
for package in "${!PACKAGES[@]}"; do
  install_package "$package" "${PACKAGES[$package]}"
done

# Install additional dependencies for pwntools
echo "Installing additional dependencies for pwntools..." | tee -a "$LOGFILE"
apt install -y python3 python3-pip python3-dev git libssl-dev libffi-dev build-essential >> "$LOGFILE" 2>&1
if [ $? -ne 0 ]; then
  echo "Failed to install dependencies. Check $LOGFILE for details." | tee -a "$LOGFILE"
  exit 1
fi

# Upgrade pip and install pwntools
python3 -m pip install --upgrade pip >> "$LOGFILE" 2>&1
python3 -m pip install --upgrade pwntools >> "$LOGFILE" 2>&1
if [ $? -ne 0 ]; then
  echo "Failed to install pwntools. Check $LOGFILE for details." | tee -a "$LOGFILE"
  exit 1
fi

# ---- METASPLOIT INSTALLATION WITHOUT ROOT ISSUES ----

# Install Metasploit using the Metasploit installer
echo "Installing Metasploit..." | tee -a "$LOGFILE"
METASPLOIT_INSTALLER_URL="https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate"
curl -sSL "$METASPLOIT_INSTALLER_URL" | bash >> "$LOGFILE" 2>&1

if [ $? -ne 0 ]; then
  echo "Failed to install Metasploit. Check $LOGFILE for details." | tee -a "$LOGFILE"
  exit 1
fi

# Set up Metasploit database as a non-root user
echo "Setting up Metasploit database..." | tee -a "$LOGFILE"
if sudo -u "$SUDO_USER" msfdb init >> "$LOGFILE" 2>&1; then
  echo "Metasploit database initialized successfully." | tee -a "$LOGFILE"
else
  echo "Failed to initialize Metasploit database. Check $LOGFILE for details." | tee -a "$LOGFILE"
  exit 1
fi

# Post-installation configuration for Wireshark
echo "Configuring Wireshark..." | tee -a "$LOGFILE"
if usermod -aG wireshark "$SUDO_USER" >> "$LOGFILE" 2>&1; then
  echo "Wireshark configured successfully. Please log out and log back in for group changes to take effect." | tee -a "$LOGFILE"
else
  echo "Failed to configure Wireshark. Check $LOGFILE for details." | tee -a "$LOGFILE"
fi

echo "All installations and configurations are complete. Check $LOGFILE for any errors." | tee -a "$LOGFILE"
echo "Installation completed at $(date)" | tee -a "$LOGFILE"

# End of script

