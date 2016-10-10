# Игра Найди Дратути)

import random as rand

def a(a):
     arr=[]
     for d in a:
             arr.append(chr(ord(d)+1))
     return ''.join(arr)
 
def b(a):
     arr=[]
     for d in a:
             arr.append(chr(ord(d)-1))
     return ''.join(arr)

def ran(c):
     bol=rand.randint(0,1)
     if(bol):
             c = a(c)
     else:
             c = b(c)
     return c

def Rand(y, n):
     for i in range(n):
             y=ran(y)
     return y
 
def code(y, n):
  for i in y:
     if ord(i) + n >= 0x110000:
     	i = chr(ord(i) + n - 0x110000+1);
  for i in range(n):
     y=a(y)
  return y

def decode(y, n):
  for i in y:
     if ord(i) - n < 0:
     	i = chr(ord(i) - n + 0x110000);
  for i in range(n):
     y=b(y)
  return y

try:
  lvl=rand.randint(0, 999);

##############################################
  st=[
  	  "Дратути))0))",
      "Приффки :)",
      "Пасибки, бро ;)",
      "НуЧоЗа(9((",
      "Досвидули :Р",
      "Сложнааа...",
      "Мамзелька :з",
      "Добрый вечер?",
      "Найти покемона",
      "Сложный прекол",
      "Баян! :D",
      "Майо Увожение",
      "Ничоси! :0"
     ]
##############################################

  index=rand.randint(1,len(st))-1;
  rst=Rand(st[index], lvl)

  while True:
    att=int(input("Введите ключ шифра, чтобы разгадать слово: "))
    if att<0:
    	att=-att
    	rst=decode(rst, att)
    else:
    	rst=code(rst, att)
    print("У вас получилось:", rst)
    if(rst == st[index]):
    	print("ПОЗДРАВЛЯШКИ!!! :3333")
    	break

except KeyboardInterrupt:
	print()

except EOFError:
	print()
	
except ValueError:
	print("Введите целое число!")
