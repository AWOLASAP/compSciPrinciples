def convert_to_dec(b):
	value, total = 1, 0
	for i in reversed(str(b)):
		if i == '1':
			total += value
		value *= 2
	
	return total
binary = input("Give me an 8-bit binary number: ")
print(convert_to_dec(binary))
