from random import randint as ran
from sys import argv as teams

del teams[0]  # читаем названия команд из аргументов нашей программы
number = len(teams)  # хранит количество команд

if number < 2:
	print("Команд должно быть хотя бы 2 :-(")
	exit()

goals = []  # таблица голов (цифра в позиции (i,j) описывает кол-во голов,
							     # забитых i-ой командой j-ой команде)
results = []  # итоговая таблица (i-я строка - i-я команда; столбцы:
							  # название, кол-во побед, кол-во поражений, кол-во ничьих,
							  # голов забито, голов пропущено, кол-во очков)

# заполняем таблицу голов случайными числами от 0 до 10
for a in range(number):
	goals.append( [] )
	for b in range(number):
		if a != b:
			goals[a].append(ran(0, 10))
		else:
			goals[a].append(0)

# на основе таблицы голов заполняем итоговую таблицу
for i in range(number):
	wins=0
	defeats=0
	draws=0
	goal=0
	
	for j in range(number):
		goal += goals[j][i]
		if goals[i][j] > goals[j][i]:
			wins += 1
		elif goals[i][j] == goals[j][i]:
			draws += 1
		else:
			defeats += 1
	
	results.append([teams[i],		  # название команды
					wins,			  # кол-во побед
					defeats,		  # кол-во поражений
					draws-1,		  # кол-во ничьих
					sum(goals[i]),	  # забитые голы
					goal, 			  # пропущенные голы
					wins*3 + draws])  # набранные очки

# сортируем по кол-ву набранных очков
results.sort(key = lambda x: x[6], reverse = True)

# вывод таблицы
print(" № |    Название    |  Побед  |Поражений| Ничьих  | Забито  |Пропущено|  Очков  ")
print("___|________________|_________|_________|_________|_________|_________|_________")

#print("---|----------------|---------|---------|---------|---------|---------|---------")

for i in range(1,number+1):
	print("{0:^3}|{1[0]:^16}|{1[1]:^9}|{1[2]:^9}|{1[3]:^9}|{1[4]:^9}|{1[5]:^9}|{1[6]:^9}".format(i, results[i - 1]))

# ждём команд от пользователя
print()
print("Введите h/help/? для получения справки")
while True:
	
	# предусматриваем различные варианты выхода
	try:
		text = input(':')
	except EOFError:
		print()
		break
	except KeyboardInterrupt:
		print()
		break
	else:
		if text == 'q' or text == 'quit' or text == 'exit':
			print()
			break
		
		# показываем справку
		if text == 'h' or text == 'help' or text == '?':
			print("Для получения информации о конкретном матче введите названия игравших команд через пробел.")
			print("Для выхода из программы наберите Ctrl+D/Ctrl+C/q/quit/exit")
		else:
		
			# показываем счёт, с которым завершился запрошенный матч
			text = text.split()
			if len(text) == 2 and text[0] in teams and text[1] in teams:
				a = teams.index(text[0])
				b = teams.index(text[1])
				if a != b:
					print("Встреча {} - {} завершилась со счётом: {}:{}".format(teams[a], teams[b], goals[a][b], goals[b][a]))
			else:
				print("Такая встреча не проводилась")
