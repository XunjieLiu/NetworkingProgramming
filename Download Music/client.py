import socket
import struct
import pickle

class Command:
    command = ""
    payload = ""

host = "localhost"
port = 4567

# AF_INET表示IPv4网络， SOCK_DGRAM表示TCP协议
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

# List command
# Make a new command and set the command value to list
# note that the list command has no payload, so we don't set it
listCommand = Command()
listCommand.command = "List"

# Serialize the command class instance with pickle
packedData = pickle.dumps(listCommand)

# The total length of the message is just the length of the serialized data
totalLen = len(packedData)

# Send the length of the data, then the data - we have to pack the int into a binary stream
s.sendall(struct.pack("i", totalLen))
s.sendall(packedData)

# First receive the 4 byte header, with tells us how big the data is - we have to unpack the int first
replyLen = struct.unpack("i", s.recv(4))[0]

# Now receive the data
replyData = s.recv(replyLen)

# Use pickle to deserialize the data
replyCommand = pickle.loads(replyData)

# Now we can use it like a normal class....
print("Reply type is:" + replyCommand.command)
print("list is", pickle.loads(replyCommand.payload))

#Todo: Get SongA.mp3 and save it to a file

s.close()
        

