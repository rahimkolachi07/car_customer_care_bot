import socket
from gemini.gemini import g_model

# Define host and port
HOST = '127.0.0.1'
PORT = 12345

# Create socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(1)

print('Waiting for a connection...')

# Accept incoming connection
conn, addr = server_socket.accept()
print('Connected by', addr)

while True:
    try:
        # Receive data from the client
        data = conn.recv(1024)
        if not data:
            break
        
        print('AutoBot:', data.decode())
        response_text = g_model(data.decode())

        # Respond to the client
        message = response_text
        conn.sendall(message.encode())
    except KeyboardInterrupt:
        break

# Close the connection
conn.close()
