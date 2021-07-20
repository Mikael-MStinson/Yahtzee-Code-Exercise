from unittest import TestCase
from yahtzee import Yahtzee, RollLimitError


class TestRolling(TestCase):
	def test_roll_method(self):
		yahtzee = Yahtzee()
		yahtzee.roll()
		
	def test_roll_limit(self):
		yahtzee = Yahtzee()
		yahtzee.roll()
		yahtzee.roll()
		yahtzee.roll()
		self.assertRaises(RollLimitError, yahtzee.roll)
		
	def test_roll_limit_and_score(self):
		yahtzee = Yahtzee()
		yahtzee.roll()
		yahtzee.roll()
		yahtzee.roll()
		self.assertRaises(RollLimitError, yahtzee.roll)
		yahtzee.score()
		yahtzee.roll()
		yahtzee.roll()
		yahtzee.roll()
		self.assertRaises(RollLimitError, yahtzee.roll)
		
	def test_roll_and_score_before_limit(self):
		yahtzee = Yahtzee()
		yahtzee.roll()
		yahtzee.roll()
		yahtzee.score()
		yahtzee.roll()
		yahtzee.roll()
		yahtzee.roll()
		self.assertRaises(RollLimitError, yahtzee.roll)
	
	