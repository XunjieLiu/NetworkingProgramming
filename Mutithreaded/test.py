import threading
from time import *

class myThread(threading.Thread):
	def __init__(self, n):
		super(myThread, self).__init__()
		self.n = n

	def run(self):
		print("Current task: ", self.n)

def music(name):
	for i in range(2):
		print("I am listening to music %s \t %s" % (name, ctime()))
		sleep(1)

def movie(name):
	for i in range(2):
		print("I am watching movies %s \t %s" % (name, ctime()))
		sleep(5)

if __name__ == '__main__':
	'''
	t1 = myThread("Thread 1")
	t2 = myThread("Thread 2")

	t1.start()
	t2.start()
	'''
	'''
	music("California Dreaming")
	movie("Ready Player One")
	print("It is all over.\t\t", ctime())
	'''

	t1 = threading.Thread(target=music("California Dreaming"))
	t2 = threading.Thread(target=movie("Ready Player One"))

	t1.start()
	t2.start()

	print("It is all over.\t\t", ctime())

