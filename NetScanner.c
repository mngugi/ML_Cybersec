#include <pcap.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <arpa/inet.h>
#include <netinet/ip.h>
#include <netinet/tcp.h>

void packet_handler(u_char *user, const struct pcap_pkthdr *pkthdr, const u_char *packet) {
    struct ip *ip_header = (struct ip *)(packet + 14); // Skip Ethernet header
    struct tcphdr *tcp_header = (struct tcphdr *)(packet + 14 + ip_header->ip_hl * 4);

    printf("%-20s %-20s %-10d %-10d\n",
           inet_ntoa(ip_header->ip_src),
           inet_ntoa(ip_header->ip_dst),
           ntohs(tcp_header->th_sport),
           ntohs(tcp_header->th_dport));
}

int main() {
    char errbuf[PCAP_ERRBUF_SIZE];
    pcap_t *handle;
    pcap_if_t *alldevs, *d;

    // Find all devices
    if (pcap_findalldevs(&alldevs, errbuf) == -1) {
        fprintf(stderr, "Error finding devices: %s\n", errbuf);
        return 1;
    }

    // Use the first device found
    if (alldevs == NULL) {
        fprintf(stderr, "No devices found\n");
        return 1;
    }

    d = alldevs;
    printf("Using device: %s\n", d->name);

    // Open the device for capturing
    handle = pcap_open_live(d->name, BUFSIZ, 1, 1000, errbuf);
    if (handle == NULL) {
        fprintf(stderr, "Couldn't open device %s: %s\n", d->name, errbuf);
        pcap_freealldevs(alldevs);
        return 1;
    }

    // Print table header
    printf("%-20s %-20s %-10s %-10s\n", "Source IP", "Destination IP", "Src Port", "Dst Port");
    printf("%-20s %-20s %-10s %-10s\n", "---------", "-------------", "--------", "--------");

    // Capture packets
    pcap_loop(handle, 10, packet_handler, NULL);

    // Close the handle
    pcap_close(handle);
    pcap_freealldevs(alldevs);

    return 0;
}

