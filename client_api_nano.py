import socket
import time

class ClientNano:
	def __init__(self, IP_ADRESS_SERVER, PORT):
		self.IP_ADRESS_SERVER = IP_ADRESS_SERVER
		self.PORT = PORT

	def connect(self):
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		while True:
			try:
				s.connect((self.IP_ADRESS_SERVER,1234))
				msg = s.recv(self.PORT)
				print('xavier on')
				print(msg.decode("utf-8"))
				break
			except:
				print('server xavier off, turn on xavier')
				time.sleep(2)		


"""
IP_ADRESS_SERVER = '192.168.0.51'
PORT = 1024
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

while True:
	try:
		s.connect((IP_ADRESS_SERVER,1234))
		msg = s.recv(PORT)
		print('xavier on')
		print(msg.decode("utf-8"))
		break
	except:
		print('server xavier off, turn on xavier')
		time.sleep(2)
"""
#def receive_info():
