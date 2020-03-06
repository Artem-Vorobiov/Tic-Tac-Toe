import os
import time
import random

# Define the board
board = ['',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def print_the_header():
	print('\n\n\t\t\t\t_______ TIC--TAC--TOE _______\n\n\n')

def print_board():
	print('    |    |    ')
	print('  '+board[1]+' | '+board[2]+'  | '+board[3]+' ')
	print('    |    |    ')
	print('----|----|----')
	print('    |    |    ')
	print('  '+board[4]+' | '+board[5]+'  | '+board[6]+' ')
	print('    |    |    ')
	print('----|----|----')
	print('    |    |    ')
	print('  '+board[7]+' | '+board[8]+'  | '+board[9]+' ')
	print('    |    |    ')

def is_winner(board, player):
	if (board[4] == player and board[5] == player and board[6] == player) or \
		(board[7] == player and board[8] == player and board[9] == player) or \
		(board[1] == player and board[4] == player and board[7] == player) or \
		(board[2] == player and board[5] == player and board[8] == player) or \
		(board[3] == player and board[6] == player and board[9] == player) or \
		(board[1] == player and board[5] == player and board[9] == player) or \
		(board[7] == player and board[5] == player and board[3] == player):
		return True
	else:
		return False

def is_board_full(board):
	if ' ' in board:
		return False 
	else:
		return True
def screen():
	os.system('Clear')
	print_the_header()
	print_board()

	


while True:
	screen()
	# Get Player X Input
	choice = input('Please, choose an empty space for X. Type a digit from 0 to 8: ')
	choice = int(choice)

	# Check to see if the space is empty first
	if board[choice] == ' ':
		board[choice] = 'X'
	else:
		print('Sorry, that space is not empty')
		time.sleep(2)

	# Check for X win
	if is_winner(board, 'X'):
		os.system('Clear')
		print_the_header()
		print_board()
		print('\n\n\t\t\t\t______ -----X WINS----- ______\n\n\n')
		break

	screen()

	# Check for a tie (is the board full)
	if is_board_full(board):
		print('\n\n\t\t\t\t______ -----TIE----- ______\n\n\n')
		break




	# Get Player O Input
	choice = input('Please, choose an empty space for O. Type a digit from 0 to 8: ')
	choice = int(choice)

	# Check to see if the space is empty first
	if board[choice] == ' ':
		board[choice] = 'O'
	else:
		print('Sorry, that space is not empty')
		time.sleep(2)

	# Check for X win
	if 	is_winner(board, 'Y'):
		os.system('Clear')
		print_the_header()
		print_board()
		print('\n\n\t\t\t\t______ -----O WINS----- ______\n\n\n')
		break

	# Check for a tie (is the board full)
	if is_board_full(board):
		print('\n\n\t\t\t\t______ -----TIE----- ______\n\n\n')
		break




















