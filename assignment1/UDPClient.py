# Group: Tyler Ostinato, Cole Leo

import socket
import time

# Create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Look for packets on the localhost
server_addr = ('localhost', 12000)
sock.settimeout(1)

elapsed_times = []

for i in range(1, 11):
    start_time = time.time()
    message = "Packet " + str(i)

    try:
        sent = sock.sendto(message, server_addr)
        print("Sending " + message + " | " + time.ctime())
        data, server = sock.recvfrom(1024)
        print("ECHOED " + data)
        end_time = time.time()
        elapsed = end_time - start_time
        elapsed_times.append(elapsed)
        print("RTT: " + str(elapsed) + " seconds\n")

    except socket.timeout:
        print("Packet " + str(i) + " Timed Out\n")

# Close the socket
sock.close()

### Print Max, Min, and AVG RTT of packets ###

# Add elapsed times and div by length of the list
print("AVG RTT: " + str(sum(elapsed_times)/len(elapsed_times)) + " seconds")

# Get MAX of the list
print("Max RTT: " + str(max(elapsed_times)) + " seconds")

# Get MIN of the list
print("Min RTT: " + str(min(elapsed_times)) + " seconds")

# Packet loss rate
print("Packet loss rate: " + str(10*(10-len(elapsed_times))) + "%")