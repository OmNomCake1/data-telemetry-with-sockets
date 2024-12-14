# laptop TCP/UDP connection which connects to the pi server, then accpets data
# Written by Ryan Wong

import socket
import sys

# pi_host = "192.168.50.39"
pi_host = "localhost"
pi_port = 12000
pi_address = (pi_host, pi_port)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(pi_address)
print(f"Connected to server {pi_host}:{pi_port}")

while(True):
    try:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(f"Received \"{data}\" from {pi_host}:{pi_port}")
    except KeyboardInterrupt:
        print("Closing client...")
        break

client_socket.close()

        
    
