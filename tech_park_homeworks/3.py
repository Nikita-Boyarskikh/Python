from math import sqrt as sq

n = 600851475143

x = y = 1
max = sq(n)

while x + 2 <= max:
	x += 2
	
	if n % x == 0:
		sqrt = sq(x)
		i = 1
		F = False
		while i + 2 <= sqrt:
			i += 2
			if x % i == 0:
				F = True
				break
		if not F:
			y = x

if y == 1:
	y = n

print(y)
