import struct
import pickle

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def show(self):
		print("Name: ", self.name, " Age: ", self.age)

a1 = 'apple'
b1 = {1: 'one', 2: 'two', 3:'three'}
c1 = ['fee', 'fre', 'fum', 'foe']
f1 = open('temp.pkl', 'wb')
pickle.dump(a1, f1, True)
pickle.dump(b1, f1, True)
pickle.dump(c1, f1, True)
f1.close()


'''
a = 20
b = 400

str = struct.pack("i", a)
print(str)
print(len(str))
'''
