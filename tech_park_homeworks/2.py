n = 4000000

x1 = 1
x2 = sum = 2
x = x1 + x2

while x < n:
	x1 = x2
	x2 = x
	x = x1 + x2
	if x % 2 == 0:
		sum += x

print(sum)
