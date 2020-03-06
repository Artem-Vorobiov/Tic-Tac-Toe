import os
import time
import random

# Define the board
board = ['',' ',' ',' ',' ',' ',' ',' ',' ',' ']
lap = 1
v1 = False
v2 = False
v3 = False
v4 = False

tactic1 = False
# tactic2 = False

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


# def game_AI(board):
# 	while True:
# 		if lap == 1:
# 			choice = board[5]

# 		if lap == 2:
# 			if board[2] =='X':
# 				choice = board[7]
# 			elif board[4] =='X':
# 				choice = board[9]
# 			elif board[6] =='X':
# 				choice = board[7]
# 			elif board[8] =='X':
# 				choice = board[1]

# 		if lap == 3:
# 			if board[3] == ' ':
# 				choice = board[3]
# 			else:
# 				choice = board[9]

# 			if board[9] == ' ':
# 				choice = board[9]
# 			else:
# 				choice = board[7]

# 			if board[1] == ' ':
# 				choice = board[1]
# 			else:
# 				choice = board[6]
def game_else(board):
	while True:
		choice = random.randint(1,9)
		if board[choice] == ' ':
			board[choice] = 'Y'
			return board[choice]
			break



def game_AI(board, lap):

##### ----> 1	
	# if lap == 1:
	# 	board[5] = 'Y'

##### ----> 2
	if lap == 2:
		if board[2] =='X':
			board[7] = 'Y'
		elif board[4] =='X':
			board[9] = 'Y'
		elif board[6] =='X':
			board[7] = 'Y'
		elif board[8] =='X':
			board[1] = 'Y'
##### ----> 3
	if lap == 3 and board[2] == 'X':
		if board[3] == ' ':
			board[3] = 'Y'
		else:
			board[1] = 'Y'
		global v1
		v1 = True

	elif lap == 3 and board[4] == 'X':
		if board[1] == ' ':
			board[1] = 'Y'
		else:
			board[7] = 'Y'
		global v2
		v2 = True

	elif lap == 3 and board[6] == 'X':
		if board[3] == ' ':
			board[3] = 'Y'
		else:
			board[9] = 'Y'
		global v3
		v3 = True


	elif lap == 3 and board[8] == 'X':
		if board[9] == ' ':
			board[9] = 'Y'
		else:
			board[7] = 'Y' ##

		global v4
		v4 = True


##### ----> 4 
	if lap == 4 and board[2] == 'X' and board[3] == 'X' and v1 == True:
		if board[4] == 'X':
			board[9] = 'Y'
		elif board[9] == 'X':
			board[4] = 'Y'
		else:
			board[4] = 'Y'

	elif lap == 4 and board[8] == 'X' and board[9] == 'X':
		if board[3] == 'X':
			board[4] = 'Y'
		elif board[4] == 'X':
			board[3] = 'Y'
		else:
			board[4] = 'Y'

	elif lap == 4 and board[3] == 'X' and board[6] == 'X' and v3 == True:
		if board[1] == 'X':
			board[8] = 'Y'
		elif board[8] == 'X':
			board[1] = 'Y'
		else:
			board[1] = 'Y'

	elif lap == 4 and board[4] == 'X' and board[1] == 'X':
		if board[3] == 'X':
			board[8] = 'Y'
		elif board[8] == 'X':
			board[3] = 'Y'
		else:
			board[8] = 'Y'




while True:


	if lap == 1:
		board[5] = 'Y'
	elif lap == 2:
		if board[2] == 'X' or board[4] == 'X' or board[6] == 'X' or board[8] == 'X':
			game_AI(board, lap)
			tactic1 = True
		else:
			game_else(board)
	elif lap > 2:
		if tactic1:
			game_AI(board, lap)
		else:
			game_else(board)
	

	if 	is_winner(board, 'Y'):
		os.system('Clear')
		print_the_header()
		print_board()
		print('\n\n\t\t\t\t______ -----Y WINS----- ______\n\n\n')
		break

	screen()
	
	# Check for a tie (is the board full)
	if is_board_full(board):
		print('\n\n\t\t\t\t______ -----TIE----- ______\n\n\n')
		break





	# Get Player X Input
	choice = input('Please, choose an empty space for X. Type a digit from 0 to 8: ')
	choice = int(choice)
	lap += 1

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

	# lap += 1





############################### AI His ... 

















