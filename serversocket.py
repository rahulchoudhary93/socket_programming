import socket

host = "localhost"
port = 7771

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serversocket:
    print("Starting socket server..")
    serversocket.bind((host, port))
    serversocket.listen(2)
    clientsocket, address = serversocket.accept()

    with clientsocket:
        print("Received connection from {}".format(address))
        while True:
            data = clientsocket.recv(1024)
            if not data:
                break
            clientsocket.send(b"Yes! Your message received.")
            # clientsocket.close() is not required as it has been used with the context-manager
