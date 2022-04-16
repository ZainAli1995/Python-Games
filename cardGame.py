#This is a simulation of the WAR game
import random

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

class Card:

	def __init__(self,suit,rank):

		self.suit = suit
		self.rank = rank
		self.value = values[rank]

	def __str__(self):
		return self.rank + " of " + self.suit

"""
two_hearts = Card(suits[0],ranks[0])
print(two_hearts)
print(values[two_hearts.rank])
"""

class Deck:

	def __init__(self):
		self.all_cards = []
		for suit in suits:
			for rank in ranks:
				card = Card(suit,rank)
				self.all_cards.append(card)

	def shuffle(self):
		random.shuffle(self.all_cards)

	def deal_one(self):
		return self.all_cards.pop()
"""
mydeck = Deck()
print(len(mydeck.all_cards))

print(mydeck.all_cards[0])

mydeck.shuffle()

print(mydeck.all_cards[0])

print(mydeck.deal_one())
"""

class Player:

	def __init__(self,name):
		self.name = name
		self.all_cards = []

	def remove_one(self):
		return self.all_cards.pop(0)

	def add_cards(self,new_cards):
		if type(new_cards) == type ([]):
			self.all_cards.extend(new_cards)
		else:
			self.all_cards.append(new_cards)

	def __str__(self):
		return "Player {} has {} cards".format(self.name,len(self.all_cards))
"""
jose = Player("Jose")
print(jose)

jose.add_cards(two_hearts)
print(jose)

jose.add_cards([two_hearts,two_hearts,two_hearts])
print(jose)
"""
	#Create two players
player_one = Player("playerOne")
player_two = Player("playerTwo")

	#Intiliaze the deck
deck = Deck()
	#shuffle the deck
deck.shuffle()

	#Deal 26 cards to each of the players
for i in range(26):
	player_one.add_cards(deck.deal_one())
	player_two.add_cards(deck.deal_one())

round_num = 0
game_on = True

while game_on:
	round_num += 1
	print("Round {}".format(round_num))

	if len(player_one.all_cards) == 0:
		print("Player one out of cards !! Game over !!")
		print("Player Two Wins !!")
		game_on = False
		break

	if len(player_two.all_cards) == 0:
		print("Player two out of cards !! Game Over !!")
		print("Player One Wins !!")
		game_on = False
		break

	#player one will start the game

	player_one_cards = []
	player_two_cards = []

	player_one_cards.append(player_one.remove_one())
	player_two_cards.append(player_two.remove_one())

	atWar = True
	while atWar:

		if player_one_cards[-1].value > player_two_cards[-1].value:
			player_one.add_cards(player_one_cards)
			player_one.add_cards(player_two_cards)
			atWar = False

		elif player_two_cards[-1].value > player_one_cards[-1].value:
			player_two.add_cards(player_two_cards)
			player_two.add_cards(player_one_cards)
			atWar = False

		else:
			#We are at War now
			if len(player_one.all_cards) < 5:
				print("Player One unable to player war! Game over at War")
				print("Player Two Wins! Player One looses!!")
				game_on = False
				break
				

			elif len(player_two.all_cards) < 5:
				print("Player Two unable to player war! Game over at War")
				print("Player One Wins! Player Two looses!!")
				game_on = False
				break

			else:
				print("War !!")
				for num in range(5):
					player_one_cards.append(player_one.remove_one())
					player_two_cards.append(player_two.remove_one())