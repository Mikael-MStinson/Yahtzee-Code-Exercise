# Yahtzee Code Exercise
 This is an exersize to recreate the game of yatzee using TDD. With the goal of making the rules expandable.
 Inspired by this video - https://www.youtube.com/watch?v=l7E3y4te7sA


## How To Play:
Player can roll a set of dice up to 3 times. On the first roll, the player rolls all 5 dice, then sets any keepers aside, rerolling the remaining dice.
Once the player has gotten a set of dice they are happy with, or have used all 3 rolls, the player must then score.

To score, the player applies the dice to one of the rules in their list.
Once a rule has been used, it cannot be used again, apart from Yahtzee.

The game ends when all rules are used up, and the total number of points earned per rule is the players score.

## Rules
* Aces - score equal to the sum of all 1's in a roll
* Twos - score equal to the sum of all 2's in a roll
* Threes - score equal to the sum of all 3's in a roll
* Fours - score equal to the sum of all 4's in a roll
* Fives - score equal to the sum of all 5's in a roll
* Sixes - score equal to the sum of all 6's in a roll
* 3 of a kind - score is equal to the sum of all dice - applies only if 3 of the dice match
* 4 of a kind - score is equal to the sum of all dice - applies only if 4 of the dice match
* Full house - score is equal to 25 - applies only if there is a 2 of a kind and a 3 of a kind
* Small Straight - score is equal to 30 - applies only if there is a consecutive sequence of 4
* Large Straight - score is equal to 40 - applies only if there is a consecutive sequence of 5
* Yahtzee - score is equal to 50 and then 100 every time after that - applies only if there is 5 of a kind
* Chance - score is equal to the sum of all dice

## Bonus Challenges
* Add a Fibon-Yahtzee rule - 100 points if the player can get a 1, 1, 2, 3, 5 in a roll without changing the code
* Add a bonus 35 points that are added if the sum of aces through sixes is at least 63 - do so without changing too much of the code.
* Create a UI using TKinter without changing the logic code

## Behaviors
* When the player types `roll`, a random hand is generated - 5 6-sided dice
* The dice should appear in a table with a die number beside it, along with the players scorecard underneath
* A config file can change how many dice can be played and how many faces each dice has
* The player can then type `keep n,n,n` to keep what ever numbers they choose.
* Dice that are being kept should have an asterix appear next to them
* The player can then type `roll` again to roll the remaining dice
* The `roll` command becomes disabled after 3 uses, and the player must score to reenable it.
* The player can type the `score n` command to apply their hand to a rule
* Typing this will reprint the scorecard with their new score and reenable/reset the roll command
* Once the scorecard is filled, the total score is printed
