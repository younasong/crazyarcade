# Youna Song (younas)
# 12/07/2017
# 15-112 Term Project

"""
This is the file for the main Hero class 
Controls hero movement, collisions with balloons, items
Draws graphics for trapped and killed hero 
"""

import pygame, math
from constants import *
from screens import * 
from items import * 

## Hero Class 

class Hero(pygame.sprite.Sprite):
    
    # initialize hero graphics 
    def initHero(self): 
        w, h = 55, 55
    
        self.heroForward = pygame.image.load("graphics/hero/heroForward.png")
        self.heroForward = pygame.transform.scale(self.heroForward, (w,h))
        
        self.heroBackwards = pygame.image.load("graphics/hero/heroBackwards.png")
        self.heroBackwards = pygame.transform.scale(self.heroBackwards, (w,h))
        
        self.heroLeft = pygame.image.load("graphics/hero/heroLeft.png")
        self.heroLeft = pygame.transform.scale(self.heroLeft, (w,h))
        
        self.heroRight = pygame.image.load("graphics/hero/heroRight.png")
        self.heroRight = pygame.transform.scale(self.heroRight, (w,h))
        
        self.trapped = pygame.image.load("graphics/hero/trapped.png")
        self.trapped = pygame.transform.scale(self.trapped, (h,h))
        
        
        die1 = pygame.image.load("graphics/hero/die1.png")
        die2 = pygame.image.load("graphics/hero/die2.png")
        die3 = pygame.image.load("graphics/hero/die3.png")
        die4 = pygame.image.load("graphics/hero/die4.png")
        die5 = pygame.image.load("graphics/hero/die5.png")
        self.die6 = pygame.image.load("graphics/hero/die6.png")
        
        die1 = pygame.transform.scale(die1, (w,h))
        die2 = pygame.transform.scale(die2, (w,h))
        die3 = pygame.transform.scale(die3, (w,h))
        die4 = pygame.transform.scale(die4, (w,h))
        die5 = pygame.transform.scale(die5, (w,h))
        self.die6 = pygame.transform.scale(self.die6, (w,h))
        
        self.dieImages = [die1, die2, die3, die4, die5, self.die6]

    def __init__(self, name = "Guest", exp = 0, level = 1, gold = 30, needles = 1, dx = 10, rounds = 0, games = dict()): 
        super().__init__()
        self.initHero()
        self.size = 60
    
        self.isTrapped = False 
        self.isDead = False 
        self.numBalloons = 1
        self.balloonRange = 1
        
        # images 
        self.heroDirection = 'forwards'
        self.currImage = self.heroForward
        self.dieIndex = 0
        self.dieImage = self.dieImages[self.dieIndex]
        
        # create hero rect 
        self.rect = self.currImage.get_rect()
        self.rect.x, self.rect.y = 6*CELL_SIZE, 7*CELL_SIZE
        self.row, self.col = int(self.rect.y / CELL_SIZE), int(self.rect.x / CELL_SIZE)
        
        self.timer = 3
        
        # hero attributes  
        self.name = name 
        self.exp = exp
        self.level = level
        self.gold = gold 
        self.needles = needles
        self.dx = dx
        self.rounds = rounds 
        self.games = games 
        
    def goLeft(self):
        self.rect.x -= self.dx
        self.heroDirection = "left"
        
    def goRight(self): 
        self.rect.x += self.dx
        self.heroDirection = "right"
        
    def goUp(self): 
        self.rect.y -= self.dx
        self.heroDirection = "backwards"
        
    def goDown(self): 
        self.rect.y += self.dx
        self.heroDirection = "forwards"
        
    # decrements timer every second if hero is trapped 
    def update(self, screen, dt):
        if self.isTrapped: 
            self.timer -= dt
            
        # update hero row and col depending on x and y position    
        self.row = int(self.rect.y / CELL_SIZE)
        self.col = int(self.rect.x / CELL_SIZE)
        
        if self.isTrapped: 
            self.trapHero(screen) 
        if self.isDead: 
            self.killHero(screen)
            
        self.levelUp()
        
    # checks hero collisions with obstacles, balloons, and monsters 
    def checkCollisions(self, obstacles, balloons, monsters): 
        d = self.heroDirection
        
        # hero can't go past obstacles 
        for obstacle in obstacles:
            if self.rect.colliderect(obstacle.rect):
                if d == 'right': 
                    self.rect.right = obstacle.rect.left
                if d == 'left': 
                    self.rect.left = obstacle.rect.right
                if d == 'forwards': 
                    self.rect.bottom = obstacle.rect.top
                if d == 'backwards': 
                    self.rect.top = obstacle.rect.bottom
            
        # hero can't go through balloons (except initially) 
        for balloon in balloons:
            if balloon.leave == True and self.rect.colliderect(balloon.rect):
                if d == 'right': 
                    self.rect.right = balloon.rect.left
                if d == 'left': 
                    self.rect.left = balloon.rect.right
                if d == 'forwards': 
                    self.rect.bottom = balloon.rect.top
                if d == 'backwards': 
                    self.rect.top = balloon.rect.bottom
                
            elif self.rect.colliderect(balloon.rect) == 0:
               balloon.leave = True 
                    
    # makes sure hero stays within screen
    def isValidStep(self):  
        w, h, m = SCREEN_WIDTH, SCREEN_HEIGHT, MARGIN
        if self.rect.x > w- self.size: 
            self.rect.x -= self.dx
            
        elif self.rect.x < 0: 
            self.rect.x = 0
            
        elif self.rect.y > h- self.size: 
            self.rect.y -= self.dx
            
        elif self.rect.y < 0: 
            self.rect.y = 0
        
    # draws hero on screen 
    def drawHero(self, screen): 
        s = 64
        x, y = self.rect.x, self.rect.y
        
        if not (self.isTrapped): 
            if self.heroDirection == 'forwards': 
                screen.blit(self.heroForward, (x, y))
            elif self.heroDirection == 'backwards': 
                screen.blit(self.heroBackwards,(x, y))
            elif self.heroDirection == 'left': 
                screen.blit(self.heroLeft,(x, y))
            elif self.heroDirection == 'right': 
                screen.blit(self.heroRight,(x, y))
        
    # uses item on hold 
    def useHoldItem(self): 
        if self.needles > 0: 
            if self.isTrapped: 
                self.isTrapped = False 
                self.needles -= 1
                
    # draw hero trapped in bubble
    def trapHero(self, screen): 
        screen.blit(self.trapped,(self.rect.x, self.rect.y))
        self.dx = 10
        
    # draw hero death
    def killHero(self, screen): 
        while self.dieIndex < len(self.dieImages)-1:
            self.dieIndex += 0.2
            self.dieImage = self.dieImages[math.floor(self.dieIndex)]
            screen.blit(self.dieImage,(self.rect.x, self.rect.y))
    
    # levels up hero 
    def levelUp(self): 
        if self.exp > 100: 
            self.exp = 0 
            self.level += 1