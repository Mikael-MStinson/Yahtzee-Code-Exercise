from unittest import TestCase
from yahtzee import Yahtzee, RollLimitError, HandNotRolledError


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
	
	def test_roll_limit_with_different_limits(self):
		yahtzee = Yahtzee(roll_limit=5)
		yahtzee.roll()
		yahtzee.roll()
		yahtzee.roll()
		yahtzee.roll()
		yahtzee.roll()
		self.assertRaises(RollLimitError, yahtzee.roll)
		
	def test_roll_with_dice(self):
		yahtzee = Yahtzee()
		self.assertRaises(HandNotRolledError, yahtzee.hand)
		yahtzee.roll()
		hand = yahtzee.hand()
		self.assertIsInstance(hand, list)
		yahtzee.roll()
		hand2 = yahtzee.hand()
		self.assertTrue(hand != hand2)
	