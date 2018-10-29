import socket
import threading
import struct
import pickle

songList = []
class Command:
    command = ""
    payload = ""

# This is my thread class.  It inherits from threading.Thread....

class SocketThread(threading.Thread):
    # you need to override the constructor, but make sure to call the base constructor
    def __init__(self, socketInstance):
        threading.Thread.__init__(self)   # make sure you do this or it won't work...
        self.mySocket = socketInstance

    # this is what gets run when you call start()
    def run(self):
        try:
            while (True):
                print("Reading initial length")
                a = self.mySocket.recv(4)
                print("Wanted 4 bytes got " + str(len(a)) + " bytes")

                messageLength = struct.unpack('i', a)[0]
                print("Message Length: ", messageLength)

                data = self.mySocket.recv(messageLength)

                newCommand = pickle.loads(data)
                print("Command is: ", newCommand.command)

                if newCommand.command == "Get":
                    print("Sending song")
                    replyCommand = Command()            # Make a new command
                    replyCommand.command = "Song Reply" # Set the command type to Song Reply
                    f = open(newCommand.payload, 'rb')  # Open the file, read it in, and use it as the payload
                    print("Sending file: ", newCommand.payload)
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

#start our main....

host = "localhost"
port = 4567

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((host,port))
serverSocket.listen(1)

print("Listening...")

while True:
    (clientSocket, address) = serverSocket.accept()
    print("Got incoming connection")
    newThread = SocketThread(clientSocket)        # make a new instance of our thread class to handle requests
    newThread.start()                             # start the thread running....
    

    
