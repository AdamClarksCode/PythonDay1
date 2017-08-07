def AddThem(x, y):
	return x+y
print(AddThem(1,2))
def AddOrMultiply(x, y, sumThem):
	if sumThem == True:
		return x+y 
	else:
		return x*y 
print(AddOrMultiply(3, 3, True))
print(AddOrMultiply(3, 3, False))
def AddMultiplyOrZero(x, y, sumThem):
	if x == 0:
		return y
	elif y == 0:
		return x
	elif sumThem == True:
		return x+y 
	else:
		return x*y 
print(AddMultiplyOrZero(0, 3, True))
print(AddMultiplyOrZero(6, 0, False))