import socket
import time
from threading import Thread
import struct
import os
ICMP_ECHO_REQUEST = 8 # platform specific

def do_checksum(source_string):
    # Verify the packet integritity
    sum = 0
    max_count = (len(source_string)/2)*2
    count = 0
    while count < max_count:

        val = source_string[count + 1]*256 + source_string[count]                   
        sum = sum + val
        sum = sum & 0xffffffff 
        count = count + 2

    if max_count<len(source_string):
        sum = sum + ord(source_string[len(source_string) - 1])
        sum = sum & 0xffffffff 

    sum = (sum >> 16)  +  (sum & 0xffff)
    sum = sum + (sum >> 16)
    answer = ~sum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer


def create_ICMPpacket(type, code, ID, sequence):
    # Create a dummy heder with a 0 checksum.
    my_checksum = 0
    header = struct.pack("bbHHh", type, code, my_checksum, ID, sequence)

    # Fill the ICMP's data field with some dummy information
    bytes_In_double = struct.calcsize("d")
    data = (192 - bytes_In_double) * "Q"
    data = struct.pack("d", time.time()) + bytes(data.encode('utf-8'))

    # Get the checksum on the data and the dummy header.
    my_checksum = do_checksum(header + data)
    header = struct.pack("bbHHh", type, code, socket.htons(my_checksum), ID, sequence)
    packet = header + data
    return packet

def send_ping(sock, ID, dst, sequence):
    # Send a ping (echo request ICMP packet) to the target host
    
    return

def listen_ICMPreply(sock, packet_size):
    # Listen to the ICMP echo reply message and get its type, code, checksum, ID, sequence
    
    return type, code, checksum, ID, sequence

def main():
    HOST = 
    PORT = 34434
    dst = (HOST, PORT)
    
    # Create an ICMP socket, and set its timeout to 1 second.
    ICMP_socket =  

    my_ID = os.getpid() & 0xFFFF
    attempts = 10
    print("Ping", HOST, ":", PORT, "...")
    for i in range(attempts):
        try:
            send_ping(sock=ICMP_socket, ID=my_ID, dst=dst, sequence=i)
            type, code, checksum, ID, sequence = listen_ICMPreply(sock=ICMP_socket, packet_size=1508)
            print("packet:[" + str(i) + "], type: [" + str(type) + "], code: [" + str(code) + "], "\
                   + "ID:[" + str(ID) + "], sequence number = [" + str(sequence) + "]")

        except socket.timeout:
            print("Request timeout.")
            pass
        
    print("Closing the socket...")
    ICMP_socket.close()
    print("Socket closed")

if __name__ == "__main__":
    main()