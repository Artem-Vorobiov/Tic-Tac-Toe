import os
import time
import random

# Define the board
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

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

while True:
	os.system('Clear')
	print_the_header()
	print_board()

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
	if 	(board[1] == 'X' and board[2] == 'X' and board[3] == 'X') or \
		(board[4] == 'X' and board[5] == 'X' and board[6] == 'X') or \
		(board[7] == 'X' and board[8] == 'X' and board[9] == 'X') or \
		(board[1] == 'X' and board[4] == 'X' and board[7] == 'X') or \
		(board[2] == 'X' and board[5] == 'X' and board[8] == 'X') or \
		(board[3] == 'X' and board[6] == 'X' and board[9] == 'X') or \
		(board[1] == 'X' and board[5] == 'X' and board[9] == 'X') or \
		(board[7] == 'X' and board[5] == 'X' and board[3] == 'X'):
		os.system('Clear')
		print_the_header()
		print_board()
		print('\n\n\t\t\t\t_______ -----TAC----- _______\n\n\n')
		break

		
