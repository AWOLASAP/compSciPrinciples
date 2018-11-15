last = 0
current = 1
tag = 1
while current < 1000:
	last, current = current, current + last
	tag += 1
print(tag)