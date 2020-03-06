import os
import time
import random

# Define the board
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

def print_the_header():
	print('\n\n\t\t\t\t_______ TIC--TAC--TOE_______\n\n\n')

def print_board():
	print('    |    |    ')
	print('  '+board[0]+' | '+board[1]+'  | '+board[2]+' ')
	print('    |    |    ')
	print('----|----|----')
	print('    |    |    ')
	print('  '+board[3]+' | '+board[4]+'  | '+board[5]+' ')
	print('    |    |    ')
	print('----|----|----')
	print('    |    |    ')
	print('  '+board[6]+' | '+board[7]+'  | '+board[8]+' ')
	print('    |    |    ')

while True:
	os.system('Clear')
	print_the_header()
	print_board()

	choice = input('Please, choose an empty space for X. Type a digit from 0 to 8: ')
	choice = int(choice)

	# Check to see if the space is empty first
	if board[choice] == ' ':
		board[choice] = 'X'
	else:
		print('Sorry, that space is not empty')
		time.sleep(2)

