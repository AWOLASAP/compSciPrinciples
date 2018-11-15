def calculate_bmi():
	height_in_fi = input("How tall are you?(feet/inches): ")
	height = height_in_fi.split(' ')
	height_in_inch = (int(height[0]) * 12) + int(height[1])

	weight = input("How much do you weigh?(lbs): ")

	BMI = (int(weight) * 702) / (int(height_in_inch) ** 2)

	print("Your BMI is", BMI)

if __name__ == '__main__':
	calculate_bmi()