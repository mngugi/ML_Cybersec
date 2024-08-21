// File: network_monitor.c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/ip.h>
#include <linux/if_ether.h>
#include <unistd.h>

// Function to monitor network traffic
void monitor_network(const char *interface) {
    int sock_raw;
    struct sockaddr saddr;
    unsigned char *buffer = (unsigned char *)malloc(65536);
    socklen_t saddr_len = sizeof(saddr);

    // Create a raw socket
    sock_raw = socket(AF_PACKET, SOCK_RAW, htons(ETH_P_IP));
    if (sock_raw < 0) {
        perror("Socket Error");
        return;
    }

    while (1) {
        // Receive a packet
        int data_size = recvfrom(sock_raw, buffer, 65536, 0, &saddr, &saddr_len);
        if (data_size < 0) {
            perror("Recvfrom error");
            return;
        }

        // Process the packet (basic packet inspection)
        struct iphdr *ip_header = (struct iphdr *)(buffer + sizeof(struct ethhdr));
        struct in_addr src, dest;
        src.s_addr = ip_header->saddr;
        dest.s_addr = ip_header->daddr;

        printf("Source IP: %s\n", inet_ntoa(src));
        printf("Destination IP: %s\n", inet_ntoa(dest));

        if (strcmp(inet_ntoa(dest), "127.0.0.1") == 0) {
            printf("Warning: Detected traffic to 127.0.0.1\n");
        }
    }

    close(sock_raw);
    free(buffer);
}
