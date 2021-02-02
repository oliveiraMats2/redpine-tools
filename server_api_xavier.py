import socket

class ServerXavier:
	def __init__(self, IP_ADRESS_SERVER):
		self.IP_ADRESS_SERVER = IP_ADRESS_SERVER

	def turn_on_server(self):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.bind((self.IP_ADRESS_SERVER,1234))
		s.listen(5)

		clientsocket, address =  s.accept()
		print("Connection from {address} has been established")
		#send text
		clientsocket.send(bytes("Welcome to the server!","utf-8"))
		s.close()



"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('192.168.0.51',1234))


s.listen(5)

clientsocket, address =  s.accept()
print("Connection from {address} has been established")
#send text
clientsocket.send(bytes("Welcome to the server!","utf-8"))

"""
