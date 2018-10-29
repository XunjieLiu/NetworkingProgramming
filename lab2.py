def search(value, list):
	length = len(list)

	for i in range(length):
		if value == list[i]:
			print('search value found')
			return i 

	print('not found')
	return length 

sample = [1, 3, 4, 5, 7, 11]
empty = []

print(search(2, sample))