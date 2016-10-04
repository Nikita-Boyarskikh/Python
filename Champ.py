from random import randint as ran
from sys import argv as teams

del(teams[0])
number = len(teams)
results = [[] * number] * number

c=0
for i in teams:
    print (i)
    c+=1
    results[c, 1]=i

for i in range(number):
    for j in range(number):
        if i != j:
            results[i][j] = ran(0,10)
        else:
            results[i][j] = 0

for i in range(number):
    for j in range(number):
        table[i][2] += results[i][j]
        table[3][j] += results[i][j]

print (table)
print (results)
