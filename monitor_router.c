#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/ip.h>
#include <linux/if_ether.h>
#include <unistd.h>
#include <netdb.h>

// Function to resolve IP address to a domain name
void resolve_ip_to_name(char *ip_address, char *resolved_name, size_t len) {
    struct sockaddr_in sa;
    sa.sin_family = AF_INET;
    sa.sin_addr.s_addr = inet_addr(ip_address);

    if (getnameinfo((struct sockaddr*)&sa, sizeof(sa), resolved_name, len, NULL, 0, 0) != 0) {
        strncpy(resolved_name, "Unknown", len);
    }
}

// Function to print the IP header details with resolved names
void print_ip_header(struct iphdr *ip_header) {
    struct in_addr src, dest;
    src.s_addr = ip_header->saddr;
    dest.s_addr = ip_header->daddr;

    char src_ip[INET_ADDRSTRLEN];
    char dest_ip[INET_ADDRSTRLEN];
    inet_ntop(AF_INET, &(src.s_addr), src_ip, INET_ADDRSTRLEN);
    inet_ntop(AF_INET, &(dest.s_addr), dest_ip, INET_ADDRSTRLEN);

    char src_name[NI_MAXHOST];
    char dest_name[NI_MAXHOST];
    resolve_ip_to_name(src_ip, src_name, sizeof(src_name));
    resolve_ip_to_name(dest_ip, dest_name, sizeof(dest_name));

    printf("IP Header Information:\n");
    printf("   |-Source IP        : %s (%s)\n", src_ip, src_name);
    printf("   |-Destination IP   : %s (%s)\n", dest_ip, dest_name);
    printf("   |-Protocol         : %d\n", (unsigned int)ip_header->protocol);
    printf("   |-Packet Length    : %d\n", ntohs(ip_header->tot_len));
}

// Function to monitor the network
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

        // Process the IP packet
        struct iphdr *ip_header = (struct iphdr *)(buffer + sizeof(struct ethhdr));
        print_ip_header(ip_header);
    }

    close(sock_raw);
    free(buffer);
}
