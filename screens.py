# Youna Song (younas)
# 12/07/2017
# 15-112 Term Project

"""
This file contains classes related to all screens and backgrounds 
Includes the Screen and SideScreen superclasses 
Nearly all graphics used are included here 
"""

## Background

import pygame
from constants import *
from items import *

## SCREEN SUPER CLASS 
class Screen(object): 

    # INIT GRAPHICS 
    def __init__(self): 
        # grass tiles 
        self.grassUL = pygame.image.load("background_tiles/rpgTile000.png")
        self.grassUR = pygame.image.load("background_tiles/rpgTile002.png")
        self.grassLL = pygame.image.load("background_tiles/rpgTile036.png")
        self.grassLR = pygame.image.load("background_tiles/rpgTile038.png")
        self.grassT = pygame.image.load("background_tiles/rpgTile001.png")
        self.grassL = pygame.image.load("background_tiles/rpgTile018.png")
        self.grassR = pygame.image.load("background_tiles/rpgTile020.png")
        self.grassB = pygame.image.load("background_tiles/rpgTile037.png")
        self.grass = pygame.image.load("background_tiles/rpgTile019.png")
        
        # water tiles 
        self.waterUL = pygame.image.load("background_tiles/rpgTile010.png")
        self.waterUR = pygame.image.load("background_tiles/rpgTile012.png")
        self.waterLL = pygame.image.load("background_tiles/rpgTile044.png")
        self.waterLR = pygame.image.load("background_tiles/rpgTile046.png")
        self.waterT = pygame.image.load("background_tiles/rpgTile011.png")
        self.waterL = pygame.image.load("background_tiles/rpgTile028.png")
        self.waterR = pygame.image.load("background_tiles/rpgTile030.png")
        self.waterB = pygame.image.load("background_tiles/rpgTile045.png")
        self.water = pygame.image.load("background_tiles/rpgTile029.png")
        
        # sand tiles 
        self.sandL = pygame.image.load("background_tiles/rpgTile051.png")
        self.sandR = pygame.image.load("background_tiles/rpgTile052.png")
        self.sand = pygame.image.load("background_tiles/rpgTile052.png")
        
        # wood tiles 
        self.woodL = pygame.image.load("background_tiles/rpgTile123.png")
        self.woodR = pygame.image.load("background_tiles/rpgTile125.png")
        self.wood = pygame.image.load("background_tiles/rpgTile124.png")
        
        # stone tiles 
        self.stoneL = pygame.image.load("background_tiles/rpgTile060.png")
        self.stoneR = pygame.image.load("background_tiles/rpgTile062.png")
        self.stone = pygame.image.load("background_tiles/rpgTile061.png")
        
        # start screen bubble graphic
        self.bubble = pygame.image.load("screen_graphics/splash.png")
        self.bubble = pygame.transform.scale(self.bubble, (450,450))
        
        # buttons
        self.quit = pygame.image.load("screen_graphics/quit.png")
        self.start = pygame.image.load("screen_graphics/start.png")
        self.help = pygame.image.load("screen_graphics/help.png")
        self.single = pygame.image.load("screen_graphics/singlePlayer.png")
        self.two = pygame.image.load("screen_graphics/twoPlayer.png")
        self.leftArrow = pygame.image.load("screen_graphics/leftArrow.png")
        self.create = pygame.image.load("screen_graphics/create.png")
        self.login = pygame.image.load("screen_graphics/startButton.png")
        self.login = pygame.transform.scale(self.login, (150,150))
        self.yellowButton = pygame.image.load("screen_graphics/nextRound.png")
        self.yellowButton = pygame.transform.scale(self.yellowButton, (180, 100))
        self.yellowLogin = pygame.image.load("screen_graphics/login.png")
        
        s1, s2 = 50, 70
                
        # gold item 
        self.gold = pygame.image.load("graphics/items/gold.png")
        self.gold = pygame.transform.scale(self.gold, (s1,s1))
        
        # needle item 
        self.needle = pygame.image.load("graphics/items/needle.png")
        self.needle = pygame.transform.scale(self.needle, (s2,s2))
        
        # exp item 
        self.exp = pygame.image.load("graphics/items/exp.png")
        self.exp = pygame.transform.scale(self.exp, (s2,s2))
        
        # skates item
        self.skates = pygame.image.load("graphics/items/skates.png")
        self.skates = pygame.transform.scale(self.skates, (s2,s2))
        
        # shop icon 
        self.shop = pygame.image.load("screen_graphics/store.png")
        self.shop = pygame.transform.scale(self.shop, (50,50))
        
        # medals 
        self.levelOne = pygame.image.load("screen_graphics/medals/flat_medal4.png")
        self.levelTwo = pygame.image.load("screen_graphics/medals/flat_medal3.png")
        self.levelThree = pygame.image.load("screen_graphics/medals/flat_medal8.png")
        self.levelFour = pygame.image.load("screen_graphics/medals/flat_medal9.png")
        self.levelFive = pygame.image.load("screen_graphics/medals/flat_medal1.png")
        self.levelSix = pygame.image.load("screen_graphics/medals/flat_medal2.png")
        self.levelSeven = pygame.image.load("screen_graphics/medals/flat_medal5.png")
        self.levelEight = pygame.image.load("screen_graphics/medals/flat_medal6.png")
        self.levelNine = pygame.image.load("screen_graphics/medals/flat_medal7.png")
        self.levelTen = pygame.image.load("screen_graphics/medals/flatshadow_medal1.png")
        
        self.levelOne = pygame.transform.scale(self.levelOne, (25,40))
        self.levelTwo = pygame.transform.scale(self.levelTwo, (25,40))
        self.levelThree = pygame.transform.scale(self.levelThree, (25,40))
        self.levelFour = pygame.transform.scale(self.levelFour, (25,40))
        self.levelFive = pygame.transform.scale(self.levelFive, (25,40))
        self.levelSix = pygame.transform.scale(self.levelSix, (25,40))
        self.levelSeven = pygame.transform.scale(self.levelSeven, (25,40))
        self.levelEight = pygame.transform.scale(self.levelEight, (25,40))
        self.levelNine = pygame.transform.scale(self.levelNine, (25,40))
        self.levelTen = pygame.transform.scale(self.levelTen, (25,40))
        
        # hero 
        self.heroForward = pygame.image.load("graphics/hero/heroForward.png")
        self.heroForward = pygame.transform.scale(self.heroForward, (65,65))
        
