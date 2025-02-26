import socket

def start_server():
    # Define the IP and port for the server
    server_ip = "192.168.56.1"
    server_port = 12345
    
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(1)
    
    print(f"Server listening on {server_ip}:{server_port}...")
    
    while True:
        # Accept a connection from the client
        connection, client_address = server_socket.accept()
        try:
            print(f"Connection from {client_address}")
            
            # Receive message from the client
            message = connection.recv(1024).decode()
            print(f"Received message: {message}")
            
            # Optionally, send a response back to the client
            response = "Message received"
            connection.sendall(response.encode())
        
        finally:
            # Clean up the connection
            connection.close()

if __name__ == "__main__":
    start_server()
