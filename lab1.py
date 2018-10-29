n = 1
m = 6
result = 1
for i in range(m):
	result = result * n
	n = n + 1

print(result)
if(result % 2 == 1):
	print("Boo, odd")
else:
	print('Yay, even')

