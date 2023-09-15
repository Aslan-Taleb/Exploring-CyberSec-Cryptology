import socket
import threading
import re

# Define IP and PORT
PORT = 5050
# Get the IP address of our computer
SERVER = socket.gethostbyname(socket.gethostname())
# Tuple with the IP address and the port number
ADDR = (SERVER, PORT)
# We use HEADER to get the length of the message to know how much data we're going to receive
FORMAT = 'utf-8'
SIZE = 1024
DISCONNECTION = "!out"

# Regular expression pattern to match email addresses
pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(fr|com)"

# Create a socket
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Now we have to bind the socket to the IP address and port
socket_server.bind(ADDR)

# Function to handle a client's connection
def handle_client(conn, addr):
    username = ""
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        message = conn.recv(SIZE).decode(FORMAT)
        if message == DISCONNECTION:
            connected = False
        if re.search(pattern, message):
            username = message.split('@')[0]
            print(f"[ACCESS] Username: {username}")
        elif message:
            if username:
                print(f"[MESSAGE] {username} said: {message}.")
            else:
                   print(f"[MESSAGE] {addr} said: {message}.") 
    conn.close() 
    print(f"[DISCONNECTION] {addr} disconnected.")

# Function to start the server
def start():
    # Here we listen for incoming connections and start the server
    socket_server.listen()
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
