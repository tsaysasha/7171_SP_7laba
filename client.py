from socket import AF_INET, SOCK_STREAM, socket, SOCK_DGRAM

SOCK_TYPE = {
    SOCK_DGRAM: "UDP",
    SOCK_STREAM: "TCP"
}


class SocketClient:
    def __init__(self, address, socket_type):
        self.sock_type = socket_type
        self.address = address
        self.socket_inst: socket = None
        self.connection()

    def connection(self):
        self.socket_inst = socket(AF_INET, self.sock_type)
        if self.sock_type == SOCK_STREAM:
            self.socket_inst.connect(self.address)

    def sent_message(self, sock_message):
        if self.sock_type == SOCK_DGRAM:
            self.socket_inst.sendto(sock_message.encode(), self.address)
        elif self.sock_type == SOCK_STREAM:
            self.socket_inst.send(sock_message.encode())

    def response_message(self):
        data = self.socket_inst.recv(1024)
        print(f"Response from {SOCK_TYPE[self.sock_type]}: {data.decode()}")


if __name__ == '__main__':
    # client_sock_type = SOCK_DGRAM
    client_sock_type = SOCK_STREAM
    address = ("localhost", 54514)
    # address = ("localhost", 51312)
    client = SocketClient(address, client_sock_type)
    client.sent_message(f"Hello i am a {SOCK_TYPE[client_sock_type]} client")
    client.response_message()
