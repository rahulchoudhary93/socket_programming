import socket

host = "localhost"
port = 7771

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientsocket:
    clientsocket.connect((host, port))
    clientsocket.sendall(b"Is this the socket server?")
    data = clientsocket.recv(1024)

print("Received: ", repr(data))