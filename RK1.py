import math

text = 'он прислушался здание театра молчало\
 римский понял что он давно один во всём втором этаже и детский неодолимый\
 страх овладел им при этой мысли он без содрогания не мог подумать о том\
 что ему придётся сейчас идти одному по пустым коридорам и спускаться по лестнице'

def f(x):
	if x==0:
		return 0;
	return x/len(text)*math.log(x/len(text), 2)

summa = f(44) + f(text.count('ё')) + f(text.count('й'))
print('_ : ', -f(44))
print('ё : ', -f(text.count('ё')))
print('й : ', -f(text.count('й')))
for i in range(ord('а'), ord('я')):
	print(chr(i), ' : ', -f(text.count(chr(i))))
	summa += f(text.count(chr(i)))
print('sum : ', -summa)
