from socket import *

serverPort = 12001
serverSocket = socket()

serverSocket.bind(('', serverPort))

serverSocket.listen(1)
# the parameter specifies the maximum number of queued connection( at least 1)
# 意思是只和一个客户端通信，只和第一个到达的客户端通信，
# 所以不用考虑多线程问题？？？

while True:
    connectionSocket, addr = serverSocket.accept()
    print("incoming connection from: ", addr)

    while True:
        cmd = connectionSocket.recv(1024).decode()

        if cmd == 'upload':
            size = connectionSocket.recv(1024).decode()
            filename = connectionSocket.recv(1024).decode()
            size = int(size)
            print('Reciece size: ', size)
            filecontent = connectionSocket.recv(size)
            f = open(filename, 'wb')
            f.write(filecontent)
            f.close()
        else:
            filename = connectionSocket.recv(1024).decode()

            with open(filename, 'rb') as f:
                clientSocket.sendall(f.read())

        

        # 没有接收到消息的话 断开本次连接
        if not size:
            print('Disconnect!')
            break

connectionSocket.close()