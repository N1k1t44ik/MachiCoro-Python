import random

from card import *
from player import *
import random as ran
import os
from time import sleep as s
import keyboard as key

ver = 'Alpha 4'
print('version : ' + ver + '\n')

logs = open('logs.txt', 'w')
lt = ''
count = 0
true = True
false = False
GameCards = []
Players = []
PlayersQueue = []
ID = 0
curentQueue = 0
allowedCards = []
autodrop = False
winid = 0
Range = 0
firstDrop = True
firstStep = True
DropCubeType = 'd'

class Game():
	def field(cards, Interface, player):
		if Interface == 'Player':
			for i in range(len(cards)):
				if cards[(i - 1) * -1].num == cards[(i - 1) * -1].dNum:
					print('- ' + cards[(i - 1) * -1].name + '(' + str(cards[(i - 1) * -1].num) + ') x' + str(
						cards[(i - 1) * -1].count))
				if not cards[(i - 1) * -1].num == cards[(i - 1) * -1].dNum:
					print('- ' + cards[(i - 1) * -1].name + '(' + str(cards[(i - 1) * -1].num) + '-' + str(
						cards[(i - 1) * -1].dNum) + ') x' + str(cards[(i - 1) * -1].count))
		if Interface == 'Allowed':
			for i in range(len(cards)):
				print(str(i + 1) + ' ' + cards[i - 1].name + ' - ' + str(cards[i - 1].cost))
		if Interface == 'Special':
			scards = player.sCards
			for i in range(len(scards)):
				hasCard = 'not bought'
				if scards[i-1].count >= 1:
					hasCard = 'bought'
				print('- ' + scards[i-1].name + ' - ' + hasCard)

	def coinsTransform(count):
		coinsText = ''
		values = [[1, 21, 31, 41, 51, 61, 71, 81, 91, 101, 121], [3, 4, 23, 24, 33, 34, 43, 44, 53, 54, 63, 64, 73, 74, 83, 84, 93, 94, 103, 103, 123, 124]]
		worked = False
		for i in range(len(values[0])):
			if count == values[0][i - 1]:
				coinsText = ' монета'
				worked = True
		for i in range(len(values[1])):
			if count == values[1][i - 1]:
				coinsText = ' монеты'
				worked = True
		if not worked:
			coinsText = ' монет'

		return coinsText

	def addCard(player, name, count):
		haveCard = False

		for i in range(len(player.cards)):
			if player.cards[i - 1].name == name:
				haveCard = True
			# print('hc set true  ' + name + '  ' + player.cards[i-1].name)

		if haveCard:
			for i in range(len(player.cards)):
				if player.cards[i - 1].name == name:
					player.cards[i - 1].count += count

		if not haveCard:
			if name == 'wheat field':
				player.cards.append(Card(cost=1, type='wheat', color='blue', num=1, gift=1, name=name, dNum=1, count=1))
			if name == 'bakery':
				player.cards.append(
					Card(cost=1, type='clothes', color='green', num=2, gift=1, name=name, dNum=3, count=1))
			if name == 'apple garden':
				player.cards.append(
					Card(cost=3, type='wheat', color='blue', num=10, gift=3, name=name, dNum=10, count=1))
			if name == 'mine':
				player.cards.append(Card(cost=6, type='gear', color='blue', num=9, gift=5, name=name, dNum=9, count=1))
			if name == 'forest':
				player.cards.append(Card(cost=3, type='gear', color='blue', num=5, gift=1, name=name, dNum=5, count=1))
			if name == 'farm':
				player.cards.append(Card(cost=1, type='pig', color='blue', num=2, gift=1, name=name, dNum=2, count=1))
			if name == 'shop':
				player.cards.append(
					Card(cost=2, type='clothes', color='green', num=4, gift=3, name=name, dNum=4, count=1))
			if name == 'furniture factory':
				player.cards.append(
					Card(cost=3, type='factory', color='green', num=8, gift=3, name=name, dNum=8, count=1))
			if name == 'cheese factory':
				player.cards.append(
					Card(cost=5, type='factory', color='green', num=7, gift=3, name=name, dNum=7, count=1))
			if name == 'fruit market':
				player.cards.append(
					Card(cost=2, type='apple', color='green', num=11, gift=2, name=name, dNum=12, count=1))
			if name == 'cafe':
				player.cards.append(
					Card(cost=2, type='cup', color='red', num=3, gift=1, name=name, dNum=3, count=1))
			if name == 'supermarket':
				player.sCards.append(
					Card(cost=10, type='special', color='gray', num=0, gift=0, name=name, dNum=0, count=0))

	def buyCard(Player, allowedCards):
		global autodrop
		ans = input('\nВыберите действие:\n1 - купить карту\n2 - пропустить ход\n')

		if ans == '1':
			cardnum = int(input('Введите номер карты: '))
			reversedAC = list(reversed(allowedCards))
			if not cardnum == 1:
				if not reversedAC[(cardnum - 1) * -1].type == 'special': Game.addCard(Player, reversedAC[(cardnum - 1) * -1].name, 1)
				if reversedAC[(cardnum - 1) * -1].type == 'special': reversedAC[(cardnum - 1) * -1].count = 1
				Player.balance -= reversedAC[(cardnum - 1) * -1].cost
				cost = reversedAC[(cardnum - 1) * -1].cost
				print('Игрок ' + Player.name + ' покупает ' + reversedAC[(cardnum - 1) * -1].name + ' и у него -' + str(
					cost) + Game.coinsTransform(cost))
			if cardnum == 1:
				if not reversedAC[(cardnum - 1) * -1].type == 'special': Game.addCard(Player, allowedCards[(cardnum - 2)].name, 1)
				if reversedAC[(cardnum - 1) * -1].type == 'special': reversedAC[(cardnum - 1) * -1].count = 1
				Player.balance -= allowedCards[(cardnum - 2)].cost
				cost = allowedCards[(cardnum - 2)].cost
				print('Игрок ' + Player.name + ' покупает ' + allowedCards[(cardnum - 2)].name + ' и у него -' + str(
					cost) + Game.coinsTransform(cost))
		# print(allowedCards[cardnum*-1].name + '  ' + str(cardnum))

	def dropCube(type, player):
		CubeNum = 0
		if not type == 'd':
			CubeNum = ran.randint(1, 6)
			player.cubeNum = CubeNum
		else:
			CubeNum = int(input())
			player.cubeNum = CubeNum
		return CubeNum

	def arrayToString(massive):
		ret = ''
		ret = str(massive).replace('[', '').replace(']', '').replace(',', '')
		return ret

