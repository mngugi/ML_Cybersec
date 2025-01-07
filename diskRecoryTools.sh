#!/bin/bash

# Disk Recovery Automation Script

echo "====================================="
echo "     Disk Recovery Automation Tool"
echo "====================================="

# Function to check if a tool is installed
check_tool() {
    if ! command -v "$1" &> /dev/null; then
        echo "Error: $1 is not installed. Installing it now..."
        sudo dnf install -y "$1"
    else
        echo "$1 is already installed."
    fi
}

# Function for TestDisk
run_testdisk() {
    echo "Launching TestDisk for partition recovery..."
    sudo testdisk
}

# Function for PhotoRec
run_photorec() {
    echo "Launching PhotoRec for file recovery..."
    sudo photorec
}

# Function for ddrescue
run_ddrescue() {
    echo "Enter the damaged disk (e.g., /dev/sdX):"
    read -r source_disk
    echo "Enter the output image file path (e.g., /path/to/output.img):"
    read -r output_img
    echo "Enter the log file path (e.g., /path/to/logfile.log):"
    read -r log_file
    echo "Running ddrescue..."
    sudo ddrescue "$source_disk" "$output_img" "$log_file"
}

# Function for extundelete
run_extundelete() {
    echo "Enter the ext3/ext4 partition (e.g., /dev/sdX):"
    read -r partition
    echo "Unmounting the partition..."
    sudo umount "$partition"
    echo "Enter the directory to restore files to (e.g., /path/to/recover):"
    read -r restore_dir
    echo "Recovering deleted files with extundelete..."
    sudo extundelete "$partition" --restore-all --output-dir "$restore_dir"
}

# Function for Foremost
run_foremost() {
    echo "Enter the disk/partition to scan (e.g., /dev/sdX):"
    read -r partition
    echo "Enter the directory to save recovered files (e.g., /path/to/output):"
    read -r output_dir
    echo "Recovering files with Foremost..."
    sudo foremost -i "$partition" -o "$output_dir"
}

# Function for Scalpel
run_scalpel() {
    echo "Enter the disk/partition to scan (e.g., /dev/sdX):"
    read -r partition
    echo "Enter the directory to save recovered files (e.g., /path/to/output):"
    read -r output_dir
    echo "Recovering files with Scalpel..."
    sudo scalpel "$partition" -o "$output_dir"
}

# Main Menu
while true; do
    echo "Choose a recovery tool to run:"
    echo "1. TestDisk (Partition Recovery)"
    echo "2. PhotoRec (File Recovery)"
    echo "3. ddrescue (Disk Cloning and Recovery)"
    echo "4. extundelete (File Recovery for ext3/ext4)"
    echo "5. Foremost (File Recovery - File Carving)"
    echo "6. Scalpel (File Recovery - File Carving)"
    echo "7. Exit"
    read -rp "Enter your choice (1-7): " choice

    case $choice in
        1)
            check_tool "testdisk"
            run_testdisk
            ;;
        2)
            check_tool "testdisk"  # PhotoRec is part of TestDisk
            run_photorec
            ;;
        3)
            check_tool "ddrescue"
            run_ddrescue
            ;;
        4)
            check_tool "extundelete"
            run_extundelete
            ;;
        5)
            check_tool "foremost"
            run_foremost
            ;;
        6)
            check_tool "scalpel"
            run_scalpel
            ;;
        7)
            echo "Exiting the script. Goodbye!"
            exit 0
            ;;
        *)
            echo "Invalid choice. Please enter a number between 1 and 7."
            ;;
    esac
done

