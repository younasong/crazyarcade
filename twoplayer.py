# Youna Song (younas)
# 12/07/2017
# 15-112 Term Project

"""
This file contains classes related to the two player game mode 
Includes the login screen and side screen classes 
"""

import pygame
from constants import *
from items import *
from screens import * 

class TwoPlayerLoginScreen(Screen):
    
    def __init__(self): 
        super().__init__()
        self.login = pygame.transform.scale(self.login, (250,250))
        self.size = 64
        
    def drawLoginScreen(self, screen): 
        s, w, h, t = SIDE_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT, TOTAL_WIDTH

        # draws stone background 
        r, c = 13, 18
        for row in range(r): 
            for col in range(c): 
                if col == 0: 
                    screen.blit(self.stoneL, (0, row*self.size))
                elif col == c-1: 
                    screen.blit(self.stoneR, (t-self.size, row*self.size))
                else: 
                    screen.blit(self.stone, (col*self.size, row*self.size))
        
        
        self.leftArrowRect = screen.blit(self.leftArrow, ((w*.1-50), h*.1-50))
        smallFont = pygame.font.Font('fonts/Kenney Future Narrow.ttf', 23)
        usernameText = smallFont.render('Username:', True, BLACK)
        passwordText = smallFont.render('Password:', True, BLACK)
        playerOne = smallFont.render('Player 1', True, BLACK)
        playerTwo = smallFont.render('Player 2', True, BLACK)
        screen.blit(usernameText, (w*.20, h*.3))
        screen.blit(passwordText, (w*.20, h*.35))
        screen.blit(usernameText, (w*.70, h*.3))
        screen.blit(passwordText, (w*.70, h*.35))
        screen.blit(playerOne, (w*.40, h*.26))
        screen.blit(playerTwo, (w*.90, h*.26))
        self.loginRect = screen.blit(self.login, ((w*.55), h*.50))
        
# side screen for two player game 
class TwoPlayerSideScreen(SideScreen): 

    def __init__(self): 
        super().__init__()
        
    def drawSide(self, screen): 
        s, w, h, t = SIDE_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT, TOTAL_WIDTH
        sR, sC = 13, 5
        pygame.draw.rect(screen, WHITE,(w,0,s,h))
        
        # draws wood background 
        for row in range(sR): 
            for col in range(sC): 
                if col == 0: 
                    screen.blit(self.woodL, (w, row*self.size))
                elif col == sC-1: 
                    screen.blit(self.woodR, (t-self.size, row*self.size))
                else: 
                    screen.blit(self.wood, (w + col*self.size, row*self.size))
                
        self.quitRect = screen.blit(self.quit, ((t*.9), h*.93))

        smallFont = pygame.font.Font('fonts/Kenney Future Narrow.ttf', 25)
        expText = smallFont.render('EXP:', True, BLACK)
        itemsText = smallFont.render('Items:', True, BLACK)
        screen.blit(expText, (t*.75, h*.23))
        screen.blit(expText, (t*.75, h*.69))
        screen.blit(itemsText, (t*.75, h*.79))
        screen.blit(itemsText, (t*.75, h*.33))
        
    # draws content for side screen 
    def drawContent(self, screen, hero1, hero2): 
        w, h = TOTAL_WIDTH, SCREEN_HEIGHT
        self.heroForward = pygame.image.load("graphics/hero/heroForward.png")
        self.heroForward = pygame.transform.scale(self.heroForward, (60,60))
        screen.blit(self.heroForward, (w*.82, h*.05))
        screen.blit(self.heroForward, (w*.82, h*.5))

        smallFont = pygame.font.Font('fonts/Kenney Future Narrow.ttf', 30)
        nameText1 = smallFont.render(hero1.name, True, BLACK)
        nameText2 = smallFont.render(hero2.name, True, BLACK)
        screen.blit(nameText1, (w*.82, h*.15))
        screen.blit(nameText2, (w*.82, h*.61))

        self.drawMedals(screen, hero1, hero2)
        self.drawLevelBar(screen, hero1, hero2)
        self.drawHold(screen, hero1, hero2)
        
    # draws medals for each hero 
    def drawMedals(self, screen, hero1, hero2): 
        w, h = TOTAL_WIDTH, SCREEN_HEIGHT

        mheight = .15
        if hero1.level == 1: 
            screen.blit(self.levelOne, (w*.79, h*mheight))
        elif hero1.level == 2: 
            screen.blit(self.levelTwo, (w*.79, h*mheight))
        elif hero1.level == 3: 
            screen.blit(self.levelThree, (w*.79, h*mheight))
        elif hero1.level == 4: 
            screen.blit(self.levelFour, (w*.79, h*mheight))
        elif hero1.level == 5: 
            screen.blit(self.levelFive, (w*.79, h*mheight))
            
        mheight = .61
        if hero2.level == 1: 
            screen.blit(self.levelOne, (w*.79, h*mheight))
        elif hero2.level == 2: 
            screen.blit(self.levelTwo, (w*.79, h*mheight))
        elif hero2.level == 3: 
            screen.blit(self.levelThree, (w*.79, h*mheight))
        elif hero2.level == 4: 
            screen.blit(self.levelFour, (w*.79, h*mheight))
        elif hero2.level == 5: 
            screen.blit(self.levelFive, (w*.79, h*mheight))

    # draws level bar for each hero 
    def drawLevelBar(self, screen, hero1, hero2): 
        w, h = TOTAL_WIDTH, SCREEN_HEIGHT
        pygame.draw.rect(screen, BLACK, (w*.81, h*.23, 200, 40), 2 )
        pygame.draw.rect(screen, DODGERBLUE, (w*.81,h*.23,hero1.exp*2,40))
        
        pygame.draw.rect(screen, BLACK, (w*.81, h*.69, 200, 40), 2 )
        pygame.draw.rect(screen, DODGERBLUE, (w*.81, h*.69, hero2.exp*2, 40))
        
        smallFont = pygame.font.Font('fonts/Kenney Future.ttf', 15)
        levelText = smallFont.render('Level:' + str(hero1.level), True, BLACK)
        screen.blit(levelText, (w*.81, h*.28))
        
        levelText = smallFont.render('Level:' + str(hero2.level), True, BLACK)
        screen.blit(levelText, (w*.81, h*.74))
        
    # draws item on hold for each player 
    def drawHold(self, screen, hero1, hero2): 
    
        self.needle = pygame.image.load("graphics/items/needle.png")
        self.needle = pygame.transform.scale(self.needle, (60,60))
        
        smallFont = pygame.font.Font('fonts/Kenney Future.ttf', 25)
        needleText1 = smallFont.render(str(hero1.needles) + 'x', True, BLACK)
        needleText2 = smallFont.render(str(hero2.needles) + 'x', True, BLACK)

        if hero1.needles > 0: 
            screen.blit(self.needle, (TOTAL_WIDTH*.77, SCREEN_HEIGHT*.85))
            screen.blit(needleText1, (TOTAL_WIDTH*.81, SCREEN_HEIGHT*.91))

        if hero2.needles > 0: 
            screen.blit(self.needle, (TOTAL_WIDTH*.77, SCREEN_HEIGHT*.39))
            screen.blit(needleText2, (TOTAL_WIDTH*.81, SCREEN_HEIGHT*.45))


        
        