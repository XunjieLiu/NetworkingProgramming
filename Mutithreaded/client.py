import socket
import struct
import pickle

class Command:
    command = ""
    payload = ""

host = "localhost"
port = 4567

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

getCommand = Command()
getCommand.command = "Get"
getCommand.payload = "SongA.mp3"
packedData = pickle.dumps(getCommand)
totalLen = len(packedData)

s.sendall(struct.pack("i", totalLen))
s.sendall(packedData)

replyLen = struct.unpack("i", s.recv(4))[0]
replyData = s.recv(replyLen)
replyCommand = pickle.loads(replyData)

f = open("newSongFile.mp3", "wb")
f.write(replyCommand.payload)

f.close()
s.close()