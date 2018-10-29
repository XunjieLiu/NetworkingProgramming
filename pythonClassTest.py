class Employee:
	'This is docnment statement, this class is for test' # 说明文档

	# empCount类似于Java里面的static变量，不随实例而改变
	empCount = 0

	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empCount += 1
		print("New employee created!")

	def displayCount(self):
		print("Totla number of employee is %d", empCount)

	def displayEmployee(self):
		print("His name is: ", self.name, " His salary is: ", self.salary)

	def prt(self):
		print(self)
		print(self.__class__)

class Parent:
	parentAttr = 100

	def __init__(self):
		print("This is parent class")

	def parentMethod(self):
		print("This is parent method")

	def setAttr(self, attr):
		Parent.parentAttr = attr
		# patentAttr是一个静态变量 不可以用self

	def getAttr(self):
		print("This is parent attr: ", parentAttr)

class Child(Parent):# 定义子类，从Parent继承
    def __init__(self):
    	print("This is child class")

    def childMethod(self):
    	print("This is child method")





'''
Xunjie = Employee("Xunjie", 30000)
John = Employee("John", 20000)
Adeline = Employee("Adeline", 500000)

print(Xunjie.empCount)
print(Xunjie.__dict__) # 返回基本信息，类的属性
print(Xunjie.__doc__) # 返回这个类的说明文档
print(Xunjie.__class__) # 返回类名
'''

