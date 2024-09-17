#!/bin/bash

# Author: Peter Mwangi Ngugi
# A bash script to install a Security lab on Pop!_OS

LOGFILE="/var/log/security_lab_install.log"
echo "Installation started at $(date)" | tee -a "$LOGFILE"

# Ensure script is run as root
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root."
  exit 1
fi

# Update system packages
echo "Updating system packages..." | tee -a "$LOGFILE"
apt update && apt upgrade -y >> "$LOGFILE" 2>&1

# Function to install a package
install_package() {
  local package=$1
  local description=$2
  echo "Installing $package: $description" | tee -a "$LOGFILE"
  
  if apt install -y "$package" >> "$LOGFILE" 2>&1; then
    echo "$package installed successfully." | tee -a "$LOGFILE"
  else
    echo "Error installing $package. Check $LOGFILE for details." | tee -a "$LOGFILE"
    return 1
  fi
}

# Function to handle manual installation from source
install_from_source() {
  local repo_url=$1
  local folder_name=$2
  echo "Attempting to install $folder_name from source..." | tee -a "$LOGFILE"
  
  apt install -y git build-essential libssl-dev >> "$LOGFILE" 2>&1
  
  git clone "$repo_url" "$folder_name" >> "$LOGFILE" 2>&1
  cd "$folder_name"
  
  if make && sudo make install >> "$LOGFILE" 2>&1; then
    echo "$folder_name installed successfully from source." | tee -a "$LOGFILE"
  else
    echo "Error installing $folder_name from source. Check $LOGFILE for details." | tee -a "$LOGFILE"
    return 1
  fi

  cd ..
  rm -rf "$folder_name"
}

# Installing security tools
declare -A PACKAGES=(
  [etherape]="Graphical network monitor"
  [ettercap-graphical]="Man-in-the-middle attack tool"
  [wireshark]="Network traffic analyzer"
  [medusa]="Brute-force login cracker"
  [nmap]="Network discovery tool"
  [scap-workbench]="SCAP scanner"
  [skipfish]="Web security reconnaissance tool"
  [yersinia]="Network protocol weakness exploiter"
  [hydra]="Powerful login cracker"
  [aircrack-ng]="Wireless network security toolset"
  [john]="Password cracker"
  [nikto]="Web server scanner"
  [metasploit-framework]="Penetration testing framework"
  [ncrack]="Network authentication cracker"
  [gobuster]="Directory/file/DNS subdomain brute-forcer"
  [openvas]="Vulnerability scanner"
  [lynis]="Security auditing tool"
  [tcpdump]="Network packet analyzer"
)

# Install security packages
for package in "${!PACKAGES[@]}"; do
  install_package "$package" "${PACKAGES[$package]}"
done

# SQLNinja installation: Install via apt or from source
install_package sqlninja "SQL Injection testing tool" || {
  echo "Attempting manual installation of sqlninja from source..." | tee -a "$LOGFILE"
  install_from_source "https://github.com/sqlninja/sqlninja.git" "sqlninja"
}

# Skipfish manual installation if apt fails
install_package skipfish "Web security reconnaissance tool" || {
  echo "Attempting manual installation of skipfish from source..." | tee -a "$LOGFILE"
  apt install -y libssl-dev libidn11-dev libpcre3-dev >> "$LOGFILE" 2>&1
  git clone https://github.com/spinkham/skipfish.git >> "$LOGFILE" 2>&1
  cd skipfish
  make >> "$LOGFILE" 2>&1
  sudo make install >> "$LOGFILE" 2>&1
  if [ $? -eq 0 ]; then
    echo "Skipfish installed successfully from source." | tee -a "$LOGFILE"
  else
    echo "Error installing Skipfish from source." | tee -a "$LOGFILE"
  fi
  cd ..
  rm -rf skipfish
}

# BurpSuite Installation (Manual download)
echo "Installing BurpSuite..." | tee -a "$LOGFILE"
BURP_URL="https://portswigger.net/burp/releases/download?product=community&version=2023.7.1&type=linux"
wget -O burpsuite.sh "$BURP_URL" >> "$LOGFILE" 2>&1
chmod +x burpsuite.sh
./burpsuite.sh >> "$LOGFILE" 2>&1
if [ $? -eq 0 ]; then
  echo "BurpSuite installed successfully." | tee -a "$LOGFILE"
else
  echo "Error installing BurpSuite. Check $LOGFILE for details." | tee -a "$LOGFILE"
fi

# Configure Wireshark (Add user to group)
echo "Configuring Wireshark..." | tee -a "$LOGFILE"
if usermod -aG wireshark "$SUDO_USER"; then
  echo "Wireshark configured successfully. Please log out and log back in for group changes to take effect." | tee -a "$LOGFILE"
else
  echo "Failed to configure Wireshark." | tee -a "$LOGFILE"
fi

# Install Metasploit
echo "Installing Metasploit..." | tee -a "$LOGFILE"
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate | bash >> "$LOGFILE" 2>&1
if msfdb init; then
  echo "Metasploit database initialized successfully." | tee -a "$LOGFILE"
else
  echo "Error initializing Metasploit database." | tee -a "$LOGFILE"
fi

echo "All installations and configurations are complete. Check $LOGFILE for details."

