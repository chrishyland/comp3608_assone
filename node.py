'''
About: COMP3608 Assignment 1
Author: Charles Christopher Hyland

----------------------------------------------------------------------------------------------------
Class for the state nodes.
----------------------------------------------------------------------------------------------------

'''

class Node():
	def __init__(self, player, value, board, parent=None):
		self.player = player
		self.value = value # evaluation function value.
		self.board = board
		self.parent = parent # node reference
		self.children = [] # contains all children of this node.