def cc():
	os.system('cls')

def writeLogs():
	global lt
	global logs
	logs.write(lt)

def setupCards():
	gameAddCard(1, 'wheat', 'blue', 1, 1, 'wheat field', 1, 11)
	gameAddCard(1, 'clothes', 'green', 2, 1, 'bakery', 3, 11)
	gameAddCard(3, 'wheat', 'blue', 10, 3, 'apple garden', 10, 6)
	gameAddCard(6, 'gear', 'blue', 9, 5, 'mine', 9, 6)
	gameAddCard(3, 'gear', 'blue', 5, 1, 'forest', 5, 6)
	gameAddCard(1, 'pig', 'blue', 2, 1, 'farm', 2, 6)
	gameAddCard(2, 'clothes', 'green', 4, 3, 'shop', 4, 6)
	gameAddCard(3, 'factory', 'green', 8, 3, 'furniture factory', 8, 6)
	gameAddCard(5, 'factory', 'green', 7, 3, 'cheese factory', 7, 6)
	gameAddCard(2, 'factory', 'green', 11, 2, 'fruit market', 12, 6)
	gameAddCard(2, 'cup', 'red', 3, 1, 'cafe', 3, 6)


def enterPlayer():
	global ID
	global lt
	global count
	global winid
	ids = []
	count = int(input('Кол-во игроков: '))
	if str(count) == '-1':
		count = 2
		key.write('Генадий')
		key.send('enter')
		key.write('Карп')
		key.send('enter')
	if str(count) == '-2':
		count = 3
		key.write('Генадий')
		key.send('enter')
		key.write('Карп')
		key.send('enter')
		key.write('Пригожин Женя')
		key.send('enter')
	if str(count) == '-3':
		count = 4
		key.write('Генадий')
		key.send('enter')
		key.write('Карп')
		key.send('enter')
		key.write('Пригожин Женя')
		key.send('enter')
		key.write('Ким-Чен-Ын')
		key.send('enter')
	if not count <= 1:
		for i in range(count):
			name = input('Введите имя игрока: ')
			Players.append(Player(3, false, ID, name))
			LocalPlayer = Players[ID]
			Game.addCard(LocalPlayer, 'wheat field', 1)
			Game.addCard(LocalPlayer, 'bakery', 1)
			Game.addCard(LocalPlayer, 'supermarket', 0)
			print('Игрок с именем: ' + name + ' и id: ' + str(ID) + ' был добавлен в игру!')
			lt += '\nPlayer content ' + name + ' ' + str(ID) + ' dots   --EnterPlayer'
			ids.append(ID)
			ID+=1
			s(0.4)
			cc()
			writeLogs()

		nums = []
		win = ''
		winid = 0
		for i in range(len(Players)):
			nums.append(ran.randint(0,6))
			ids.append(Players[i-1].id)
		for i in range(len(Players)):
			if Players[i-1].id == ids[(i-1)*-1]:
				Players[i-1].step = True
				win = Players[i-1].name
				winid = Players[i-1].id
			if not Players[i-1].id == ids[(i-1)*-1]:
				Players[i-1].step = False
		#print('Игрок ' + win + ' победил в жеребъёвке и бросает кубик первым!')
		lt += '\nCalculate first player: name:' + win + ' id:' + str(winid) + '  --id'
		writeLogs()


