import socket  # Import socket module

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create TCP socket using IPv4

client.connect(("127.0.0.1", 5555))  # Connect to server at localhost and port 5555

message = input("Please enter the message that you want to send to the server: ")  # Get user input

client.send(message.encode("utf-8"))  # Send message to server

print("Server is sending you a message...")  # Notify user
print(client.recv(1024).decode("utf-8"))  # Receive and print server response

# client.close()  # Close the connection
