from socket import *

serverPort = 12001
serverSocket = socket()

serverSocket.bind(('', serverPort))

serverSocket.listen(1)
# the parameter specifies the maximum number of queued connection( at least 1)
# 意思是只和一个客户端通信，只和第一个到达的客户端通信，
# 所以不用考虑多线程问题？？？
print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    print("incoming connection from: ", addr)

    while True:
        sentence = connectionSocket.recv(1024).decode()
        print('Reciece message: ', sentence)
        capitalizationSentence = sentence.upper()
        connectionSocket.send(capitalizationSentence.encode())

        # 没有接收到消息的话 断开本次连接
        if not sentence:
            print('Disconnect!')
            break

connectionSocket.close()
    