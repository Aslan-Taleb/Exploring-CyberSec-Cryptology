# SENDER

import socket
import threading

MCAST_GRP =   '224.0.0.127'
MCAST_PORT = 7182
FORMAT = 'utf-8'
SIZE = 1024
DISCONNECTION = "!out"
# 2-hop restriction in network
ttl = 2

socket_server = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM,
                     socket.IPPROTO_UDP)
socket_server.setsockopt(socket.IPPROTO_IP,
                socket.IP_MULTICAST_TTL,
                ttl)

# Function to handle a client's connection
def handle_client(conn, addr):
    username = ""
    print(f"[NEW CONNECTION] {username} connected.")
    connected = True
    while connected:
        message = conn.recv(SIZE).decode(FORMAT)
        if message == DISCONNECTION:
            connected = False
        elif message:    
            print(f"[MESSAGE] {username} said: {message}.") 
    conn.close() 
    print(f"[DISCONNECTION] {username} disconnected.")

def start():
    print(f"[LISTENING] server is listening on {MCAST_GRP}:{MCAST_PORT}")
    socket_server.sendto(b"[CadenaChat] Welcome !  ", (MCAST_GRP, MCAST_PORT))
    try:
        while True:
            # For each connection, we retrieve the connection object and connection information
            conn, addr = socket_server.recvfrom(SIZE)
            # Create a thread to handle the connection and pass it to our handle_client function with the arguments
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
            # We subtract 1 because our server itself is running in a thread
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
    except KeyboardInterrupt:
        print("Arrêt Serveur.")
    
print("[STARTING] server is starting...")
start()