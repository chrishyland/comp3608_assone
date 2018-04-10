'''
About: COMP3608 Assignment 1
Author: Charles Christopher Hyland

----------------------------------------------------------------------------------------------------
This code will play a game of connect four using the minimax algorithm. There will be a variant of 
the algorithm with and without alpha-beta pruning.
----------------------------------------------------------------------------------------------------

'''

from sys import maxsize # Replacement for infinity value.
from game_setup import * # Contains all functions to set up game


def main():

	initial_state = start_game()
	board = create_board(initial_state['board_state'])
	print(board)
	print_board(board)
	valid = valid_moves(board)
	
	print("")
	
	print("Player r")
	print("SCORE is {}".format(SCORE(board, PLAYER_RED)))

	print("")

	print("Player y")
	print("SCORE is {}".format(SCORE(board, PLAYER_YELLOW)))

	print("Evaluate is {}".format(EVALUATION(board)))


if __name__ == '__main__':
	main()