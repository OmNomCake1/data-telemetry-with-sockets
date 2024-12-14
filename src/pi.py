# Raspberry pi TCP/UDP connection which sends data to laptop
# the PI actually accpets the connection from the laptop so it technically is the server
# I chose this because my PI has a static IP but the laptop doesn't so it is easier to connect to.
# Written by Ryan Wong

import socket
import signal
import sys

def send_data(connection_socket):
    while(True):
        try:
            data = input("Enter message: ").encode()
            connection_socket.sendall(data)
        except:
            break        
    # close socket after finished
    connection_socket.close()
    
def client_shutdown(sig, frame):
    print("Server shutting down...")
    server_socket.close()
    sys.exit(0)
    
# listen on static DW ASUS private IP and port 12000
host = "192.168.50.39"
port = 12000
address = (host, port)

# make and bind TCP welcome socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(address)
print(f"Server listening on {host}:{port}...")

# accept connection
server_socket.listen()
server_socket.settimeout(0.5)
while (True):
    signal.signal(signal.SIGINT, client_shutdown)
    try:
        connection_socket, client_address = server_socket.accept()
        print(f"Successfully connected with {client_address[0]}:{client_address[1]}")  
        
        # once successfully connected, send data (this is BLOCKING (cannot accept anymore connections))
        send_data(connection_socket)
        break
    except socket.timeout as e:
        pass
    except Exception as e:
        print("Could not accept socket connection")
        print(e)
        sys.exit(1)

server_socket.close()
        

