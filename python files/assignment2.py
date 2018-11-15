
def assignment2():
	name = input("What is your name? ")
	subject = input("What subject are you studying? ")

	print("""Hello %s!!! Welcome to my first Python program. 
Yow will do very well in %s if you work hard!""" % (name, subject))

	num1, num2 = int(input("Give me a number: ")), int(input("Give me another one: "))
	
	print("Sum:", num1 + num2, "Difference:", num1 - num2, "Product:", num1 * num2, 
			"Quotient:", num1 / num2, "Remainder:", num1 % num2)

	print('Thank you for using my program!')

if __name__ == '__main__':
	assignment2()