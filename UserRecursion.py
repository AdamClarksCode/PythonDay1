toMultiply = []
z = int(input("Please enter a number: "))
for x in range(0, z):
	toMultiply = toMultiply + [x]
	print(x)
for y in toMultiply:
	toMultiply[y] = toMultiply[y] * 10
	print(toMultiply[y])