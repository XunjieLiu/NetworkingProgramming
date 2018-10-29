from socket import *
import os

serverNme = '10.8.196.242'
serverPort = 12001

# AF_INET表示ipv4网络， SOCK_STREAM表示TCP协议
clientSocket = socket(AF_INET, SOCK_STREAM)
# 这一行是与UDP协议不一样的地方，UDP协议直接调用sendto方法发送报文，但是TCP协议需要先进行连接
clientSocket.connect((serverNme, serverPort))

while True:
	# 接下来的和UDP基本一样了
	cmd = input('Input your command: ')
	if sentence == '':
		print('Exit!')
		break
	else if cmd == 'upload':
		filenme = input('Input the filename: ')
		size = input('Input the size: ')
		size = os.path.getsize(filename)

		clientSocket.sendall(size) # 发送文件大小
		with open(filename, 'rb') as f:
			clientSocket.sendall(f.read())
			

	else if cmd == 'download':
		modifiedSentence = clientSocket.recv(1024)


clientSocket.close()
print('Connection closed')

'''
with open('hello.txt', 'rb') as f:
	print(f.read())
'''