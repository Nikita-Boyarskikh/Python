arr = [0,1]
n = 20
debug = 0

def NOK(a, b):
	if(a>b):
		x = m = a
	else:
		x = m = b
	while(x%a + x%b > 0):
		x += m
	return x
	
for a in range(1, n):
	arr.append(a + 1)
	arr[a + 1] = NOK(arr[a], a + 1)
	
print(arr[n - 1])
