
number_list = []
def getInput():
	try:
		inp = int(input("Give me a number > "))
	except ValueError:
		print("Please give me an integer.")
		getInput()

	return inp

def run():
	while True:
		number = getInput()
		if number == 0:
			break
		else:
			number_list.append()

	print(sum(number_list))


run()
