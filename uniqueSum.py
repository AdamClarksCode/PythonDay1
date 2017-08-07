def UniqueSum(x, y, z):
	if x == y and x == z:
		return 0
	elif x == y and x != z:
		return z
	elif x == z and x != y:
		return y
	elif z == y and z != x:
		return x
	else:
		return x+y+z
print(UniqueSum(3,3,3))
print(UniqueSum(3,3,1))
print(UniqueSum(3,2,3))
print(UniqueSum(4,3,3))
print(UniqueSum(1,2,3))
