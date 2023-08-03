
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

	def CardFun(players, card, player, firstDrop):
		balance = 0
		cName = card.name
		lp = len(players)

		if cName == 'wheat field':
			for i in range(lp):
				if not player.step:
					player.balance = players[i-1].balance + (card.gift * card.count)-1
			balance = player.balance + (card.gift * card.count)-1
		if cName == 'apple garden':
			for i in range(lp):
				if not player.step:
					player.balance = players[i - 1].balance + (card.gift * card.count) - 1
			balance = player.balance + (card.gift * card.count) - 1
		if cName == 'mine':
			for i in range(lp):
				if not player.step:
					player.balance = players[i - 1].balance + (card.gift * card.count) - 1
			balance = player.balance + (card.gift * card.count) - 1
		if cName == 'forest':
			for i in range(lp):
				if not player.step:
					player.balance = players[i - 1].balance + (card.gift * card.count) - 1
			balance = player.balance + (card.gift * card.count) - 1
		if cName == 'farm':
			for i in range(lp):
				for i in range(lp):
					if not player.step:
						player.balance = players[i - 1].balance + (card.gift * card.count) - 1
				balance = player.balance + (card.gift * card.count) - 1

		if cName == 'bakery':
			balance = player.balance + (card.gift * card.count)
		if cName == 'shop':
			balance = player.balance + (card.gift * card.count)
		if cName == 'furniture factory':
			multiplier = 0
			Cards = player.cards
			for i in range(len(Cards)):
				if Cards[i-1].type == 'gear':
					for g in range(card.count):
						multiplier += 1
			balance = player.balance + (card.gift * card.count * multiplier)
		if cName == 'cheese factory':
			multiplier = 0
			Cards = player.cards
			for i in range(len(Cards)):
				if Cards[i-1].type == 'pig':
					for g in range(card.count):
						multiplier += 1
			balance = player.balance + (card.gift * card.count * multiplier)
		if cName == 'fruit market':
			multiplier = 0
			Cards = player.cards
			for i in range(len(Cards)):
				if Cards[i-1].type == 'wheat':
					for g in range(card.count):
						multiplier+=1
			balance = player.balance + (card.gift * card.count * multiplier)

		if firstDrop:
			balance += 1
		return balance

	def BuyCard(self, Player):
		cost = self.cost
		Player.balance -= cost
		Player.cards.append(self)
