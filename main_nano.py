from lib.nano.client_api_nano import ClientNano

IP_ADRESS_SERVER = '127.0.0.1'
PORT = 1234

if __name__ == '__main__':
    s = ClientNano(IP_ADRESS_SERVER, PORT)
    s.connect()
