'''
About: COMP3608 Assignment 1
Author: Charles Christopher Hyland

----------------------------------------------------------------------------------------------------
This code will play a game of connect four using the minimax algorithm. There will be a variant of 
the algorithm with and without alpha-beta pruning.
----------------------------------------------------------------------------------------------------

'''
from sys import maxsize # Replacement for infinity value.
import numpy as np
import sys
ROW = 6 # These are constant for the board.
COLUMN = 7
PLAYER_RED = 'r'
PLAYER_YELLOW = 'y'


def start_game():
	'''Initialises the game and return dict.'''
	parameters = sys.argv
	board = parameters[1].split(',')
	player = "" # Who's about to play
	if parameters[2] == 'red':
		player = 'r'
	else:
		player = 'y'
	algorithm_choice = parameters[3]
	max_depth = int(parameters[4]) # Depth for algorithm to search
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

def get_opposite_player(player):
	'''Return opposite player.'''
	if(player == PLAYER_RED):
		return PLAYER_YELLOW
	else:
		return PLAYER_RED

def has_won(array_board, player):
	'''Check if player has won.'''
	if(NUM_IN_A_ROW(4, array_board, player) != 0):
		return 1
	else:
		return 0


def update_board(move, array_board, parent):
	'''Updates the board for new player.'''
	array_board[move[0]][move[1]] = get_opposite_player(parent)
	return array_board

def is_sequence_horizontal(i, j, count, player, array_board):
	'''Checks whether horizontal sequence of length count for player'''
	
	if(within_range(i, j-1) and array_board[i][j-1] == player):
		return 0 # Current token is part of previous sequence
	if(within_range(i, j+count) and array_board[i][j+count] == player):
		return 0 # Part of longer sequence.
	track = 0
	for step in range(0, count):
		if(within_range(i, j+step)):
			if(array_board[i][j+step] != player):
				return 0
			track +=1 # To ensure if only 1 token at end, doesn't break
	
	if(track != count):
		return 0
	return 1


def is_sequence_vertical(i, j, count, player, array_board):
	'''Checks whether vertical sequence of length count for player'''
	
	if(within_range(i-1, j) and array_board[i-1][j] == player):
		return 0 # Current token is part of previous sequence
	
	if(within_range(i+count, j) and array_board[i+count][j] == player):
		return 0 # Part of longer sequence.
	track = 0
	for step in range(0, count):
		if(within_range(i+step, j)):
			if(array_board[i+step][j] != player):
				return 0
			track +=1 # To ensure if only 1 token at end, doesn't break
	
	if(track != count):
		return 0
	return 1


def is_sequence_right_diagonal(i, j, count, player, array_board):
	'''Checks whether right diagonal sequence of length count for player'''
	
	if(within_range(i-1, j-1) and array_board[i-1][j-1] == player):
		return 0 # Current token is part of previous sequence
	
	if(within_range(i+count, j+count) and array_board[i+count][j+count] == player):
		return 0 # Part of longer sequence.
	track = 0
	for step in range(0, count):
		if(within_range(i+step, j+step)):
			if(array_board[i+step][j+step] != player):
				return 0
			track +=1 # To ensure if only 1 token at end, doesn't break
	
	if(track != count):
		return 0
	return 1


def is_sequence_left_diagonal(i, j, count, player, array_board):
	'''Checks whether left diagonal sequence of length count for player'''
	
	if(within_range(i-1, j+1) and array_board[i-1][j+1] == player):
		return 0 # Current token is part of previous sequence


	if(within_range(i+count, j-count) and array_board[i+count][j-count] == player):
		return 0 # Part of longer sequence.

	track = 0
	for step in range(0, count):
		if(within_range(i+step, j-step)):
			if(array_board[i+step][j-step] != player):
				return 0
			track +=1 # To ensure if only 1 token at end, doesn't break
	
	if(track != count):
		return 0
	return 1


def NUM_IN_A_ROW(count, array_board, player):
	'''Computes the number in a row for a player with a given state.'''
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


def SCORE(array_board, player):
	'''Computes the SCORE of a player.'''
	return count_total_tokens(array_board, player) + (10*NUM_IN_A_ROW(2, array_board, player)) + (100*NUM_IN_A_ROW(3, array_board, player)) + (1000*NUM_IN_A_ROW(4, array_board, player))


def count_total_tokens(array_board, player):
	'''Count total number of tokens player has on board'''
	count = 0
	for i in range(0, ROW):
		for j in range(0, COLUMN):
			if(array_board[i][j] == player):
				count += 1
	return count


def valid_moves(array_board):
	'''Figures out valid moves from NUMPY array and stores coordinates.'''
	moves_can_make = []
	for j in range(0, COLUMN):
		for i in range(0, ROW):
			if(array_board[i][j] == '.'):
				moves_can_make.append((i, j))
				break
	return moves_can_make


def EVALUATION(array_board, PLAYER):
	'''Evaluates the state.'''
	if PLAYER == PLAYER_RED:
		return SCORE(array_board, PLAYER_RED) - SCORE(array_board, PLAYER_YELLOW)
	else:
		return SCORE(array_board, PLAYER_YELLOW) - SCORE(array_board, PLAYER_RED)

def min_max(node, depth, maximizing_player, original_player):
    '''Minimax algorithm for the board.'''
    if depth == 0:
        return EVALUATION(node.board, original_player)

    # NEED TO CHECK IF TERMINAL NODE.

    if maximizing_player==True:
        best_value = -100000000
        for child in node.children:
            value = min_max(child, depth-1, False, original_player)
            best_value = max(best_value, value)
            return best_value
    else:
        best_value = 100000000
        for child in node.children:
            value = min_max(child, depth-1, True, original_player)
            best_value = min(best_value, value)
            return best_value


class State():
	def __init__(self, player, board, parent=None):
		self.player = player
		self.board = board
		self.parent = parent # node reference
		self.children = [] # contains all children of this node.
		self.value = 0


	def create_children(self):
		'''Create children for the current state.'''
		player_turn = None 
		if self.player == PLAYER_YELLOW: # Get opposite player.
			player_turn = PLAYER_RED
		else:
			player_turn = PLAYER_YELLOW

		possible_moves = valid_moves(self.board)
		for move in possible_moves:
			# Create children of this current node.
			self.children.append(create_child(self, move, np.copy(self.board), player_turn))
			

def create_child(parent, move, board, player_turn):
	'''Creates child node by updating move.'''
	row, column = move
	update_row = list(board[row])
	update_row[column] = player_turn
	board[row] = ''.join(update_row)
	return State(player=player_turn, board=board, parent=parent)


def create_tree(depth, board, player_turn):
	'''Build tree of the whole game.'''
	root = State(player_turn, board, None)
	i = 0
	recurse_build(root, i, depth)
	return root


def recurse_build(node, current_depth, depth):
	'''Recursively build the tree.'''
	if current_depth == depth: # base case.
		return
	
	node.create_children() # build children.
	for child in node.children:
		recurse_build(child, current_depth+1, depth)


def countNodes(node):
   count = 1
   for Child in node.children:
      count +=  countNodes(Child)
   return count

def main():
	
	initial_state = start_game()
	board = create_board(initial_state['board_state'])
	valid = valid_moves(board)

	# Create game tree.
	root = create_tree(initial_state['depth'], board, initial_state['player'])
	print(min_max(root, initial_state['depth'], True, root.player))

	
	print(countNodes(root)+7) # Add seven since need to check root's children

if __name__ == '__main__':
	main()