# Youna Song (younas)
# 12/07/2017
# 15-112 Term Project

"""This file is responsible for the creation of boards 
   Boards can be made using a list containing strings with certain characters
   representing objects such as obstacles and monsters on the board 
"""

from constants import * 
from obstacles import * 
from monster import * 
from items import *

# makes board using a given boardString 
# 'c' = Crate, 'h' = Chest, 'b' = Bomb, 's' = Skates, 'f' = Flask, 'l' = BalloonItem 
def makeBoard(L): 
    board = [[None] * COLS for i in range(ROWS)]
    obstacles = []
    monsters = []
    items = [] 
    
    for row in range(ROWS): 
        for col in range(COLS): 
            cell = L[row][col] 
            if cell == 'c': 
                board[row][col] = Crate(row, col)
                obstacles += [Crate(row, col)]
            elif cell == 'h': 
                board[row][col] = Chest(row, col)
                obstacles += [Chest(row, col)]
            elif cell == 'b':  
                board[row][col] = Bomb(row, col)
                monsters += [Bomb(row, col)]
            elif cell == 's': 
                board[row][col] = Skates(row, col)
                items += [Skates(row, col)]
            elif cell == 'f': 
                board[row][col] = Flask(row, col)
                items += [Flask(row, col)]
            elif cell == 'l': 
                board[row][col] = BalloonItem(row, col)
                items += [BalloonItem(row, col)]
            elif cell == 'g': 
                board[row][col] = Gold(row, col)
                items += [Gold(row, col)]
            
    return board, obstacles, monsters, items
                
    
def board1(): 

    # boardOutline = ['ccccccccccccc',
    #                 'c           c',
    #                 'c   b    b  c', 
    #                 'c           c', 
    #                 'c  hhhhhhh  c',
    #                 'c  hl   gh  c',
    #                 'c  h     h  c',
    #                 'c  h    sh  c',
    #                 'c  hhhhhhh  c',
    #                 'c           c',
    #                 'c   b    b  c', 
    #                 'c           c', 
    #                 'ccccccccccccc']
    
    # Easier board for demonstration purposes 
    boardOutline = ['ccccccccccccc',
                    'c           c',
                    'c           c', 
                    'c           c', 
                    'c  hhhhhhh  c',
                    'c  hl   gh  c',
                    'c  h     h  c',
                    'c  h    fh  c',
                    'c  hhhhhhh  c',
                    'c           c',
                    'c   b       c', 
                    'c           c', 
                    'ccccccccccccc']
    # #             
    return makeBoard(boardOutline)
        
def board2(): 
    # boardOutline = ['   b     b   ', 
    #                 'chchchchchchc', 
    #                 '             ',
    #                 'hchchchchchch', 
    #                 '      b      ', 
    #                 'chchchchchchc', 
    #                 ' l        s  ', 
    #                 'hchchchchchch',
    #                 '      b      ',
    #                 'chchchchchchc', 
    #                 '             ', 
    #                 'hchchchchchch', 
    #                 '  b     b    ']
    boardOutline = ['             ', 
                    'chchchchchchc', 
                    '             ',
                    'hchchchchchch', 
                    '      b      ', 
                    'chchchchchchc', 
                    '             ', 
                    'hchchchchchch',
                    '             ',
                    'chchchchchchc', 
                    '             ', 
                    'hchchchchchch', 
                    '              ']
    return makeBoard(boardOutline)
    
def board3(): 
    boardOutline = ['cc    b    cc',
                    'ch    b    hc', 
                    '     ccc     ',
                    '  cc  s  cc  ',
                    '  cc ccc cc  ', 
                    'b cc ccc cc b', 
                    '  cc     cc  ', 
                    '  cc     cc  ', 
                    '             ', 
                    '  hhhhhhhhh  ', 
                    '             ', 
                    'ch    b    hc', 
                    'cc  l b f  cc']
                    
                    
    return makeBoard(boardOutline)
    
        