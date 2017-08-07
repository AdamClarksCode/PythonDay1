def AddMultiplyOrZero(x, y, sumThem):
	if x == 0:
		return y
	elif y == 0:
		return x
	elif sumThem == True:
		return x+y 
	else:
		return x*y
for i in range(0, 10):
	print(AddMultiplyOrZero(i, 2, False))
listOfInts =  range(0, 10)
print(AddMultiplyOrZero(listOfInts[0], listOfInts[2], False))
for num in listOfInts:
	print(listOfInts[num])
toMultiply = []
for x in range(0, 10):
	toMultiply = toMultiply + [x]
	print(x)
for y in toMultiply:
	toMultiply[y] = toMultiply[y] * 10
	print(toMultiply[y])


