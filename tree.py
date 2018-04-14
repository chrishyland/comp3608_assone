'''
About: COMP3608 Assignment 1
Author: Charles Christopher Hyland

----------------------------------------------------------------------------------------------------
Class to store game tree.
----------------------------------------------------------------------------------------------------

'''

# https://tonypoer.io/2016/10/08/recursively-parsing-a-list-of-lists-into-a-game-tree-using-python/
from node import *
from game_setup import *
from game_actions import *

class Tree():

	def __init__(self):
		self.root = None


	def initailise_tree(self, player, initial_board):
		'''Build the whole tree.'''
		self.root = Node(player, EVALUATION(initial_board, player), initial_board)
		

	def build_tree(self, depth, board):
		'''Generate possible moves from the board.'''
		moves_valid = valid_moves(self.root.board) # Moves valid from first move.
		print(moves_valid)
		for move in moves_valid:
			#for elem in data_list:
			#self.parse_subtree(elem, self.root)
			self.build_children(move, board, self.root, depth)
			# get the move and the board
			# combine to create a new board with all the costs etc
			# indicate which player as well is playing
			# ensure we repeat this board creating thing certain number of times

	def build_children(move, board, parent, depth):
		'''Build child nodes with parents.'''

	
	def addChild(self, childNode):
		'''Add child node to list of children.'''
		self.children.append(childNode)


	def parse_subtree(self, data_list, parent):
		# base case
		if type(data_list) is tuple:
			# make connections
			leaf_node = Node(data_list[0])
			leaf_node.parent = parent
			# if we're at a leaf, set the value
			if len(data_list) == 2:
				leaf_node.value = data_list[1]
			return

		# recursive case
		tree_node = Node(data_list.pop(0))
		# make connections
		tree_node.parent = parent
		parent.addChild(tree_node)
		for elem in data_list:
			self.parse_subtree(elem, tree_node)
		# return from entire method if base case and recursive case both done running
		return