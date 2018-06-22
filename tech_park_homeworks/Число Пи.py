c=0
pi=0
n=int(input("введите число: "))
for i in range(1, n+1):
  if(c%2==0):
     pi+=1/(1+2*c)
  else:
     pi-=1/(1+2*c)
  c+=1
print(pi*4)
