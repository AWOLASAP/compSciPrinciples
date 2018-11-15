def calculator(num1, num2, operator):
	if operator not in ['+', '-', '*', '/']:
		return "Please use one of the four basic operators: +, -, *, /."

	try:
		num1 = int(num1)
		num2 = int(num2)
	except ValueError:
		return "Please enter in a two numbers with an operator in between seperated by spaces."

	if operator == '+': return num1 + num2
	elif operator == '-': return num1 - num2
	elif operator == '*': return num1 * num2
	elif operator == '/':
		if num2 == 0: return "You cannot divide by zero idiot!"
		return num1 / num2

while True:
	equation = input("Give me a simple equation (ex. num1 operator num2): ")
	if equation.lower() in ['quit', 'q', 'goodbye', 'no', 'bye', 'leave',
					 'quit ', 'q ', 'goodbye ', 'no ', 'bye ', 'leave ']:
		break

	split_equation = equation.split(" ")
	
	try:
		test = split_equation[0]
		test2 = split_equation[1]
		test3 = split_equation[2]
	except IndexError:
		print("Use the correct format!")
		continue

	answer = calculator(split_equation[0], split_equation[2], split_equation[1])

	if answer == "Please enter in a two numbers with an operator in between seperated by spaces." \
		or answer == "You cannot divide by zero idiot!" or \
		answer == "Please use one of the four basic operators: +, -, *, /.":
		print(answer)
	else:
		print(equation, '=', answer)
	print()

print("Goodbye!")