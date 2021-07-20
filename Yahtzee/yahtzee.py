from random import choice 

class HandNotRolledError(Exception):
	pass

class RollLimitError(Exception):
	pass

class Yahtzee:
	def __init__(self, roll_limit = 3):
		self.roll_count = 0
		self.roll_limit = roll_limit
		
	def roll(self):
		if self.roll_count >= self.roll_limit:
			raise RollLimitError("Player cannot roll anymore and must score")
		self.roll_count += 1
		
	def score(self):
		self.roll_count = 0
	
	def hand(self):
		if self.roll_count == 0:
			raise HandNotRolledError("Player must roll before they can read their hand")
		else:
			return [choice([1,2,3,4,5,6])]
		