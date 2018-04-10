'''
About: COMP3608 Assignment 1
Author: Charles Christopher Hyland

----------------------------------------------------------------------------------------------------
Class to store states.
----------------------------------------------------------------------------------------------------

'''

class board(Object):
	def __init__(self, i_depth, i_player, i_value, state):
		self.i_depth = i_depth
		self.i_player = i_player
		self.i_value = i_value
		self.state = state
		self.children = [] # Contains all children of this node.


	def create_children():
		'''Generates children for nodes we create.'''

	