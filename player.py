
import random as ran
class Player():
	def __init__(self, balance, step, id, name):
		self.balance = balance
		self.cards = []
		self.step = step
		self.id = id
		self.name = name
		self.sCards = []

#TODO добавить ботов beta1
class Bot():
	def __init__(self):
		names = ['Джо', 'Мики', 'Питер', 'Ники', 'Мэй', 'Лекстер', 'Доктор Абоба', 'Михаил', 'Маэстро', 'Глеб', 'Василёчек']
		self.name = names[ran.randint(0, len(names)-1)]
