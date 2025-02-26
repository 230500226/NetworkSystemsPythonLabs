import socket

def start_server():
    # Define the IP and port for the server
    server_ip = "192.168.56.1"
    server_port = 12345
    
    # Create a UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((server_ip, server_port))
    
    print(f"Server listening on {server_ip}:{server_port}...")
    
    while True:
        # Receive message from the client
        message, client_address = server_socket.recvfrom(1024)
        print(f"Received message from {client_address}: {message.decode()}")
        
        # Optionally, send a response back to the client
        response = "Message received"
        server_socket.sendto(response.encode(), client_address)

if __name__ == "__main__":
    start_server()
