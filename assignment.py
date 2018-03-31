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

# SCORE(state, player):
# 	return number of tokens of player’s colour +
#           10 * NUM_IN_A_ROW(2, state, player) +
#           100 * NUM_IN_A_ROW(3, state, player) +
#           1000 * NUM_IN_A_ROW(4 or more, state, player)

# NUM_IN_A_ROW(count, state, player):
# 	'''returns the number of times that <state> contains a <count>‐in‐a‐row for the given <player>'''


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


def print_board(array_board):
	'''Print out board.'''
	for i in range(ROW-1, 0, -1):
		for j in range(0, COLUMN):
			print(array_board[i][j], end=' ')
		print()


def valid_moves(array_board):
	'''Figures out valid moves from NUMPY array.'''
	moves_can_make = [] # Stores co-ordinates of where can play

	for i in range(ROW-1, 0, -1):
		for j in range(0, COLUMN):
			

			print(array_board[i][j], end=' ')
		print()


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
	valid_moves(board)


if __name__ == '__main__':
	main()

