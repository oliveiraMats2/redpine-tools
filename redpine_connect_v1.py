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
        elapsed = 1
        init = time.time()
        while 1:
            if elapsed % temp == 0:
                if self.connection():
                    break
            elapsed = int(time.time() - init)

    def verify_connect(self, url="http://192.168.0.1", timeout=15):  # gateway--url
        try:
            request = requests.get(url, timeout=timeout)
            return True

        except (requests.ConnectionError, requests.Timeout) as exception:
            return False

    def find_network(self):
        if self.verify_network():
            print("network found")
        else:
            while 1:
                print("network not found")
                if self.verify_network():
                    break
            time.sleep(2)

            print("--find network!--:", elapsed, "s")

    def periodic_re_connect(self):
        init = time.time()

        while 1:  # infinite loop
            if self.verify_connect() == True:
                print("rede conectada, ta tranquilo!")
            else:
                self.periodic_check()
            time.sleep(5)

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
            self.periodic_re_connect()


if __name__ == "__main__":
    name = "NET_2G0EE7DC"
    password = "4F0EE7DC"
    interface = "enp3s0f1"
    execute = AutoRedpine(name, password, interface)
    execute.run()
