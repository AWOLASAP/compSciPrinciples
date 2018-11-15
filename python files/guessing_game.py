from random import randint

def guess_game():
	answer = randint(0, 1000000000000000000000000000000000000)
	guess = int(input("Guess my number: "))
	while guess != answer:
		if guess > answer:
			print("Guess lower: ")
		else:
			print("Guess Higher: ")
		guess = int(input())

	print("You got it!!! It was", answer)

guess_game()
