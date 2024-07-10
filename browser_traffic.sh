#!/bin/bash

# Define variables
INTERFACE="eth0"  # Change this to your network interface
DURATION=60       # Duration to capture traffic in seconds
OUTPUT_FILE="vivaldi_traffic.pcap"
DISPLAY_FILE="vivaldi_traffic.txt"

# Check if tcpdump is installed
if ! command -v tcpdump &> /dev/null
then
    echo "tcpdump could not be found. Please install it and run the script again."
    exit 1
fi

# Start capturing traffic
echo "Capturing network traffic for Vivaldi browser on interface $INTERFACE for $DURATION seconds..."
sudo tcpdump -i $INTERFACE -w $OUTPUT_FILE port 80 or port 443 &

# Wait for the specified duration
sleep $DURATION

# Stop capturing traffic
sudo pkill tcpdump
echo "Capture complete. Traffic saved to $OUTPUT_FILE."

# Convert pcap file to readable text
echo "Converting pcap file to readable text..."
sudo tcpdump -r $OUTPUT_FILE > $DISPLAY_FILE
echo "Conversion complete. Traffic saved to $DISPLAY_FILE."

# Display the captured traffic
echo "Displaying captured traffic:"
cat $DISPLAY_FILE

