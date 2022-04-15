#Building a tictactoe version using python
#You will play with the computer
import random

def displayBoard(board_list):

	for i in range(1,len(board_list)+1):

		if i % 3 == 0:
			print(board_list[i-1])
		else:
			print(board_list[i-1],end="")

def startFirst():

	return random.randint(1,2)

def choosePlayerOnePos(board_list):

	while True:
		try:
			result = int(input("Where would you like to place your item ? "))
		except:
			print("You can only input numbers between 1 and 9")
			continue
		else:
			if result > 9 or result < 1:
				print("You can only input numbers between 1 and 9")
				continue
			else:
				if checkIfEmpty(board_list,result):
					break
				else:
					print("This position is already taken, try again ")
					continue

	return result

def chooseComputerPos(board_list):

	pos = random.randint(1,9)

	while not checkIfEmpty(board_list,pos):
		pos = random.randint(1,9)

	return pos

def placerPos(board_list,pos,marker):

	board_list[pos-1] = marker

def checkIfEmpty(board_list,pos):

	if board_list[pos-1] == 'O' or board_list[pos-1] == 'X':
		return False
	else:
		return True

def winCheck(board_list,marker):

	i = 0
	if board_list[i] == board_list[i+1] == board_list[i+2] == marker:
		return True
	elif board_list[i+3] == board_list[i+4] == board_list[i+5] == marker:
		return True
	elif board_list[i+6] == board_list[i+7] == board_list[i+8] == marker:
		return True
	elif board_list[i] == board_list[i+3] == board_list[i+6] == marker:
		return True
	elif board_list[i+1] == board_list[i+4] == board_list[i+7] == marker:
		return True
	elif board_list[i+2] == board_list[i+5] == board_list[i+8] == marker:
		return True
	elif board_list[i] == board_list[i+4] == board_list[i+8] == marker:
		return True
	elif board_list[i+2] == board_list[i+4] == board_list[i+6] == marker:
		return True
	else:
		return False

def checkIfBoardFull(board_list):

	if '*' not in board_list:
		return True
	else:
		return False

while True:
	print("Welcome to the tictactoe game")
	print("You will be Player 1 => X")

	board_list = ['*','*','*','*','*','*','*','*','*']
	#method to print out the board
	displayBoard(board_list)

	#method to choose which player will start
	index = startFirst()
	gameOn = True

	while gameOn:
		#Game will go on until somone wins
		if index % 2 == 0:
			#Player one chooses the starting location
			compPos = chooseComputerPos(board_list)
			placerPos(board_list,compPos,'O')
		else:
			#Computer will choose a position
			playerPos = choosePlayerOnePos(board_list)
			placerPos(board_list,playerPos,'X')

		print(" ===============================================")
		displayBoard(board_list)
		index += 1

		#Check if anyone
		if winCheck(board_list,'X'):
			print("Player 1 has won the game")
			break
		elif winCheck(board_list,'O'):
			print("Computer has won the game")
			break
		if checkIfBoardFull(board_list):
			print("The game has been drawn")
			break

	userInput = input("Do you want to play again with the nasty computer [YES/NO] ")
	if userInput == 'YES':
		continue
	else:
		break