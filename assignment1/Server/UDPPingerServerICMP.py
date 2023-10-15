import random
import socket
import struct

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)
serverSocket.setsockopt(socket.SOL_IP, socket.IP_HDRINCL, 1)
# TODO: Assign IP address and port number to socket
HOST = 
PORT = 
serverSocket.bind((HOST, PORT))

print('server start at: %s:%s' % (HOST, PORT))
print('wait for connection...')

while True:
    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)
    icmp_header = message[20:28]
    type, code, checksum, ID, sequence = struct.unpack('bbHHh', icmp_header)
    print('recvfrom ' + str(address[0]), ", type: [" + str(type) + "], code: [" + str(code) + "], "\
                   + "ID:[" + str(ID) + "], sequence number = [" + str(sequence) + "]")
