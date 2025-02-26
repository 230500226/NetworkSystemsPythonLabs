import socket

def send_message():
    # Define the IP and port for the server
    server_ip = "127.0.0.1"
    server_port = 12345
    
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Connect to the server
    client_socket.connect((server_ip, server_port))
    
    # Message to be sent
    message = "Hello, Server!"
    client_socket.sendall(message.encode())
    
    # Receive response from the server
    response = client_socket.recv(1024).decode()  # Corrected from recvfrom to recv
    print(f"Received response from server: {response}")
    
    # Clean up the socket
    client_socket.close()

if __name__ == "__main__":
    send_message()
