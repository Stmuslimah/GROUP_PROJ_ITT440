import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = ''
port = 8888


print('Waiting for connection...\n')

#open file
file = open('Details.txt','a') 
while True:

	data , addr = s.recvfrom(1024)

	print('Connected to ', addr)

	file_data = data
	file.write(str(file_data) + '\n')



file.close()
s.close()
