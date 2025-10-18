import socket  # Import socket module

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create TCP socket using IPv4

server.bind(("127.0.0.1", 5555))  # Bind socket to localhost and port 5555

server.listen(5)  # Start listening for incoming connections
print("Server is listening on port 5555...")

client, address = server.accept()  # Accept a connection from a client
print(f"Connection established with {address}")

message = client.recv(1024).decode("utf-8")  # Receive message from client
print(f"Client says: {message}")

client.send("Hello, this is server".encode("utf-8"))  # Send response to client

# client.close()  # Close the connection
