'''
About: COMP3608 Assignment 1
Author: Charles Christopher Hyland

----------------------------------------------------------------------------------------------------
This is testing purposes and used to modularise the code.
----------------------------------------------------------------------------------------------------

'''
import sys
from game_setup import * # Contains all functions to set up game
from game_actions import *
from state import *
from minmax import *
from alpha_beta import *

def main():

	initial_state = start_game()
	board = create_board(initial_state['board_state'])

	# Create game tree.
	root = create_tree(initial_state['depth'], board, initial_state['player'])
	#print(min_max(root, initial_state['depth'], True, root.player))
	
	if initial_state['algo'] == 'M':
		# Minimax algorithm.
		print(move_make(root, initial_state['depth'], True, root.player)[1].move[1])
	
		print(countNodes(root))

	else:
		print(move_make(root, initial_state['depth'], True, root.player)[1].move[1])
		#print(alpha_beta(root, initial_state['depth'], -100000000, 100000000, True, initial_state['player']))
		
	

if __name__ == '__main__':
	main()