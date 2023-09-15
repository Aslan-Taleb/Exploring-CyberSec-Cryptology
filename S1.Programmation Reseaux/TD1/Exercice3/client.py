import socket

# Define IP and PORT
PORT = 5050
# Get the IP address of our computer
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECTION = "!out"

# Create a socket
socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
socket_client.connect(ADDR)
print("Connected to the server")

# Function to send messages to the server
def send(msg):
    message = msg.encode(FORMAT)
    socket_client.send(message)

# Continuously send user input to the server
while True:
    user_input = input()
    send(user_input)
    if user_input == DISCONNECTION:
        print("you have been disconnected")
        break
    

# Close the socket when done
socket_client.close()
