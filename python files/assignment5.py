#PCC Assignment 5
boy_scores = []
girl_scores = []
def compareBoyAndGirl(boy, score):
	if boy:
		boy_scores.append(int(score))
	else:
		girl_scores.append(int(score))

def average(input_list):
	total = 0
	for i in input_list:
		total += int(i) 
	return total / len(input_list)

prompt = 'Boy (b), Girl (g), quit(q)'

while True:
	command = input(prompt).lower()
	if command == 'q':
		break
	if command == 'b':
		score = input("Boy Score: ")
		compareBoyAndGirl(True, score)
	elif command == 'g':
		score = input("Girl Score: ")
		compareBoyAndGirl(False, score)


print('Boy Score Average =', average(boy_scores))
print('Girl Score Average =', average(girl_scores))