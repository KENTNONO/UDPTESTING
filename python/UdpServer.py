import socket

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    PORT = 1060

    s.bind(('localhost', PORT))
    print('Listening for broadcast at ', s.getsockname())

    while True:
        data, address = s.recvfrom(1024)
        print('Server received from {}:{}'.format(address, data.decode('utf-8')))