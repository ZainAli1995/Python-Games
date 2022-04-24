#Hangman game to guess the word
#Print the word using dashes
import csv
import random

def printWord(wordlist):

	for letter in wordlist:
		print(letter,end="  ")

	print()

def readWordsCSV(file):

	data = open(file,encoding='utf-8')
	csv_data = csv.reader(data)

	return list(csv_data)

def chooseWord(word_list):

	rand = random.randint(0,len(word_list)-1)
	return list(word_list[rand][0])

def checkIfLetterInWord(letter,word):

	indices = []
	index = 0
	for char in word:
		if char == letter:
			indices.append(index)
		index += 1
	return indices

def generateEmptyStartingList(guess_word):
	
	generatePlayerList = []
	
	for i in range(len(guess_word)):
		generatePlayerList.append("_")
	return generatePlayerList

def checkIfAllGuessed(guess_word):

	if "_" in guess_word:
		return False
	else:
		return True

def replaceCharacter(player_guess,letter,indices):

	for i in indices:
		player_guess[i] = letter

#def replaceChar(word,letter,index):
word_list = readWordsCSV('country_data.csv')
guess_word = chooseWord(word_list)
player_guess = generateEmptyStartingList(guess_word)
printWord(player_guess)

gameOn = True
attempts = 0

while attempts < 6 and not checkIfAllGuessed(player_guess):

	user_input = input("\nEnter a letter ")
	indices = checkIfLetterInWord(user_input,guess_word)
	if len(indices) == 0:
		attempts += 1
	replaceCharacter(player_guess,user_input,indices)
	printWord(player_guess)

	print("Number of attempts left : " + str(6 - attempts))

if attempts != 6:
	print("Congratulations !! You are the winner of this game !! ")
else:
	print("Ooops sorry you have lost !! Try again later")