from lib.xavier.server_api_xavier import ServerXavier

IP_ADRESS_SERVER = '127.0.0.1'

if __name__ == '__main__':
    s = ServerXavier(IP_ADRESS_SERVER)
    s.turn_on_server()