def gameAddCard(cost, type, color, num, gift, name, dNum, count):
	global GameCards
	GameCards.append(Card(cost, type, color, num, gift, name, dNum, count))

def changePlayer():
	global PlayersQueue
	global curentQueue
	global count
	global firstStep

	if firstStep:
		playersIDs = []
		for i in range(len(Players)):
			playersIDs.append(Players[i-1].id)
		PlayersQueue = []
		for i in range(len(playersIDs)):
			random_number = random.randint(0, len(playersIDs)-1)
			PlayersQueue.append(playersIDs[random_number])
			playersIDs.remove(playersIDs[random_number])
		firstStep = False

	curentQueue += 1
	if curentQueue >= len(PlayersQueue):
		curentQueue = 0

	Players[curentQueue-1].step = False
	Players[curentQueue].step = True

	# for i in range(len(Players)):
	# 	if Players[i-1].step:
	# 		Players[i-1].step = False
	# 	if Players[i-1].id == PlayersQueue[curentQueue-1]:
	# 		Players[i-1].step = True

#TODO добавить карты
def findCard(Player):
    global CubeNum
    global Players
    global lt
    for i in range(len(Player.cards)):
        Cards = Player.cards
        if CubeNum >= Cards[i-1].num and CubeNum <= Cards[i-1].dNum:
            lt += '\n --Card used-- Card: ' + str(Cards[i-1])
            writeLogs()
            addBalance = Card.CardFun(Players, Cards[i - 1], Player, curentQueue, PlayersQueue)
            Player.balance += addBalance
            if not addBalance == 0:
                print('Игрок ' + Player.name + ' получает ' + str(addBalance) + Game.coinsTransform((addBalance)))

