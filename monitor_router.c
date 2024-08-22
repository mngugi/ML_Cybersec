#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/ip.h>
#include <linux/if_ether.h>
#include <unistd.h>

// Ensure the function is properly exported
void monitor_network() {
    int sock_raw;
    struct sockaddr saddr;
    unsigned char *buffer = (unsigned char *)malloc(65536);
    socklen_t saddr_len = sizeof(saddr);

    // Create a raw socket
    sock_raw = socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ALL));
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

        // Process the packet (for simplicity, just print some data)
        struct iphdr *ip_header = (struct iphdr *)(buffer + sizeof(struct ethhdr));
        struct in_addr src, dest;
        src.s_addr = ip_header->saddr;
        dest.s_addr = ip_header->daddr;

        printf("Source IP: %s\n", inet_ntoa(src));
        printf("Destination IP: %s\n", inet_ntoa(dest));
    }

    close(sock_raw);
    free(buffer);
}
