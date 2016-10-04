def Palindrome(left_half):
	return int(str(left_half) + str(left_half)[::-1])

done = False
palindrom = 0
left_half = 997  # наибольший возможный палиндром, произведение 2-х трёхначных числел (999*999=998001) = 997799

while not done:
	palindrom = Palindrome(left_half)
	
	for i in range(999, 99, -1):
		if palindrom / i > 999 or i*i < palindrom:
			break
			
		if palindrom % i == 0:
			done = True
			break
	
	left_half -= 1

print(palindrom)
