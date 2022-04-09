#!/bin/python

#function that can print out a board 3x3

def display_board(board):
	
	index = 0
	for i in board:
		if index == 2 or index == 5 or index == 8:
			print(i)
		else:
			print(i),
		index += 1

#test_board = ['#','X','O','X','O','X','O','X','O']
#display_board(test_board)

def player_input():
	
	result = input("Enter the position where you would like to place the item => ")
	
	newlist = [1,2,3,4,5,6,7,8,9]	

	while result not in newlist:
		result = int(input("Enter the position where you would like to place the item => "))
	
	return result

def place_marker(board,marker,position):
	
	board[position - 1] = marker

def win_check(board,mark):
	
	i = 0
	
	if board[i] == board[i+1] == board[i+2] == mark:
		return True
	elif board[i+3] == board[i+4] == board[i+5] == mark:
		return True
	elif board[i+6] == board[i+7] == board[i+8] == mark:
		return True
	elif board[i] == board[i+3] == board[i+6] == mark:
		return True
	elif board[i+1] == board[i+4] == board[i+7] == mark:
		return True
	elif board[i+2] == board[i+5] == board[i+8] == mark:
		return True
	elif board[i] == board[i+4] == board[i+8] == mark:
		return True
	elif board[i+2] == board[i+4] == board[i+6] == mark:
		return True
	else:
		return False

#print(win_check(test_board,'X'))
#print(win_check(test_board,'O'))

import random

def choose_first():
	
	return random.randint(1,2)

def space_check(board,position):
	
	if board[position-1] == 'X' or board[position-1] == 'O':
		return False
	else:
		return True

def full_board_check(board):
	
	total = 0
	for i in board:
		if i == 'X' or i == 'O':
			total += 1
	
	return total == len(board)

def player_choice(board):

	user_input = int(input("Enter your next position : "))
	check_pos = space_check(board,user_input)
	
	if check_pos:
		return user_input
	else:
		return null

def replay():
	
	user_input = ("Do you want to play again ? [Yes/No] ")
	if user_input == 'Yes':
		return True
	else:
		return False

print("Welcome to tictac to !!!")

while True:
	board = ['*','*','*','*','*','*','*','*','*']
	display_board(board)
	
	player = choose_first()
	if player == 1:
		index = 2
	else:
		index = 3

	game_on = True
	
	winner = ''
	
	while game_on:
		
		if index % 2 == 0:
			player_marker = 'X'
			print("Player 1 turn ")
		else:
			player_marker = 'O'
			print("Player 2 turn ")
		
		pos = player_input()
	
		while not space_check(board,pos):
			print("This space is already taken !!!")
			pos = player_input()
		
		place_marker(board,player_marker,pos)
			
		index += 1
		print("=================================== \n")
		display_board(board)
		
		if win_check(board,'X'):
			game_on = False
			winner = 'Player 1'
	
		elif win_check(board,'O'):
			game_on = False
			winner = 'Player 2'

		if full_board_check(board):
			game_on = False		
	
	if winner == 'Player 1':
		print("Player 1 won the game")
	elif winner == 'Player 2':
		print("Player 2 won the game")
	else:
		print("The game has been drawn")
	
	if not replay():
		break
