#PCC Assignment 6
n = int(input("Give me a number: "))
m = int(input("Give me another number: "))

if m < n:
	n, m = m, n

answer1 = 0
answer2 = 0

if n % 2 == 0:
	n_even = n
	n_odd = n + 1
else:
	n_even = n + 1
	n_odd = n

for i in range(n_even, m+1, 2):
	answer1 += i

print("All the even numbers between %s and %s are: " % (n, m), answer1)

for i in range(n_odd, m+1, 2):
	answer2 += i 

print("All the odd numbers between %s and %s are: " % (n, m), answer2)

exit = input("Thank You!")