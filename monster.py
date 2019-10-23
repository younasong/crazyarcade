# Youna Song (younas)
# 12/07/2017
# 15-112 Term Project

"""
This file contains classes for Monsters
Includes monster animations, explosions, and collisions with heroes and obstacles 
"""

import pygame, random, math
from constants import *
from screens import * 

class Monster(pygame.sprite.Sprite):
    def __init__(self, row, col): 
        super().__init__()
        self.size = 100
        self.row, self.col = row, col 
        
        self.directions = ['forwards', 'backwards', 'left', 'right']
        self.direction = "forwards"
        self.stepSize = 5
        self.stepTimer = 5000
        
        self.last = pygame.time.get_ticks()
        self.colliding = False 
        
    # checks that monster stays on screen
    def isValidStep(self):  
        w, h, m, c = SCREEN_WIDTH, SCREEN_HEIGHT, MARGIN, CELL_SIZE
        if self.rect.x > w-m - self.size/2: 
            self.rect.x -= self.stepSize
            return False 
        elif self.rect.x < m: 
            self.rect.x += self.stepSize
            return False 
        elif self.rect.y > h-m - self.size/2: 
            self.rect.y -= self.stepSize
            return False 
        elif self.rect.y < m: 
            self.rect.y += self.stepSize
            return False 
        return True 
            
    # checks monster collisions with obstacles, balloon, and the hero 
    def checkCollisions(self, obstacles, balloons, hero): 
        d = self.direction
        self.colliding = False 
        
        # monster can't go past obstacle 
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
                
                # changes direction 
                newDirection = random.choice(self.directions)
                while newDirection == self.direction: 
                    newDirection = random.choice(self.directions)
                self.direction = newDirection
                
        # monster can't go through balloons 
        for balloon in balloons:
            if self.rect.colliderect(balloon.rect):
                if d == 'right': 
                    self.rect.right = balloon.rect.left
                if d == 'left': 
                    self.rect.left = balloon.rect.right
                if d == 'forwards': 
                    self.rect.bottom = balloon.rect.top
                if d == 'backwards': 
                    self.rect.top = balloon.rect.bottom
                
                # changes direction 
                newDirection = random.choice(self.directions)
                while newDirection == self.direction: 
                    newDirection = random.choice(self.directions)
                self.direction = newDirection
                
        # kills hero if colliding with monster 
        if self.rect.colliderect(hero.rect):
            hero.isDead = True 
        return False 
    
    # draw monster on screen
    def drawMonster(self, screen): 
        s = 64
        x, y = self.rect.x, self.rect.y
        screen.blit(self.image, (x, y))
        
    # animate monsters
    def animate(self):
        if self.direction == 'forwards': 
            self.images = self.frontImages
        elif self.direction == 'backwards': 
            self.images = self.backImages
        elif self.direction == 'right': 
            self.images = self.rightImages
        elif self.direction == 'left': 
            self.images = self.leftImages

        self.index += 0.7
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[math.floor(self.index)]
        
    
    # moves monster
    def moveMonster(self, screen):             
        if self.direction == "forwards": 
            self.rect.y += self.stepSize
        elif self.direction == 'backwards': 
            self.rect.y -= self.stepSize 
        elif self.direction == 'left': 
            self.rect.x -= self.stepSize 
        elif self.direction == 'right': 
            self.rect.x += self.stepSize
            
        # changes direction if step is not valid 
        if not(self.isValidStep()): 
            newDirection = random.choice(self.directions)
            while newDirection == self.direction: 
                newDirection = random.choice(self.directions)
            self.direction = newDirection
        
        # changes direction every so often (determined by stepTimer) 
        now = pygame.time.get_ticks() 
        if now - self.last >= self.stepTimer:
            self.direction  = random.choice(self.directions)
            self.last = now 
        
# BOMB MONSTER
class Bomb(Monster): 

    # import bomb graphics 
    def initBomb(self): 
        w, h = self.width, self.height
    
        self.monsterFront1 = pygame.image.load("graphics/monsters/bombFront1.png")
        self.monsterFront1 = pygame.transform.scale(self.monsterFront1, (w,h))
        self.monsterFront2 = pygame.image.load("graphics/monsters/bombFront2.png")
        self.monsterFront2 = pygame.transform.scale(self.monsterFront2, (w,h))
        self.monsterFront3 = pygame.image.load("graphics/monsters/bombFront3.png")
        self.monsterFront3 = pygame.transform.scale(self.monsterFront3, (w,h))
        
        self.monsterBack1 = pygame.image.load("graphics/monsters/bombBack1.png")
        self.monsterBack1 = pygame.transform.scale(self.monsterBack1, (w,h))
        self.monsterBack2 = pygame.image.load("graphics/monsters/bombBack2.png")
        self.monsterBack2 = pygame.transform.scale(self.monsterBack2, (w,h))
        self.monsterBack3 = pygame.image.load("graphics/monsters/bombBack3.png")
        self.monsterBack3 = pygame.transform.scale(self.monsterBack3, (w,h))
        
        self.monsterLeft1 = pygame.image.load("graphics/monsters/bombLeft1.png")
        self.monsterLeft1 = pygame.transform.scale(self.monsterLeft1, (w,h))
        self.monsterLeft2 = pygame.image.load("graphics/monsters/bombLeft2.png")
        self.monsterLeft2 = pygame.transform.scale(self.monsterLeft2, (w,h))
        self.monsterLeft3 = pygame.image.load("graphics/monsters/bombLeft3.png")
        self.monsterLeft3 = pygame.transform.scale(self.monsterLeft3, (w,h))
        
        self.monsterRight1 = pygame.image.load("graphics/monsters/bombRight1.png")
        self.monsterRight1 = pygame.transform.scale(self.monsterRight1, (w,h))
        self.monsterRight2 = pygame.image.load("graphics/monsters/bombRight2.png")
        self.monsterRight2 = pygame.transform.scale(self.monsterRight2, (w,h))
        self.monsterRight3 = pygame.image.load("graphics/monsters/bombRight3.png")
        self.monsterRight3 = pygame.transform.scale(self.monsterRight3, (w,h))
        
        self.frontImages = [self.monsterFront1, self.monsterFront2, self.monsterFront3]
        self.backImages = [self.monsterBack1, self.monsterBack2, self.monsterBack3]
        self.leftImages = [self.monsterLeft1, self.monsterLeft2, self.monsterLeft3]
        self.rightImages = [self.monsterRight1, self.monsterRight2, self.monsterRight3]
        self.images = self.frontImages
    
    def __init__(self, row, col): 
        super().__init__(row, col)
        self.width, self.height = 60, 60 
        self.initBomb()
        
        self.currImage = self.monsterFront1
        self.exp = 10 
        
        # create zombie rect 
        self.rect = self.currImage.get_rect()
        self.rect.x = MARGIN + col*CELL_SIZE
        self.rect.y = MARGIN + row*CELL_SIZE
        
        # animation img index 
        self.index = 0
        self.frontImage = self.frontImages[self.index]
        self.backImage = self.backImages[self.index]
        self.leftImage = self.leftImages[self.index]
        self.rightImage = self.rightImages[self.index]
        
    def update(self): 
        self.row = int(self.rect.y / CELL_SIZE)
        self.col = int(self.rect.x / CELL_SIZE)
        
        