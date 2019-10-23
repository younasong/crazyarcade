# Youna Song (younas)
# 12/07/2017
# 15-112 Term Project

"""
This file contains classes for Items. It controls the drawing of items and 
each of their attributes 
"""

import pygame 
from constants import *
from screens import * 

# item superclass 
class Item(pygame.sprite.Sprite):
    
    def __init__(self, row, col): 
        super().__init__()
        self.size = 60
        self.row = row
        self.col = col 
        
    def drawItem(self): 
        pass
        
    def useItem(self, hero, items, board, goldEarned): 
        return goldEarned
   
# FLASK ITEM 
class Flask(Item): 

    # initializes Flask graphics 
    def initFlask(self): 
        s = self.size
        self.flask = pygame.image.load("graphics/items/flask.png")
        self.flask = pygame.transform.scale(self.flask, (s,s))
        
    def __init__(self, row, col) :
        super().__init__(row, col)
        self.initFlask()
        
        # creates flask rect
        self.rect = self.flask.get_rect()
        self.rect.x = MARGIN + col*CELL_SIZE
        self.rect.y = MARGIN + row*CELL_SIZE
    
    # increases range of balloons
    def useItem(self, hero, items, board, goldEarned): 
        if not hero.isTrapped and not hero.isDead:
            if hero.balloonRange < 4: 
                hero.balloonRange += 1
            items.remove(self)
            board[self.row][self.col] = None 
        return goldEarned

    # draws flask on screen 
    def drawItem(self, screen): 
        x, y = self.rect.x, self.rect.y
        screen.blit(self.flask, (x, y))
   
# NEEDLE ITEM  
class Needle(Item): 

    # initializes Needle graphics 
    def initNeedle(self): 
        s = self.size
        self.needle = pygame.image.load("graphics/items/needle.png")
        self.needle = pygame.transform.scale(self.needle, (s,s))
        
    def __init__(self, row, col) :
        super().__init__(row, col)
        self.initNeedle()
        
        # creates needle rect
        self.rect = self.needle.get_rect()
        self.rect.x = MARGIN + col*CELL_SIZE
        self.rect.y = MARGIN + row*CELL_SIZE
    
    # saves hero if trapped 
    def useItem(self, hero, items, board, goldEarned): 
        hero.needles += 1
        items.remove(self)
        board[self.row][self.col] = None 
        return goldEarned

    # draws needle on screen 
    def drawItem(self, screen): 
        x, y = self.rect.x, self.rect.y
        screen.blit(self.needle, (x, y))
        
# SKATES ITEM 
class Skates(Item): 

    # initializes Skate graphics 
    def initSkates(self): 
        s = self.size
        self.skates = pygame.image.load("graphics/items/skates.png")
        self.skates = pygame.transform.scale(self.skates, (s,s))
        
    def __init__(self, row, col) :
        super().__init__(row, col)
        self.initSkates()
        
        # creates skates rect
        self.rect = self.skates.get_rect()
        self.rect.x = MARGIN + col*CELL_SIZE
        self.rect.y = MARGIN + row*CELL_SIZE
    
    # speeds up hero 
    def useItem(self, hero, items, board, goldEarned): 
        if not hero.isTrapped:
            hero.dx += 5
            if hero.dx > 30: 
                hero.dx = 30 
            items.remove(self)
            board[self.row][self.col] = None 
        return goldEarned

    # draws skates on screen 
    def drawItem(self, screen): 
        x, y = self.rect.x, self.rect.y
        screen.blit(self.skates, (x, y))
    
# BALLOON ITEM 
class BalloonItem(Item): 

    # initializes balloon graphics 
    def initBalloonItem(self): 
        s = self.size
        self.balloonItem = pygame.image.load("graphics/items/balloonItem.png")
        self.balloonItem = pygame.transform.scale(self.balloonItem, (s,s))
        
    def __init__(self, row, col) :
        super().__init__(row, col)
        self.initBalloonItem()
        
        # creates balloon rect
        self.rect = self.balloonItem.get_rect()
        self.rect.x = MARGIN + col*CELL_SIZE
        self.rect.y = MARGIN + row*CELL_SIZE
    
    # gives hero additional balloon 
    def useItem(self, hero, items, board, goldEarned): 
        hero.numBalloons += 1
        items.remove(self)
        board[self.row][self.col] = None 
        return goldEarned

    # draws balloon on screen 
    def drawItem(self, screen): 
        x, y = self.rect.x, self.rect.y
        screen.blit(self.balloonItem, (x, y))
    
# EXP ITEM 
class EXPItem(Item): 

    # initializes exp graphics 
    def initEXPItem(self): 
        s = self.size
        self.exp = pygame.image.load("graphics/items/exp.png")
        self.exp = pygame.transform.scale(self.exp, (s,s))
        
    def __init__(self, row, col) :
        super().__init__(row, col)
        self.initEXPItem()
        
        # creates exp rect
        self.rect = self.exp.get_rect()
        self.rect.x = MARGIN + col*CELL_SIZE
        self.rect.y = MARGIN + row*CELL_SIZE
    
    # gives hero exp 
    def useItem(self, hero, items, board, goldEarned): 
        hero.exp += 10
        items.remove(self)
        board[self.row][self.col] = None 
        return goldEarned

    # draws item on screen 
    def drawItem(self, screen): 
        x, y = self.rect.x, self.rect.y
        screen.blit(self.exp, (x, y))
    
# GOLD ITEM 
class Gold(Item):
    
    # initializes gold graphics 
    def initGold(self): 
        s = self.size
        self.gold = pygame.image.load("graphics/items/gold.png")
        self.gold = pygame.transform.scale(self.gold, (s,s))
        
    def __init__(self, row, col) :
        super().__init__(row, col)
        self.initGold()
        
        # creates gold rect
        self.rect = self.gold.get_rect()
        self.rect.x = MARGIN + col*CELL_SIZE
        self.rect.y = MARGIN + row*CELL_SIZE
    
    # gives hero gold
    def useItem(self, hero, items, board, goldEarned): 
        hero.gold += 10
        goldEarned += 10 
        items.remove(self)
        board[self.row][self.col] = None 
        return goldEarned
        
    # draws balloon on screen 
    def drawItem(self, screen): 
        x, y = self.rect.x, self.rect.y
        screen.blit(self.gold, (x, y))