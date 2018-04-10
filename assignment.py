'''
About: COMP3608 Assignment 1
Author: Charles Christopher Hyland

----------------------------------------------------------------------------------------------------
This code will play a game of connect four using the minimax algorithm. There will be a variant of 
the algorithm with and without alpha-beta pruning.
----------------------------------------------------------------------------------------------------

'''

import numpy as np
from sys import maxsize # Replacement for infinity value.

RED_COINS = 0 # Define number of coins on board for both players.
YELLOW_COINS = 0
ROW = 6 # These are constant for the board.
COLUMN = 7

# UTILITY(state):
# 	'''Computes the utility of the player.'''
# 	if red is winner:
#            return 10000
#     if yellow is winner
#           return ‐10000




def start_game():
	'''Initialises the game and return dict.'''
	parameters = input().split(' ')
	board = parameters[0].split(',')
	player = parameters[1] # Who's about to play
	algorithm_choice = parameters[2]
	max_depth = int(parameters[3]) # Depth for algorithm to search
	
	return {'board_state':board, 'player':player, 
			'algo':algorithm_choice, 'depth': max_depth}


def create_board(list_of_states):
	'''Create NUMPY array from list of lists.'''
	return np.array([np.array(row) for row in list_of_states])


def within_range(i, j):
	'''Check if outside of bound.'''
	if i >= ROW or j >= COLUMN or i < 0 or j < 0:
		return False
	return True


def print_board(array_board):
	'''Print out board.'''
	for i in range(ROW-1, -1, -1):
		for j in range(0, COLUMN):
			print(array_board[i][j], end=' ')
		print()

# NUM_IN_A_ROW(count, state, player):
# 	'''returns the number of times that <state> contains a <count>‐in‐a‐row for the given <player>'''


def is_sequence_horizontal(i, j, count, player, array_board):
	'''Checks whether horizontal sequence of length count for player'''
	
	if(within_range(i, j-1) and array_board[i][j-1] == player):
		return 0 # Current token is part of previous sequence

	track = 0
	for step in range(0, count):
		if(within_range(i, j+step)):
			if(array_board[i][j+step] != player):
				return 0
			track +=1 # To ensure if only 1 token at end, doesn't break
	
	if(track != count):
		return 0

	if(within_range(i, j+count) and array_board[i][j+count] == player):
		return 0 # Part of longer sequence.
	else:
		return 1


def is_sequence_vertical(i, j, count, player, array_board):
	'''Checks whether vertical sequence of length count for player'''
	
	if(within_range(i-1, j) and array_board[i-1][j] == player):
		return 0 # Current token is part of previous sequence
	
	track = 0
	for step in range(0, count):
		if(within_range(i+step, j)):
			if(array_board[i+step][j] != player):
				return 0
			track +=1 # To ensure if only 1 token at end, doesn't break
	
	if(track != count):
		return 0

	if(within_range(i+count, j) and array_board[i+count][j] == player):
		return 0 # Part of longer sequence.
	else:
		return 1


def is_sequence_right_diagonal(i, j, count, player, array_board):
	'''Checks whether right diagonal sequence of length count for player'''
	
	if(within_range(i-1, j-1) and array_board[i-1][j-1] == player):
		return 0 # Current token is part of previous sequence
	
	track = 0
	for step in range(0, count):
		if(within_range(i+step, j+step)):
			if(array_board[i+step][j+step] != player):
				return 0
			track +=1 # To ensure if only 1 token at end, doesn't break
	
	if(track != count):
		return 0

	if(within_range(i+count, j+count) and array_board[i+count][j+count] == player):
		return 0 # Part of longer sequence.
	else:
		return 1


def is_sequence_left_diagonal(i, j, count, player, array_board):
	'''Checks whether left diagonal sequence of length count for player'''
	
	if(within_range(i-1, j+1) and array_board[i-1][j+1] == player):
		return 0 # Current token is part of previous sequence
	
	track = 0
	for step in range(0, count):
		if(within_range(i+step, j-step)):
			if(array_board[i+step][j-step] != player):
				return 0
			track +=1 # To ensure if only 1 token at end, doesn't break
	
	if(track != count):
		return 0

	if(within_range(i+count, j-count) and array_board[i+count][j-count] == player):
		return 0 # Part of longer sequence.
	else:
		return 1


def num_in_a_row(count, array_board, player):
	'''Computes the number in a row for a player with a given state.'''
	num_counts = 0
	num_vert = 0
	num_hor = 0
	num_diag_r = 0
	num_diag_l = 0
	for i in range(0, ROW):
		for j in range(0, COLUMN):
			if(array_board[i][j] == player):
				# We found a sequence to begin
				num_hor += is_sequence_horizontal(i, j, count, player, array_board)
				num_vert += is_sequence_vertical(i, j, count, player, array_board)
				num_diag_r += is_sequence_right_diagonal(i, j, count, player, array_board)
				num_diag_l += is_sequence_left_diagonal(i, j, count, player, array_board)
	
	return (num_hor + num_vert + num_diag_r + num_diag_l)


def score(array_board, player):
	'''Computes the score of a player.'''
	return count_total_tokens(array_board, player) + (10*num_in_a_row(2, array_board, player)) + (100*num_in_a_row(3, array_board, player)) + (1000*num_in_a_row(4, array_board, player))


def count_total_tokens(array_board, player):
	'''Count total number of tokens player has on board'''
	count = 0
	for i in range(0, ROW):
		for j in range(0, COLUMN):
			if(array_board[i][j] == player):
				count += 1
	return count


		# When you find a token, check if next to it is the same and start counting
			# Need to make sure token before it is not the same token.
			# Make sure only apply to r or y characters.
			# Apply it count number of times and if its exactly satisfies, then use the score



# def compute_score(array_board):
# 	'''Computes the score based on the number of tokens.'''


# SCORE(state, player):
# 	return number of tokens of player’s colour +
#           10 * NUM_IN_A_ROW(2, state, player) +
#           100 * NUM_IN_A_ROW(3, state, player) +
#           1000 * NUM_IN_A_ROW(4 or more, state, player)


def valid_moves(array_board):
	'''Figures out valid moves from NUMPY array and stores coordinates.'''
	moves_can_make = []
	for j in range(0, COLUMN):
		for i in range(0, ROW):
			if(array_board[i][j] == '.'):
				moves_can_make.append((i, j))
				break
	return moves_can_make


def valid_coordinate(row, column):
	'''Checks if coordinate to be evaluated is within board.'''
	if row>=ROW or row<0:
		return 0
	if column>=COLUMN or column<0:
		return 0
	return 1 # No issues with board


# def evaluate(state):
# 	'''Evaluates the state.'''
# 	return SCORE(state, red player) – SCORE(state, yellow player)


#def min_max():
	# Need to define minmax algorithm

	# Take the depth factor so we know how much of the tree we should traverse.
	# DFS and evaluate. 
		# At the leaves, check the utility of the move.
		# Return the highest value and which one to traverse
	# Choose the min, max etc
	# Traverse the path
	# Need to check has the game ended or not as well

def main():

	initial_state = start_game()
	board = create_board(initial_state['board_state'])
	print(board)
	print_board(board)
	valid = valid_moves(board)
	
	print("")
	
	print("Player r")
	print("Score is {}".format(score(board, 'r')))

	print("")

	print("Player y")
	print("Score is {}".format(score(board, 'y')))







	

if __name__ == '__main__':
	main()