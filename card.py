
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

# TODO доделать красные карты
	def red(Players, PlayersQueue, curentQueue, CubeNum):
		curentPlayer = Players[PlayersQueue[curentQueue]]
		for i in range(len(Players)):
			print('red loop')
			hasRedCard = False
			modif = 0
			Cards = curentPlayer.cards
			for g in range(len(Cards)):
				if Cards[g - 1].type == 'cup':
					if CubeNum >= Cards[g - 1].num and CubeNum <= Cards[g - 1].dNum:
						print('hasCard')
						hasRedCard = True
						modif = Cards[g - 1].gift
						print(modif)
			curentPlayerBalance = curentPlayer.balance

			print(Players[i-1].name)
			print(curentPlayer.name)
			print(hasRedCard)
			if not Players[i - 1] == curentPlayer and hasRedCard:
				print('not')
				if curentPlayerBalance >= modif:
					Players[i - 1].balance += modif
					print(Players[i-1].name + ' Получает ' + str(modif) + ' за счёт ' + curentPlayer.name)
					curentPlayer.balance -= modif
					print(curentPlayer.name + ' Теряет ' + str(modif) + ' отдав игроку ' + Players[i-1].name)
				if curentPlayerBalance > 0 and curentPlayerBalance < modif:
					Players[i - 1].balance += curentPlayerBalance
					print(Players[i - 1].name + ' Получает ' + str(curentPlayerBalance) + ' за счёт ' + curentPlayer.name)
					curentPlayer.balance -= curentPlayerBalance
					print(curentPlayer.name + ' Теряет ' + str(curentPlayerBalance) + ' отдав игроку ' + Players[i - 1].name)

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
