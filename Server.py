import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = ''
port = 8888

s.bind((host,port))

print('Waiting for connection...\n')

#open file
file = open('Details.txt','a') 
while True:

	data, addr = s.recvfrom(1024)

	if data == b'end':
		False
		print('\nDetail Record')
		file = open('Details.txt','r')
		print(file.read())
		time.sleep(1)
		print('Connection ended...\n')
		time.sleep(1)
		break

	if data != b'end' and  data != b'':
		print('Connected to ', addr)


file.close()
s.close()