# TODO баг кр карты
def findRedCard(cards):
	global CubeNum
	global oldCubeNum
	global Players
	global curentQueue
	global PlayersQueue
	if not CubeNum == oldCubeNum:
		for i in range(len(cards)):
			Card.RedFun(cards[i-1], curentQueue, PlayersQueue, Players, CubeNum)
		wait = False

def checkCard(name):
	ret = True
	for i in range(len(allowedCards)):
		Name = allowedCards[i-1].name
		if name == Name:
			ret = False
	return ret

# wheat cup entertainment pig gear clothes special factory apple

#Players.append(Player(3, true))
#Players.append(Player(6, false))

#Players[0].cards.append(Card(1, 'wheat', 'blue', 1, 1, 'wheat field', 1))
#Players[0].cards.append(Card(1, 'clothes', 'green', 2, 1, 'bakery', 3))
CubeNum = 0

setupCards()
enterPlayer()
cc()
changePlayer()

k = 0
oldCubeNum = 0

while True:
	for i in range(len(PlayersQueue)):
		oldCubeNum = CubeNum
		# Проверка является ли игрок ведущим
		if Players[i-1].id == PlayersQueue[curentQueue-1]:
			findRedCard(Players[i-1].cards)

			# Бросок кубика
			# TODO баг с пустым экраном
			CubeNum = Game.dropCube(DropCubeType, Players[i-1])


			# print(curentQueue)
			# print(Players[PlayersQueue[curentQueue - 1]].name)
			# print(PlayersQueue)
			# for g in range(len(Players)):
			# 	print(Players[g - 1].name + ' ' + str(Players[g - 1].id))

			lPlayer = Players[PlayersQueue[curentQueue-1]]
			print(lPlayer.name + ' бросает кубик.')
			print('Значение кубика: ' + str(CubeNum))

			# Проверка карт игрока
			findCard(lPlayer)

			# Создание списка с доступными для покупки картами
			allowedCards = []
			for j in range(len(GameCards)):
				card = GameCards[j - 1]
				if card.cost <= lPlayer.balance:
					if checkCard(card.name):
						allowedCards.append(card)
				scards = lPlayer.sCards
				if j <= len(scards):
					if scards[j-1].cost <= lPlayer.balance:
						if checkCard(scards[j-1].name):
							allowedCards.append(scards[j-1])

			# Отображение баланса,карт игрока / разрешённых карт / специальных карт
			coins = Game.coinsTransform(lPlayer.balance)
			print('Баланс игрока ' + lPlayer.name + ': ' + str(lPlayer.balance) + coins)
			print('Специальные карты игрока: ')
			Game.field(lPlayer.cards, 'Special', lPlayer)
			print('Карты игрока: ')
			Game.field(lPlayer.cards, 'Player', lPlayer)
			print('\nКарты доступные для покупки:')
			Game.field(allowedCards, 'Allowed', lPlayer)

			# Запуск покупки карты
			Game.buyCard(lPlayer, allowedCards)
			# Смена игрока
			changePlayer()


			command = ''
			if not autodrop: command = input('команда: ')
			if autodrop: command = ''

			if command == 'e' or command == 'у' or command == '\n':
				writeLogs()
				logs.close()
				exit()

			if command == 'c':
				changePlayer()

			if command == 'ad':
				autodrop = True

			if command == 'r':
				os.startfile('main.py')
				break

			command = command.split()
			if len(command) > 0:
				if command[0] == 'add':
					add = int(command[2])
					ThisPlayer = Players[0]
					name = command[1]
					for i in range(len(Players)):
						if Players[i-1].name == name:
							ThisPlayer = Players[i-1]
					ThisPlayer.balance += add
					print('Добавлено ' + str(add) + Game.coinsTransform(ThisPlayer.balance) + ' игроку ' + ThisPlayer.name)

			s(0.5)
			
			#cc()


WriteLogs()
logs.close()

# ./build.exe чтобы собрать новую версию приложения