## SIDE SCREEN SUPER CLASS 
class SideScreen(Screen): 
    def __init__(self): 
        super().__init__()
        w, h = TOTAL_WIDTH, SCREEN_HEIGHT
        self.size = 64
        self.quit = pygame.image.load("screen_graphics/quit.png")
        
        self.yBRect = self.yellowButton.get_rect()
        self.yBRect.x = w*.76
        self.yBRect.y = h*.49
        
        
## MAIN GAME SCREEN 
class MainScreen(Screen): 

    def __init__(self): 
        super().__init__()
        self.tileSize = 64
        self.groundRows, self.groundCols = 13,13
        
    # draws grass ground 
    def drawGround(self, screen): 
        w, h, m = SCREEN_WIDTH, SCREEN_HEIGHT, MARGIN
        gC, gR = self.groundCols, self.groundRows
        s = self.tileSize
        
        for row in range(gR): 
            for col in range(gC): 
                if row == 0 and col != gC-1 and col != 0: 
                    screen.blit(self.grassT, (s*col,0))
                elif row == gR-1 and col != gC-1 and col != 0: 
                    screen.blit(self.grassB, (s*col, h-s))
                elif col == 0 and row != 0 and row != gR-1: 
                    screen.blit(self.grassL, (0, s*row))
                elif col == gC-1 and row != 0 and row != gR-1: 
                    screen.blit(self.grassR, (w-s, s*row))
                elif row != 0 and row != gR-1 and col != gC-1 and col != 0: 
                    screen.blit(self.grass, (s*col, s*row))
        
        # draw four corners
        screen.blit(self.grassUL, (0,0))
        screen.blit(self.grassLL, (0, h-s))
        screen.blit(self.grassUR, (w-s, 0))
        screen.blit(self.grassLR, (w-s, h-s))
        
    # draw game board outline 
    def drawBoard(self, screen): 
        m, s = MARGIN, CELL_SIZE
        border = 5
        
        for r in range(ROWS): 
            for c in range(COLS): 
                pygame.draw.rect(screen, BLACK,(m+r*s, m+c*s, s, s), border)
                
