'''
About: COMP3608 Assignment 1
Author: Charles Christopher Hyland

----------------------------------------------------------------------------------------------------
Alpha-Beta Algorithm.
----------------------------------------------------------------------------------------------------

'''
from game_actions import *
from game_setup import *
from game_actions import *

def alpha_beta(node, depth, alpha, beta, maximizing_player, original_player):
    '''Minimax algorithm for the board.'''
    if depth == 0:
        if node.win==True:
            if node.player == original_player:
                return 10000
            else:
                return -10000
        return EVALUATION(node.board, original_player)

    if node.win == True:
        return node.value, node
    if maximizing_player==True:
        value = -100000000
        for child in node.children:
            value = alpha_beta(child, depth-1, alpha, beta, False, original_player)
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value
    else:
        value = 100000000
        for child in node.children:
            value = alpha_beta(child, depth-1, alpha, beta, True, original_player)
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value



def move_alpha_beta(node, depth, alpha, beta, maximizing_player, original_player):
    '''Minimax algorithm for the board.'''
    if depth == 0:
        if node.win==True:
            if node.player == original_player:
                return 10000, node
            else:
                return -10000, node
        return EVALUATION(node.board, original_player), node

    if node.win == True:
        return node.value, node
    if maximizing_player==True:
        value = -100000000
        best_node = node.children[0]
        for child in node.children:
            value, best_node = alpha_beta(child, depth-1, alpha, beta, False, original_player)
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return value, best_node
    else:
        value = 100000000
        for child in node.children:
            value = alpha_beta(child, depth-1, alpha, beta, True, original_player)
            beta = min(beta, value)
            if beta <= alpha:
                break
        return value



def move_make(node, depth, maximizing_player, original_player):
    '''Minimax algorithm for the board.'''
    if depth == 0:
        if node.win==True:
            if node.player == original_player:
                return 10000, node
            else:
                return -10000, node
        return EVALUATION(node.board, original_player), node
    
    if node.win == True:
        return node.value, node
    if maximizing_player==True:
        best_value = -100000000
        best_node = node.children[0] # Default
        for child in node.children:
            value, child_node = move_make(child, depth-1, False, original_player)
            if value >= best_value:
                best_value = value
                best_node = child_node
        return best_value, best_node

    else:
        best_value = 100000000
        best_node = node.children[0] # Default
        for child in node.children:
            value, child_node = move_make(child, depth-1, True, original_player)
            if value <= best_value:
                best_value = value
                best_node = child_node
        return best_value, best_node