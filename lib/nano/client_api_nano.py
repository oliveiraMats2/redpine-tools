import socket
import time


class ClientNano:
    def __init__(self, ip_address_server, port):
        self.ip_address_server = ip_address_server
        self.port = port

    def connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while True:
            try:
                s.connect((self.ip_address_server, 1234))
                msg = s.recv(self.port)
                print('xavier on')
                print(msg.decode("utf-8"))
                break
            except:
                print('server xavier off, turn on xavier')
                time.sleep(2)
