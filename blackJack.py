def BlackJack(x, y):
	if x > 21 and y > 21:
		return 0
	elif x > y and x < 22:
		return x
	else: 
		return y
print(BlackJack(18,21))
print(BlackJack(20,18))
print(BlackJack(22,22))
