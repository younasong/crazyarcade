# Youna Song (younas)
# 12/07/2017
# 15-112 Term Project

"""
This file contains classes for Obstacles
Draws obstacles on the screen 
"""

import pygame 
from constants import *

# obstacle superclass 
class Obstacle(pygame.sprite.Sprite):

    def __init__(self, row, col): 
        super().__init__()
        self.row = row
        self.col = col 
        self.size = 60 
        
    def drawObstacle(self, screen): 
        pass
                    
# CRATE OBSTACLE 
class Crate(Obstacle): 
    def initCrate(self): 
        s = self.size  
        self.crate = pygame.image.load("graphics/obstacles/crate.png")
        self.crate = pygame.transform.scale(self.crate, (s,s))
        
    def __init__(self, row, col): 
        super().__init__(row, col)
        self.initCrate()
        
        # create crate rect 
        self.rect = self.crate.get_rect()
        self.rect.x = MARGIN + col*self.size
        self.rect.y = MARGIN + row*self.size
    
    # draw crate
    def drawObstacle(self ,screen, board): 
        s, m = CELL_SIZE, MARGIN
        r, c = self.row, self.col
        if board[r][c] != None: 
            screen.blit(self.crate, (m+c*s, m+r*s))
        
# CHEST OBSTACLE 
class Chest(Obstacle): 
    def initChest(self): 
        s = self.size  
        self.chest = pygame.image.load("graphics/obstacles/bluechest.png")
        self.chest = pygame.transform.scale(self.chest, (s,s))
        
    def __init__(self, row, col): 
        super().__init__(row, col)
        self.initChest()
        
        # create chest rect
        self.rect = self.chest.get_rect()
        self.rect.x = MARGIN + col*self.size
        self.rect.y = MARGIN + row*self.size
    
    # draw chest
    def drawObstacle(self ,screen, board): 
        s, m = CELL_SIZE, MARGIN
        r, c = self.row, self.col
        if board[r][c] != None: 
            screen.blit(self.chest, (m+c*s, m+r*s))
            