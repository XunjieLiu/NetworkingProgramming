import threading

class myThread(threading.Thread):
	def __init__(self, n):
		super(myThread, self).__init__()
		self.n = n

	def run(self):
		print("Current task: ", self.n)

if __name__ == '__main__':
	t1 = myThread("Thread 1")
	t2 = myThread("Thread 2")

	t1.start()
	t2.start()

