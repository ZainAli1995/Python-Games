"""You need to create a simple text-based BlackJack game
The game needs to have one player versus an automated dealer.
The player can stand or hit.
The player must be able to pick their betting amount.
You need to keep track of the player's total money.
You need to alert the player of wins, losses, or busts, etc...
"""

#### Issue Tacker #####
# IP-1 dealer and player have equal cards, what to do in this scenario ??? 
# IP-2 implement the betting logic with this piece of code

#Create the resources required to create cards

import random

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':10}

class Card:

	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank
		self.value = values[rank]

	def __str__(self):
		return self.rank + " of " + self.suit

class Deck:

	def __init__(self):

		self.all_cards = []
		for suit in suits:
			for rank in ranks:
				card = Card(suit,rank)
				self.all_cards.append(card)

	def shuffle(self):

		random.shuffle(self.all_cards)

	def removeOne(self):
		return self.all_cards.pop(0)

#deck = Deck()
#print(deck.all_cards[0])
#deck.shuffle()
#print(deck.all_cards[0])
class Player:

	def __init__(self,name,money):
		self.name = name
		self.money = money

	def bet(self,money):

		if self.money >= money:
			self.money -= money
			return True
		else:
			return False

	def winBet(self,money):
		self.money += money

	def loseBet(self,money):
		self.money -= money

	def __str__(self):
		return self.name + " has $" + str(self.money) + " left" 

def showCards(player,cards):
	print(player + " cards")
	for card in cards:
		print(card,end=",")
	print()

def cardSum(cards):
	total = 0
	for card in cards:
		total += card.value
	return total

#Setup the game first
rounds = True
dealer = Player("Dealer",1000)
player = Player("Player",250)

print(player)

#### Issue Tacker #####
# IP-1 dealer and player have equal cards, what to do in this scenario ??? 
# IP-2 implement the betting logic with this piece of code

while rounds:

	deck = Deck()
	deck.shuffle()

	player_cards = []
	dealer_cards = []

	for i in range(2):
		player_cards.append(deck.removeOne())

	showCards("Player ",player_cards)
	dealer_cards.append(deck.removeOne())
	showCards("Dealer ", dealer_cards)

	while True:
		takeInput = input("How much would you like to bet SIR ? ")
		try:
			checkMoney = int(takeInput)
		except:
			print("You can only input numbers, sorry !! ")
			continue
		else:
			break

	checkIfEnoughMoney = player.bet(checkMoney)

	if not checkIfEnoughMoney:
		print("Game is over, add more cash to your account to play any further !!!")
		rounds = False
		break

	gameOn = True

	while True:
		takeInput = input("Would you like to HIT OR STAND [H/S] ? ")
		if takeInput == "H":
			player_cards.append(deck.removeOne())
			showCards("Player " ,player_cards)
			if cardSum(player_cards) > 21:
				print("You have been BUSTED !! Dealer has the won the Round !!!")
				gameOn = False
				break
			else:
				continue
		elif takeInput == "S":
			print("DO NOTHING and let the dealer hit now")
			while cardSum(dealer_cards) <= 16:
				dealer_cards.append(deck.removeOne())
				showCards("Dealer ",dealer_cards)
			break
		else:
			print("Wrong input try again !!!")
			continue

	dealer_total = cardSum(dealer_cards)
	player_total = cardSum(player_cards)

	if gameOn:
		if dealer_total > 21:
			print("Dealer has been BUSTED !!! Player One has won the game !!!")
			player.winBet(checkMoney * 2)
		elif dealer_total > player_total:
			print("Dealer has Won the game !!! ")
			player.loseBet(checkMoney)
		elif dealer_total < player_total:
			print("Player has Won the game")
			player.winBet(checkMoney *  2)
		else:
			print("The game was drawn")
			player.winBet(checkMoney)

	askInput = 'S'
	while askInput not in ['Y','N']:
		askInput = input("Would you like to play again SIR ? [Y/N] ")
		if askInput == 'N':
			rounds = False
			break
		elif askInput == 'Y':
			break
		else:
			print("Incorrect input, try again please !! ")
			continue
	print(player)