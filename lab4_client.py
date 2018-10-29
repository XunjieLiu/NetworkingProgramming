from socket import *
import os

serverNme = '10.8.124.169'
serverPort = 12001

# AF_INET表示ipv4网络， SOCK_STREAM表示TCP协议
clientSocket = socket(AF_INET, SOCK_STREAM)
# 这一行是与UDP协议不一样的地方，UDP协议直接调用sendto方法发送报文，但是TCP协议需要先进行连接
clientSocket.connect((serverNme, serverPort))

while True:
    # 接下来的和UDP基本一样了
    cmd = input('Input your command: ')
    clientSocket.sendall(cmd.encode())

    if cmd == 'upload':
        filename = input('Input the filename: ')
        size = os.path.getsize(filename)
        size = str(size)

        clientSocket.sendall(size.encode()) # 发送文件大小
        clientSocket.sendall(filename.encode())
        with open(filename, 'rb') as f:
            clientSocket.sendall(f.read())
    else:
        continue
        '''
        filename = input('Input the filename: ')
        clientSocket.sendall(filename.encode())

        clientSocket.recv(1024)
        '''

clientSocket.close()
print('Connection closed')

'''
with open('hello.txt', 'rb') as f:
    print(f.read())
'''