import socket

def send_message():
    # Define the IP and port for the server
    server_ip = "127.0.0.1"
    server_port = 12345
    
    # Create a UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Message to be sent
    message = "Hello, Server!"
    client_socket.sendto(message.encode(), (server_ip, server_port))
    
    # Receive response from the server
    response, server_address = client_socket.recvfrom(1024)
    print(f"Received response from server: {response.decode()}")

if __name__ == "__main__":
    send_message()
