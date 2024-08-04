from scapy.all import *

# Function to process each packet
def packet_callback(packet):
    # Check if the packet has IP layer
    if IP in packet:
        ip_layer = packet[IP]
        print(f'New Packet: {ip_layer.src} -> {ip_layer.dst}')
        print(f'Protocol: {ip_layer.proto}')
        
        # Check if the packet has TCP layer
        if TCP in packet:
            tcp_layer = packet[TCP]
            print(f'TCP Packet: {tcp_layer.sport} -> {tcp_layer.dport}')
            print(f'Payload: {bytes(tcp_layer.payload)}')
        
        # Check if the packet has UDP layer
        elif UDP in packet:
            udp_layer = packet[UDP]
            print(f'UDP Packet: {udp_layer.sport} -> {udp_layer.dport}')
            print(f'Payload: {bytes(udp_layer.payload)}')
        
        # Check if the packet has ICMP layer
        elif ICMP in packet:
            icmp_layer = packet[ICMP]
            print(f'ICMP Packet: Type {icmp_layer.type} Code {icmp_layer.code}')
        
        print('-' * 80)

# Start sniffing with a limit on the number of packets and a timeout
packet_limit = 10  # Number of packets to capture
timeout = 30       # Timeout in seconds

print('Starting packet sniffing...')
sniff(prn=packet_callback, store=0, count=packet_limit, timeout=timeout)
print('Packet sniffing completed.')
