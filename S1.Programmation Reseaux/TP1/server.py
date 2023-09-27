import socket
import threading
import re
from bonus import *


# Define IP and PORT
PORT = 8080
# Get the IP address of our computer
SERVER = socket.gethostbyname(socket.gethostname())
# Tuple with the IP address and the port number
ADDR = (SERVER, PORT)
# We use HEADER to get the length of the message to know how much data we're going to receive
FORMAT = 'utf-8'
SIZE = 1024
DISCONNECTION = "!out"



# Create a socket
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#OPTIMIZATION liberer le port qu'utilise le socket toute suite apres
#Cette option permet de réutiliser immédiatement une adresse IP et un numéro de port locaux lorsque la socket se termine
socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
# Now we have to bind the socket to the IP address and port
socket_server.bind(ADDR)

# Function to handle a client's connection
def handle_client(conn, addr):
    username = UsernameGenerator()
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

# Function to start the server
def start():
    # Here we listen for incoming connections and start the server
    socket_server.listen(socket.SOMAXCONN)
    print(f"[LISTENING] server is listening on {SERVER}:{PORT}")
    while True:
        # For each connection, we retrieve the connection object and connection information
        conn, addr = socket_server.accept()
        # Create a thread to handle the connection and pass it to our handle_client function with the arguments
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        # We subtract 1 because our server itself is running in a thread
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print("[STARTING] server is starting...")
start()








