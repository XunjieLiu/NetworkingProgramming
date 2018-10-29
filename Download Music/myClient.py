import socket
import struct
import pickle
import os

class Command:
    command = ""
    payload = ""

host = "10.8.196.242"
port = 12010

# AF_INET表示IPv4网络， SOCK_DGRAM表示TCP协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# List command
# Make a new command and set the command value to list
# note that the list command has no payload, so we don't set it
# Command对象纯粹是为了传输数据的 类似于数据包
listCommand = Command()

comm = input("Input your command: ")

listCommand.command = comm

if comm == 'Get':
    listCommand.payload = 'SongA.mp3'

# Serialize the command class instance with pickle
# 把数据包装到pickle类型的文件里面
packedData = pickle.dumps(listCommand)

# The total length of the message is just the length of the serialized data
# 获取pickle文件的长度（大小）
totalLen = len(packedData)

# Send the length of the data, then the data - we have to pack the int into a binary stream
# i代表Integer， 用struct包把整数“4”打包成一个4位的二进制数
s.sendall(struct.pack("i", totalLen)) # 第一个sendall把文件大小传过去
s.sendall(packedData) # 第二个把pickle文件传过去

# First receive the 4 byte header, with tells us how big the data is - we have to unpack the int first
replyLen = struct.unpack("i", s.recv(4))[0]

# Now receive the data
replyData = s.recv(replyLen)

# Use pickle to deserialize the data
replyCommand = pickle.loads(replyData)

if comm == 'List':
    # Now we can use it like a normal class....
    print("Reply type is:" + replyCommand.command)
    print("list is", pickle.loads(replyCommand.payload))
elif comm == 'Get':
    # 新建一个文件夹 用来存储MP3文件
    folder = 'songs'

    if not folder:
        os.makedirs('songs')
    else:
        continue

    mp3File = 'songs\\' + 'SongA.mp3'
    with open(mp3File, 'wb') as output:
        output.write(replyCommand.payload)

    print('Get songA and saved')
else:
    print('Unknown command')    


#Todo: Get SongA.mp3 and save it to a file

s.close()
        
'''
def mkdir(path):

    folder = os.path.exists(path)

    if not folder:
        os.makedirs(path)
    else:
        print('There is a folder')

file = 'songs'
mkdir(file)

current = os.getcwd()
name = file + '\\songlist.txt'

with open(name, 'w') as f:
    f.write("Hello!")
'''