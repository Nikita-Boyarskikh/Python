n=int(input('Введите число:'))

a = [i for i in range(2, n+1)]

i=0
while(i<len(a)-1):
	j=i+1
	while(j<len(a)):
		if(a[j]%a[i]==0):
			del(a[j])
		j+=1
	i+=1

print('Список всех простых чисел до заданного числа {}: {}'.format(n, ", ".join([str(i) for i in a])))
