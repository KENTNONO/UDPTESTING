import socket

if __name__ == "__main__":
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    PORT = 1060
    network = 'localhost'
    for i in range(100) :
        s.sendto(f'Client broadcast message!{i}'.encode('utf-8'), (network, PORT))