## START SCREEN 
class StartScreen(Screen): 
        
    def __init__(self): 
        super().__init__()
        self.tileSize = 64
    
    def drawStart(self, screen): 
        w, h = TOTAL_WIDTH, SCREEN_HEIGHT
        
        screen.blit(self.bubble, ((w/2)-250, 50))
        self.singleRect = screen.blit(self.single, ((w/2 -230), h*.65))
        self.twoRect = screen.blit(self.two, ((w/2 +20), h*.65))
        self.quitRect = screen.blit(self.quit, ((w*.85), h*.9))
        self.loginRect = screen.blit(self.yellowLogin, ((w*.56), h*.77))
        self.createRect = screen.blit(self.create, ((w*.36), h*.87))
        
        smallFont = pygame.font.Font('fonts/Kenney Future Narrow.ttf', 23)
        usernameText = smallFont.render('Username:', True, BLACK)
        passwordText = smallFont.render('Password:', True, BLACK)
        screen.blit(usernameText, (w*.23, h*.76))
        screen.blit(passwordText, (w*.23, h*.81))
        
    # draws water ground 
    def drawGround(self, screen):
        w, h, m = TOTAL_WIDTH, SCREEN_HEIGHT, MARGIN
        gC, gR = 18, 13
        s = self.tileSize
        for row in range(gR): 
            for col in range(gC): 
                if row == 0 and col != gC-1 and col != 0: 
                    screen.blit(self.waterT, (s*col,0))
                elif row == gR-1 and col != gC-1 and col != 0: 
                    screen.blit(self.waterB, (s*col, h-s))
                elif col == 0 and row != 0 and row != gR-1: 
                    screen.blit(self.waterL, (0, s*row))
                elif col == gC-1 and row != 0 and row != gR-1: 
                    screen.blit(self.waterR, (w-s, s*row))
                elif row != 0 and row != gR-1 and col != gC-1 and col != 0: 
                    screen.blit(self.water, (s*col, s*row))
        
        screen.blit(self.waterUL, (0,0))
        screen.blit(self.waterLL, (0, h-s))
        screen.blit(self.waterUR, (w-s, 0))
        screen.blit(self.waterLR, (w-s, h-s))
        
class shopScreen(Screen): 
    def initShop(self): 
        w, h = TOTAL_WIDTH, SCREEN_HEIGHT
       
        # back button 
        self.leftArrowRect = self.leftArrow.get_rect()
        self.leftArrowRect.x = w*.1-50
        self.leftArrowRect.y = h*.1-50

        # buy button graphics
        self.needleCheck = pygame.image.load("screen_graphics/check.png")
        self.expCheck = pygame.image.load("screen_graphics/check.png")
        self.skateCheck = pygame.image.load("screen_graphics/check.png")
        
        # needle buy button
        self.needleBuyRect = self.needleCheck.get_rect()
        self.needleBuyRect.x = w*.15
        self.needleBuyRect.y = h*.28
        
        # exp buy button
        self.expBuyRect = self.expCheck.get_rect()
        self.expBuyRect.x = w*.15
        self.expBuyRect.y = h*.43
        
        # skates buy button 
        self.skateBuyRect = self.skateCheck.get_rect()
        self.skateBuyRect.x = w*.15
        self.skateBuyRect.y = h*.58
        
        self.size = 64

    def __init__(self): 
        super().__init__()
        self.initShop()
        
    # draws sand background 
    def drawBackground(self, screen): 
        w, h, t = SCREEN_WIDTH, SCREEN_HEIGHT, TOTAL_WIDTH

        rows, cols = 13, 18 
        for row in range(rows): 
            for col in range(cols): 
                if col == 0: 
                    screen.blit(self.sandL, (0, row*self.size))
                elif col == cols-1: 
                    screen.blit(self.sandR, (t-self.size, row*self.size))
                else: 
                    screen.blit(self.sand, (col*self.size, row*self.size))
        
    def drawShop(self, screen, hero): 
        self.drawBackground(screen)
        w, h = TOTAL_WIDTH, SCREEN_HEIGHT
        
        screen.blit(self.leftArrow, self.leftArrowRect)
        
        font1 = pygame.font.Font('fonts/Kenney Future Narrow.ttf', 40)
        font2 = pygame.font.Font('fonts/Kenney Future Narrow.ttf', 30)

        titleText = font1.render('COIN SHOP', True, BLACK)
        goldText = font2.render(str(hero.gold) + 'C', True, BLACK)
        screen.blit(titleText, (w*.4, h*.05))
        screen.blit(goldText, (w*.5, h*.12))
        screen.blit(self.gold, (w*.42, h*.12))
        
        # needle item
        needlePrice = font2.render('20C', True, BLACK)
        self.needleRect = screen.blit(self.needle, (w*.2, h*.25))
        screen.blit(needlePrice, (w*.28, h*.27))
        screen.blit(self.needleCheck, self.needleBuyRect)
        
        # exp item 
        expPrice = font2.render('50C', True, BLACK)
        self.expRect = screen.blit(self.exp, (w*.2, h*.4))
        screen.blit(expPrice, (w*.28, h*.42))
        screen.blit(self.expCheck, self.expBuyRect)

        # skate item 
        skatePrice = font2.render('100C', True, BLACK)
        self.skateRect = screen.blit(self.skates, (w*.2, h*.55))
        screen.blit(skatePrice, (w*.28, h*.57))
        screen.blit(self.skateCheck, self.skateBuyRect)
        
