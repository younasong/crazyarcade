# Youna Song (younas)
# 12/07/2017
# 15-112 Term Project

"""This is the file for the main Balloon class 
   Includes balloon animations, explosions, and collisions with heroes and obstacles 
"""

import pygame, math, random 
from constants import * 
from hero import * 
from items import * 
from obstacles import * 
from monster import *

class Balloon(pygame.sprite.Sprite):
    
    # initializes balloon graphics 
    def initTiles(self): 
        bS = self.size
        
        balloon1 = pygame.image.load("graphics/balloon/balloon1.png")
        balloon2 = pygame.image.load("graphics/balloon/balloon2.png")
        balloon3 = pygame.image.load("graphics/balloon/balloon3.png")
        balloon4 = pygame.image.load("graphics/balloon/balloon4.png")
    
        balloon1 = pygame.transform.scale(balloon1, (bS,bS))
        balloon2 = pygame.transform.scale(balloon2, (bS,bS))
        balloon3 = pygame.transform.scale(balloon3, (bS,bS))
        balloon4 = pygame.transform.scale(balloon4, (bS,bS))
        
        self.images = [balloon1, balloon2, balloon3, balloon4]
            
        self.splashCenter = pygame.image.load("graphics/splash/splashCenter.png")
        self.splashLeftEnd = pygame.image.load("graphics/splash/splashLeftEnd.png")
        self.splashRightEnd = pygame.image.load("graphics/splash/splashRightEnd.png")
        self.splashTopEnd = pygame.image.load("graphics/splash/splashTopEnd.png")
        self.splashBottomEnd = pygame.image.load("graphics/splash/splashBottomEnd.png")
        self.splashMiddleLR = pygame.image.load("graphics/splash/splashMiddle.png")

        self.splashCenter = pygame.transform.scale(self.splashCenter, (bS,bS))
        self.splashLeftEnd = pygame.transform.scale(self.splashLeftEnd, (bS,bS))
        self.splashRightEnd = pygame.transform.scale(self.splashRightEnd, (bS,bS))
        self.splashTopEnd = pygame.transform.scale(self.splashTopEnd, (bS,bS))
        self.splashBottomEnd = pygame.transform.scale(self.splashBottomEnd, (bS,bS))
        self.splashMiddleLR = pygame.transform.scale(self.splashMiddleLR, (bS,bS))
        self.splashMiddleU = pygame.transform.rotate(self.splashMiddleLR, 90)
        self.splashMiddleD = pygame.transform.rotate(self.splashMiddleLR, -90)

    def __init__(self, row, col, hero): 
        super().__init__()
        self.size = 60 
        self.initTiles()
        
        self.row = row 
        self.col = col 
        self.leave = False 
        self.splashCells = []
        self.hero = hero 
    
        # animation img index 
        self.index = 0
        self.image = self.images[self.index]

        # create balloon rect 
        self.rect = self.image.get_rect()
        self.rect.x = MARGIN + col*self.size
        self.rect.y = MARGIN + row*self.size

        # balloon timer 
        self.timer = 3
        self.pushTimer = 1500 
        self.last = pygame.time.get_ticks()
        
    def __eq__(self, other): 
        return isinstance(other, Balloon) and self.row == other.row and self.col == other.col
        
    # decrements timer every second 
    def update(self, dt, screen, board, hero):
        self.timer -= dt
        
        # CONTROLS BALLOON PUSH 
        # now = pygame.time.get_ticks() 
        # if hero.rect.right == self.rect.left: 
        #     if now - self.last >= self.pushTimer:
        #         self.pushBalloon('right', screen, board)
        # elif hero.rect.left == self.rect.right: 
        #     if now - self.last >= self.pushTimer:
        #         self.pushBalloon('left', screen, board)
        # elif hero.rect.bottom == self.rect.top: 
        #     if now - self.last >= self.pushTimer:
        #         self.pushBalloon('down', screen, board)
        # elif hero.rect.top == self.rect.bottom: 
        #     if now - self.last >= self.pushTimer:
        #         self.pushBalloon('up', screen, board)
        # else: 
        #     self.last = now 
            
    
    # pushes balloon depending on direction of hero 
    def pushBalloon(self, d, screen, board):
        s, m = CELL_SIZE, MARGIN
        
        initRow, initCol = self.row, self.col 
        if d == 'down': 
            while ( self.row+1 >= 0 and self.col >= 0 and 
                    self.row+1 < ROWS and self.col < COLS and 
                    board[self.row+1][self.col] == None or board[self.row+1][self.col] == Bomb(self.row+1, self.col)): 
                self.row += 1
            board[initRow][initCol] = None 
                
        elif d == 'up': 
            while ( self.row-1 >= 0 and self.col >= 0 and 
                    self.row-1 < ROWS and self.col < COLS and 
                    board[self.row-1][self.col] == None or board[self.row+1][self.col] == Bomb(self.row+1, self.col)): 
                self.row -= 1
            board[initRow][initCol] = None 
           
        elif d == 'left': 
            while ( self.row >= 0 and self.col-1 >= 0 and 
                    self.row < ROWS and self.col-1 < COLS and 
                    board[self.row][self.col-1] == None or board[self.row+1][self.col] == Bomb(self.row+1, self.col)):                
                self.col -= 1
            board[initRow][initCol] = None 
        
        elif d == 'right': 
            while ( self.row >= 0 and self.col+1 >= 0 and 
                    self.row < ROWS and self.col+1 < COLS and 
                    board[self.row][self.col+1] == None or board[self.row+1][self.col] == Bomb(self.row+1, self.col)):                 
                self.col += 1
            board[initRow][initCol] = None 
                
    # exlodes balloon on screen 
    def explodeBalloon(self,screen, board, balloons, obstacles, monsters, items, hero, heroes): 
    
        bR = hero.balloonRange
        r, c, m, s = self.row, self.col, MARGIN, CELL_SIZE
        lStop, rStop, uStop, dStop = False, False, False, False 
        
        self.splashCells = [(r,c)]
        board[r][c] = None 
                
        # left splash 
        for i in range(1, bR): 
            if r-i >= 0: 
                if board[r-i][c] != None: 
                    screen.blit(self.splashMiddleU, (m+c*s, m+(r-i)*s))
                    uStop = True 
                    self.splashCells += [(r-i, c)]
                    board[r-i][c] = None
                    break 
                else: 
                    screen.blit(self.splashMiddleU, (m+c*s, m+(r-i)*s))
                    self.splashCells += [(r-i, c)]
                    board[r-i][c] = None
                
        # right splash 
        for i in range(1, bR):
            if r+i < ROWS: 
                if board[r+i][c] != None: 
                    screen.blit(self.splashMiddleD, (m+c*s, m+(r+i)*s))
                    dStop = True 
                    self.splashCells += [(r+i, c)]
                    board[r+i][c] = None
                    break
                else: 
                    screen.blit(self.splashMiddleD, (m+c*s, m+(r+i)*s)) 
                    self.splashCells += [(r+i, c)]
                    board[r+i][c] = None

        # top splash 
        for i in range(1, bR): 
            if c-i >= 0: 
                if board[r][c-i] != None: 
                    screen.blit(self.splashMiddleLR, (m+(c-i)*s, m+r*s))
                    lStop = True 
                    self.splashCells += [(r, c-i)]                    
                    board[r][c-i] = None

                    break 
                else: 
                    screen.blit(self.splashMiddleLR, (m+(c-i)*s, m+r*s))
                    self.splashCells += [(r, c-i)]
                    board[r][c-i] = None

        # bottom splash 
        for i in range(1, bR): 
            if c+i < COLS:
                if board[r][c+i] != None:
                    screen.blit(self.splashMiddleLR, (m+(c+i)*s, m+r*s))
                    rStop = True 
                    self.splashCells += [(r, c+i)]
                    board[r][c+i] = None
                    break 
                else: 
                    screen.blit(self.splashMiddleLR, (m+(c+i)*s, m+r*s)) 
                    self.splashCells += [(r, c+i)]
                    board[r][c+i] = None
                    
        screen.blit(self.splashCenter, (m+c*s, m+r*s))
        
        # stop balloon splash when obstacle is reached
        if uStop == False: 
            screen.blit(self.splashTopEnd, (m+c*s, m+(r-bR)*s))
            self.splashCells += [(r-bR,c)]
        if dStop == False: 
            screen.blit(self.splashBottomEnd, (m+c*s, m+(r+bR)*s))
            self.splashCells += [(r+bR,c)]
        if lStop == False: 
            screen.blit(self.splashLeftEnd, (m+(c-bR)*s, m+r*s))
            self.splashCells += [(r,c-bR)]
        if rStop == False: 
            screen.blit(self.splashRightEnd, (m+(c+bR)*s, m+r*s))
            self.splashCells += [(r,c+bR)]
        
    # checks splash collisions with obstacles, monsters, and hero 
    def checkCollisions(self, board, obstacles, monsters, items, heroes, expEarned):
        
       # removes obstacle if hit by balloon 
        for obstacle in obstacles: 
            r, c = obstacle.row, obstacle.col
            if (r, c) in self.splashCells: 
                obstacles.remove(obstacle)
                
                # puts random item where obstacle was 30% of the time 
                if random.random() < 0.30:
                    itemList = [BalloonItem(r,c), Needle(r,c), Flask(r,c), Skates(r,c), EXPItem(r,c), Gold(r,c)]
                    item = random.choice(itemList)
                    items += [item] 
                    
                board[r][c] = None 
                self.splashCells[:] = [x for x in self.splashCells if x != (r,c)]

                # DEMONSTRATION PURPOSES (exp is given when obstacles are removed) 
                self.hero.exp += 5
                expEarned += 5
                
        # removes monsters if hit by balloon 
        for monster in monsters: 
            r, c = monster.row, monster.col
            if (r, c) in self.splashCells: 
                monsters.remove(monster)
                board[monster.row][monster.col] = None 
                self.splashCells[:] = [x for x in self.splashCells if x != (r,c)]
                # gives hero exp 
                self.hero.exp += 10
                expEarned += 10
                
        # removes items if hit by balloon 
        for item in items: 
            r, c = item.row, item.col
            if (item.row, item.col) in self.splashCells: 
                items.remove(item)
                self.splashCells[:] = [x for x in self.splashCells if x != (r,c)]
                board[item.row][item.col] = None 
        
        # traps hero if hit by balloon 
        for hero in heroes: 
            if (hero.row, hero.col) in self.splashCells: 
                hero.isTrapped = True 
    
        self.splashCells = []
            
        # remove all surrounding objects from board 
        r, c = self.row, self.col
        directions = [(0,0), (0,1),(0,-1),(1,0),(-1,0)]
        for direction in directions: 
            rowMove = direction[0]
            colMove = direction[1]
            if (r + rowMove >= 0 and r + rowMove < ROWS and 
                c + colMove >= 0 and c + colMove < COLS): 
                board[r+rowMove][c+colMove] = None 

        return expEarned
               
    # animate balloon
    def animate(self):
        self.index += 0.095
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[math.floor(self.index)]
            
    # draws balloon on screen 
    def drawBalloon(self, screen): 
        s, m = CELL_SIZE, MARGIN
        row, col = self.row, self.col
        screen.blit(self.image, (m+col*s, m+row*s))