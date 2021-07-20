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
		