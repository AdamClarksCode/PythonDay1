def tooHot(temperature, isSummer):
	if isSummer == True and temperature >= 60 and temperature <= 100:
		return True
	elif isSummer == False and temperature >= 60 and temperature <= 90:
		return True
	else:
		return False
print(tooHot(91, True))
print(tooHot(91, False))
print(tooHot(61, False))
