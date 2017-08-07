from functools import partial
def Multiply(x, y):
	return x*y
doubleIt = partial(Multiply, 2)
trippleIt = partial(Multiply, 3)
print(doubleIt(2))
print(trippleIt(2))
