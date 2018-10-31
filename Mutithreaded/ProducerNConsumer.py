import threading
import time
import queue

'''
使用threading，只需要从threading.Thread继承，并重写__init__()和run方()法
threading提供了一个锁：lock = threading.Lock()，调用锁的acquire()和release()方法可以使线程获得和释放锁

需要注意的是，Python有一个GIL（Global Interpreter Lock）机制，
任何线程在运行之前必须获取这个全局锁才能执行，每当执行完100条字节码，全局锁才会释放，切换到其他线程执行

所以Python中的多线程不能利用多核计算机的优势，
无论有多少个核，同一时间只有一个线程能得到全局锁，只有一个线程能够运行

当执行IO密集型任务时，比如Python爬虫，大部分时间都用在了等待返回的socket数据上，
CPU此时是完全闲置的，这种情况下采用多线程较好

计算密集的任务，比如图形计算的时候，大部分时间CPU都用于计算
使用多进程才可以加速（多线程共享的是同一块CPU资源）

'''

queue = queue.Queue(10) # Queue是一个线程安全的容器


class Producer(threading.Thread):
	# 构造方法
	def __init__(self, name):
		super().__init__()
		self.name = name

	def run(self):
		while 1:
			queue.put(0)
			print("Producer %s creates a product" % self.name)
			print("Producer %s put a product into queue" % self.name)

class Consumer(threading.Thread):
	def __init__(self, name):
		super().__init__()
		self.name = name

	def run(self):
		while 1:
			queue.get()
			print("Consumer %s get a product" % self.name)

def test():
	p1 = Producer("Producer 1")
	c1 = Consumer("Consumer 1")

	p1.start()
	c1.start()


if __name__ == '__main__':
	test()