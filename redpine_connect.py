import os
import time
import requests


class AutoRedpine:
    def __init__(self, server_name, password, interface_name):
        self.server_name = server_name
        self.password = password
        self.interface_name = interface_name

    def verify_network(self):
        command = """sudo iwlist wlp2s0 scan | grep -ioE 'ssid:"(.*{}.*)'"""
        result = os.popen(command.format(self.server_name))
        result = list(result)
        ssid_list = [item.lstrip('SSID:').strip('"\n') for item in result]
        if len(result) == 0:
            return False
        else:
            return True

    def connection(self):
        try:
            x = os.system("nmcli d wifi connect {} password {}".format(self.server_name, self.password))

            if x == 2560:
                return False

            if x == 32512:
                print("senha incorreta")
                time.sleep(5)
                return False

            return True
        except:
            pass

    def periodic_check(self, temp=5):
        if self.verify_network():
            print('placa conectada no check periodic')
        else:
            print('placa desconectada')
            self.connection()

    def find_network(self):
        if self.verify_network():#<-----verificou se existe a network
            print("network found")
        else:
            while 1:
                print("network not found")
                if self.verify_network():
                    break
            time.sleep(2)

            print("--find network!--:")

    def periodic_re_connect(self):
        while 1:  # infinite loop
            if self.verify_network() == True:
                print("rede conectada, ta tranquilo!")
            else:
                self.periodic_check()
            time.sleep(1)

    def run(self):
        # -----begin--------
        self.find_network()
        # ---try connect----
        if self.connection():
            print("connected")
            self.periodic_re_connect()

        else:
            print("first connection failed")
            self.periodic_check()
            


if __name__ == "__main__":
    name = "GalaxyS10"
    password = "bajc3169"
    interface = "enp3s0f1"
    execute = AutoRedpine(name, password, interface)
    execute.run()
