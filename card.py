
class Card():
	"""docstring for ClassName"""
	def __init__(self, cost, type, color, num, gift, name, dNum, count):
		self.cost = cost
		self.type = type
		self.color = color
		self.gift = gift
		self.name = name
		self.num = num
		self.dNum = dNum
		self.count = count

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

	def checkMarket(player):
		hasMarket = False
		for i in range(len(player.sCards)):
			card = player.sCards[i-1]
			if card.name == 'supermarket':
				if card.count == 1:
					hasMarket = True
		return hasMarket

	def blue_standart(card, cq, lp, players):
		balance = 0
		for i in range(lp):
			if not players[i-1].id == cq:
				hasCard = False
				pCard = Card(0, 0, 0, 0, 0, 0,0,0)
				for g in range(len(players[i - 1].cards)):
					if players[i - 1].cards[g - 1].name == card.name:
						pCard = players[i-1].cards[g-1]
						hasCard = True
				if hasCard:
					players[i-1].balance += pCard.gift * pCard.count
			else:
				balance = card.gift * card.count
		return balance

	def blue_factory(card, cq, lp, players, type, player, pq):
		balance = 0
		for i in range(lp):
			if not players[i-1].id == pq[cq-1]:
				hasCard = False
				pCard = Card(0, 0, 0, 0, 0, 0,0,0)
				for g in range(len(players[i-1].cards)):
					if players[i-1].cards[g-1].name == card.name:
						pCard = players[i - 1].cards[g - 1]
						hasCard = True

				if hasCard:
					multiplier = 0
					for h in range(len(players[i-1].cards)):
						if players[i-1].cards[h-1].type == type and not players[i-1].cards[h-1].name == card.name:
							#print(players[i-1].cards[h-1].name)
							multiplier += 1 * players[i-1].cards[h-1].count
					#print('multiplier2 = ' + str(multiplier))
					players[i-1].balance += pCard.gift * pCard.count * multiplier
			else:
				multiplier = 0
				for g in range(len(player.cards)):
					if player.cards[g-1].type == type and not player.cards[g-1].name == card.name:
						#print(player.cards[g-1].name)
						multiplier += 1 * player.cards[g - 1].count
				#print('multiplier = ' + str(multiplier))
				balance = card.gift * card.count * multiplier
		return balance

	def green_standart(card, players, player):
		lp = len(players)
		balance = 0
		balance = card.gift * card.count
		if card.type == 'clothes':
			if Card.checkMarket(player):
				balance += card.count
		return balance

	def green_factory(card, player, type, players):
		lp = len(players)
		balance = 0
		multiplier = 0
		Cards = player.cards
		for i in range(len(Cards)):
			if Cards[i - 1].type == type and not Cards[i-1].name == card.name:
				multiplier += Cards[i - 1].count
		balance = card.gift * card.count * multiplier
		if card.type == 'clothes':
			if Card.checkMarket(player):
				balance += card.count
		return balance

	def checkCubeNum(CubeNum, card):
		ret = False
		if CubeNum >= card.num and CubeNum <= card.dNum:
			ret = True
		return ret

	def switchCards(Player1, Player2, card1, card2):
		hasCard1 = False
		hasCard2 = False
		cardID1 = 0
		cardID2 = 0
		for card in Player1.cards:
			if card.name == card1.name:
				hasCard1 = True
				cardID1 = Player1.cards.index(card)
		for card in Player2.cards:
			if card.name == card2.name:
				hasCard2 = True
				cardID2 = Player2.cards.index(card)

		if hasCard1:
			Player1.cards[cardID1].count += 1
			if card2.count == 1:
				Player1.cards.remove(card2)
			else:
				for card in Player1.cards:
					if card.name == card2.name:
						card.count -= 1
		else:
			Player1.cards.append(card1)
			Player1.cards.remove(card2)
		if hasCard2:
			Player2.cards[cardID2].count += 1
			if card1.count == 1:
				Player2.cards.remove(card1)
			else:
				for card in Player2.cards:
					if card.name == card1.name:
						card.count -= 1
		else:
			Player2.cards.remove(card1)
			Player2.cards.append(card2)


	def red(Players, currentPlayer, CubeNum):
		for player in Players:
			if not player == currentPlayer:
				for card in player.cards:
					if Card.checkCubeNum(CubeNum, card) and card.type == 'cup':
						multiplier = 0
						if Card.checkMarket(player):
							multiplier = card.count
						modif = card.gift + multiplier
						if currentPlayer.balance >= modif:
							player.balance += modif
							currentPlayer.balance -= modif
							print('Игрок ' + currentPlayer.name + ' отдаёт ' + str(modif) + ' игроку ' + player.name)
						else:
							player.balance += currentPlayer.balance
							currentPlayer.balance -= currentPlayer.balance
							print('Игрок ' + currentPlayer.name + ' отдаёт ' + str(currentPlayer.balance) + ' игроку ' + player.name)
	def stadium(Players, currentPlayer, CubeNum):
		for player in Players:
			if not player == currentPlayer:
				for card in currentPlayer.cards:
					if Card.checkCubeNum(CubeNum, card) and card.name == 'stadium':
						modif = card.gift
						if player.balance >= modif:
							currentPlayer.balance += modif
							player.balance -= modif
							print('Игрок ' + player.name + ' отдаёт ' + str(modif) + ' игроку ' + currentPlayer.name)
						else:
							currentPlayer.balance += player.balance
							player.balance -= player.balance
							print('Игрок ' + player.name + ' отдаёт ' + str(
								player.balance) + ' игроку ' + currentPlayer.name)
	def tvcenter(Players, currentPlayer, CubeNum):
		for card in currentPlayer.cards:
			if Card.checkCubeNum(CubeNum, card) and card.name == 'TV center':
				print('Выберите игрока:')
				for player in Players:
					if not player == currentPlayer: print(player.name + ' ' + str(player.balance) + Card.coinsTransform(player.balance))
				name = input()
				Player = None
				for player in Players:
					if player.name == name:
						Player = player
				if not Player == None:
					modif = card.gift
					if Player.balance >= modif:
						currentPlayer.balance += modif
						Player.balance -= modif
						print('Игрок ' + Player.name + ' отдаёт ' + str(modif) + Card.coinsTransform(modif) + ' игроку ' + currentPlayer.name)
					else:
						print('Игрок ' + Player.name + ' отдаёт ' + str(
							Player.balance) + Card.coinsTransform(Player.balance) + ' игроку ' + currentPlayer.name)
						currentPlayer.balance += Player.balance
						Player.balance -= Player.balance

	def businesscenter(Players, currentPlayer, CubeNum):
		for card in currentPlayer.cards:
			if Card.checkCubeNum(CubeNum, card) and card.name == 'business center':
				print('Выберите игрока:')
				for player in Players:
					if not player == currentPlayer:
						print(player.name)
						print('Его карты:')
						number = 1
						for i in range(len(player.cards)):
							if not player.cards[i-1].type == 'entertainment':
								print(str(number) + player.cards[i-1].name)
								number += 1
				name = input()
				Player = None
				for player in Players:
					if name == player.name:
						Player = player
				cards = Player.cards
				for i in range(len(cards)):
					print(str(i-1) + cards[i-1].name)
				cardNum = int(input('Номер карты игрока: '))
				CARD = None
				for i in range(len(cards)):
					if i-1 == cardNum:
						CARD = cards[i-1]
				for i in range(len(currentPlayer.cards)):
					print(str(i-1) + currentPlayer.cards[i-1].name)
				cardNum = int(input('Номер вашей карты: '))
				YCARD = None
				for i in range(len(currentPlayer.cards)):
					if i-1 == cardNum:
						YCARD = currentPlayer.cards[i-1]
				print('Игрок ' + currentPlayer.name + ' забирает карту ' + CARD.name + ' у игрока ' + Player.name + ' и отдаёт ему ' + YCARD.name)
				Card.switchCards(currentPlayer, Player, CARD, YCARD)


	def CardFun(players, card, player, cq, pq):
		balance = 0
		cName = card.name
		lp = len(players)

		if cName == 'wheat field':
			balance = Card.blue_standart(card, cq, lp, players)
		if cName == 'apple garden':
			balance	 = Card.blue_factory(card, cq, lp, players, 'wheat', player, pq)
		if cName == 'mine':
			balance = Card.blue_standart(card, players, players)
		if cName == 'forest':
			balance = Card.blue_standart(card, cq, lp, players)
		if cName == 'farm':
			balance = Card.blue_standart(card, cq, lp, players)

		if cName == 'bakery':
			balance = Card.green_standart(card, players, player)
		if cName == 'shop':
			balance = Card.green_standart(card, players, player)
		if cName == 'furniture factory':
			balance = Card.green_factory(card, player, 'gear', players)
		if cName == 'cheese factory':
			balance = Card.green_factory(card, player, 'pig', players)
		if cName == 'fruit market':
			balance = Card.green_factory(card, player, 'wheat', players)


		return balance


	def BuyCard(self, Player):
		cost = self.cost
		Player.balance -= cost
		Player.cards.append(self)
