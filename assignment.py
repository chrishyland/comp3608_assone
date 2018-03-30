'''
About: COMP3608 Assignment 1
Author: Charles Christopher Hyland

----------------------------------------------------------------------------------------------------
This code will play a game of connect four using the minimax algorithm. There will be a variant of 
the algorithm with and without alpha-beta pruning.
----------------------------------------------------------------------------------------------------

'''

import networkx as nx
from sys import maxsize # Replacement for infinity value.

RED_COINS = 0 # Define number of coins on board for both players.
YELLOW_COINS = 0

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
	board = input().split(',')
	player = input() # Who's about to play
	algorithm_choice = input()
	max_depth = int(input()) # Depth for algorithm to search

	return {'board_state':board, 'player':player, 
			'algo':algorithm_choice, 'depth': max_depth}

def evaluate(state):
	'''Evaluates the state.'''
	return SCORE(state, red player) – SCORE(state, yellow player)


def min_max():
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
	# Need to generate all games possibles and assign values to them
	print(initial_state)


if __name__ == '__main__':
	main()

