# SENDER

import socket

group = '224.1.1.1'
port = 5004
FORMAT = 'utf-8'
# 2-hop restriction in network
ttl = 2

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM,
                     socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP,
                socket.IP_MULTICAST_TTL,
                ttl)
def send(msg):
    message = msg.encode(FORMAT)
    sock.sendto(message, (group, port))
    
print("[ON] SENDER Connected")
try:
    while True:
        message = input("Your Message : ")
        send(message)
except KeyboardInterrupt:
    print("[OFF] SENDER Disconnected")
finally:
    sock.close()