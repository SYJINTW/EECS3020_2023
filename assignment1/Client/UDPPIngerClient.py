import socket
import time
from statistics import mean

# Create a UDP socket for client
client = 

# Declare server's IP address and port number
HOST = 
PORT = 

# Declare some variables to track packet loss rate and round trip time
packet_loss = 0
rtt_list = []

# Set the socket's timeout to 1 second

# Ping the server 10 times
print("Ping ", HOST, ":", PORT, "...")
t = 10
for i in range(t):
    to = False
    t1 = 0
    t2 = 0
    try:
        # Record the timestamp before sending the message to server
        t1 = (time.time() * 1000)

        # Send a message to the server
        # Listen to the server for the feedback

        # Record the timestamp after getting server's feedback
        t2 = (time.time() * 1000)
        
    except socket.timeout:
        # If the timeout is reached, skip it.
    
    # Get rtt be minusing t1 and t2
    rtt = t2-t1

    # Print the results
    if(to==False):
        print("PING ", i, rtt)
        rtt_list.append(rtt)
    else:
        packet_loss = packet_loss+1
        print("Request timed out.")


# Calculate the average round trip time and packet loss rate
avg_rtt = mean(rtt_list)
packet_loss_rate = packet_loss / t
# Print the results
print("Result:")
print("Average RTT = " + str(avg_rtt))
print("Packet loss rate = " + str(packet_loss_rate))
print("Closing the socket...")
client.close()
print("Socket closed.")