import socket
import threading
import struct
import pickle

songList = []
class Command:
    command = ""
    payload = ""

class SocketThread(threading.Thread):
    def __init__(self, socketInstance):
        # 收到connection
        self.mySocket = socketInstance

    def Run(self):
        global songList
        try:
            while (True):
                print("Reading initial length")

                # 客户端发送了两次 第一次发送的是一个4位整数 标识这个命令的总长度，所以预设接受4位
                a = self.mySocket.recv(4)
                print("Wanted 4 bytes got " + str(len(a)) + " bytes")

                #接收之后，用struct模块解析，得到message length
                messageLength = struct.unpack('i', a)[0]
                print("Message Length: ", messageLength)

                # 利用message length，预定义接受的命令长度
                data = self.mySocket.recv(messageLength)

                # 使用pickle加载收到的pickle文件，得到command
                newCommand = pickle.loads(data)
                print("Command is: ", newCommand.command)

                # 使用If判断command内容
                # 利用command内容 新建一个Command对象，并将需要的文件加载进去
                # 最后把这个对象写到pickle里面，然后返回
                if newCommand.command == "List":
                    print("Sending List")
                    replyCommand = Command()
                    replyCommand.command = "List reply"
                    replyCommand.payload = pickle.dumps(songList)

                elif newCommand.command == "Get":
                    print("Sending song")
                    replyCommand = Command()            # Make a new command
                    replyCommand.command = "Song Reply" # Set the command type to Song Reply
                    f = open(newCommand.payload, 'rb')  # Open the file, read it in, and use it as the payload
                    replyCommand.payload = f.read()
                    f.close()

                else:
                    print("Unknown Command")
                    continue

                packedData = pickle.dumps((replyCommand))               # Serialize the class to a binary array
                self.mySocket.sendall(struct.pack("i", len(packedData))) # Length of the message is just the length of the array
                self.mySocket.sendall(packedData)

        except Exception as e:
            print("Closing socket")
            print(e)
            self.mySocket.close()

f = open("songlist.txt")

for line in f:
    songList.append(line.rstrip())
f.close()

# 正常建立监听的过程
host = "127.0.0.0"
port = 12010

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('',port))
serverSocket.listen(1)

print("Listening...")

while True:
    (clientSocket, address) = serverSocket.accept()
    print("Got incoming connection")
    # 不使用持续连接 而是新建多个线程
    newThread = SocketThread(clientSocket)
    newThread.Run()