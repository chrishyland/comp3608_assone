'''
About: COMP3608 Assignment 1
Author: Charles Christopher Hyland

----------------------------------------------------------------------------------------------------
Class for the state nodes and building tree.
----------------------------------------------------------------------------------------------------

'''
from game_actions import *

class State():
	def __init__(self, player, board, move, win, parent=None):
		self.player = player # who's turn to play
		self.board = board
		self.parent = parent # node reference
		self.children = [] # contains all children of this node.
		self.value = 0
		self.move = move
		self.win = win # Check if game is over.


	def create_children(self):
		'''Create children for the current state.'''
		possible_moves = valid_moves(self.board)
		for move in possible_moves:
			# Create children of this current node.
			self.children.append(create_child(parent=self, move=move, board=np.copy(self.board), player_turn=self.player))

			

def create_child(parent, move, board, player_turn):
	'''Creates child node by updating move.'''
	turn_to_play = None 
	if parent.player == PLAYER_YELLOW: # Get opposite player.
		turn_to_play = PLAYER_RED
	else:
		turn_to_play = PLAYER_YELLOW
	row, column = move
	update_row = list(board[row])
	update_row[column] = player_turn
	board[row] = ''.join(update_row)
	if(NUM_IN_A_ROW(4, board, turn_to_play)>0):
		# Game won already.
		return State(player=turn_to_play, board=board, move=move, parent=parent, win=True)
	else:
		return State(player=turn_to_play, board=board, move=move, parent=parent, win=False)


def create_tree(depth, board, player_turn):
	'''Build tree of the whole game.'''
	root = State(player_turn, board, move=None, win=False, parent=None)
	i = 0
	recurse_build(root, i, depth)
	return root


def recurse_build(node, current_depth, depth):
	'''Recursively build the tree.'''
	if current_depth == depth: # base case.
		return
	
	node.create_children() # build children.
	for child in node.children:
		# So that we don't build terminal nodes.
		if child.win == False:
			recurse_build(child, current_depth+1, depth)


def countNodes(node):
   count = 1
   for Child in node.children:
      count +=  countNodes(Child)
   return count