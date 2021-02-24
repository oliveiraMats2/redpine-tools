import socket


class ServerXavier:
    def __init__(self, ip_address_server):
        self.ip_address_server = ip_address_server

    def turn_on_server(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.ip_address_server, 1234))
        s.listen(5)

        client_socket, address = s.accept()
        print(f"Connection from {address} has been established")
        # send text
        client_socket.send(bytes("Welcome to the server!", "utf-8"))
        s.close()
