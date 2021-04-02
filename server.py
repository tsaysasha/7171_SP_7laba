from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
import threading


class SocketServer:
    def __init__(self, address, socket_type):
        self.address = address
        self.socket_type = socket_type
        self.socket = None

    def udp(self):
        while True:
            print('Server is wait UDP connection')
            data, address = self.socket.recvfrom(1024)
            print(f'Response from {address} - {data.decode()}')
            self.socket.sendto(f"Hi i am a UDP server".encode(), address)

    def tcp(self):
        self.socket.listen()
        while True:
            print('Server is wait TCP connection')
            client, address = self.socket.accept()
            data = client.recv(1024)
            print(f"Response from {address}: {data.decode()}")
            client.send(f'Hi i am a TCP server'.encode())

    def listen(self):
        with socket(AF_INET, self.socket_type) as socket_inst:
            self.socket = socket_inst
            self.socket.bind(self.address)
            if self.socket_type == SOCK_DGRAM:
                self.udp()
            elif self.socket_type == SOCK_STREAM:
                self.tcp()


if __name__ == '__main__':
    tcp = SocketServer(('localhost', 54514), SOCK_STREAM)
    udp = SocketServer(('localhost', 51312), SOCK_DGRAM)

    tcp = threading.Thread(target=tcp.listen)
    udp = threading.Thread(target=udp.listen)

    tcp.start()
    udp.start()
