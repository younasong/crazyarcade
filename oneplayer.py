# Youna Song (younas)
# 12/07/2017
# 15-112 Term Project

"""
This file contains classes related to the one player game mode 
Includes the profile screen and side screen classes 
"""

import pygame
from constants import *
from items import *
from screens import * 

class OnePlayerProfile(Screen): 
    def __init__(self): 
        super().__init__()
        w, h, t = SCREEN_WIDTH, SCREEN_HEIGHT, TOTAL_WIDTH
        self.size = 64
        
        self.leftArrowRect = self.leftArrow.get_rect()
        self.leftArrowRect.x = w*.1-50
        self.leftArrowRect.y = h*.1-50
        
        self.login = pygame.transform.scale(self.login, (170,170))
        self.loginRect = self.login.get_rect()
        self.loginRect.x = t*.8
        self.loginRect.y = h*.75
        
        self.shopRect = self.shop.get_rect()
        self.shopRect.x = t*.05
        self.shopRect.y = h*.9

    # draw profile screen 
    def drawProfileScreen(self, screen, hero): 
        w, h, t = SCREEN_WIDTH, SCREEN_HEIGHT, TOTAL_WIDTH
        sR, sC = 13, 18
        
        for row in range(sR): 
            for col in range(sC): 
                if col == 0: 
                    screen.blit(self.woodL, (0, row*self.size))
                elif col == sC-1: 
                    screen.blit(self.woodR, (t-self.size, row*self.size))
                else: 
                    screen.blit(self.wood, (col*self.size, row*self.size))
        
        font1 = pygame.font.Font('fonts/Kenney Future Narrow.ttf', 50)
        font2 = pygame.font.Font('fonts/Kenney Future Narrow.ttf', 40)
        font3 = pygame.font.Font('fonts/Kenney Future Narrow.ttf', 25)

        profileText = font1.render('Character Profile', True, DARKBLUE)
        nameText = font2.render(hero.name, True, TEALBLUE)
        roundsText = font3.render('Rounds Played: ' + str(hero.rounds), True, BLACK)
        levelText = font3.render('Current Level: ' + str(hero.level), True, BLACK)
        expText = font3.render('EXP Gained: ' + str(hero.exp), True, BLACK)
        goldText = font3.render('Gold Earned: ' + str(hero.gold) + "C", True, BLACK)
        itemsText = font2.render('ITEMS', True, TEALBLUE)
        needleText = font3.render(str(hero.needles) + 'X', True, BLACK)
        
        screen.blit(self.login, self.loginRect)
        screen.blit(self.shop, self.shopRect)
        screen.blit(self.leftArrow, self.leftArrowRect)
        screen.blit(profileText, (t*.25, h*.05))
        screen.blit(self.heroForward, (t*.2, h*.15))
        screen.blit(nameText, (t*.16, h*.25))
        screen.blit(roundsText, (t*.1, h*.35))
        screen.blit(levelText, (t*.1, h*.4))
        screen.blit(expText, (t*.1, h*.45))
        screen.blit(goldText, (t*.1, h*.5))
        screen.blit(itemsText, (t*.15, h*.7))
        screen.blit(self.needle, (t*.13, h*.78))
        screen.blit(needleText, (t*.21, h*.8))
        
        self.drawHistory(screen, hero)
        
    # draws game history 
    def drawHistory(self, screen, hero): 
        w, h, t = SCREEN_WIDTH, SCREEN_HEIGHT, TOTAL_WIDTH
        font1 = pygame.font.Font('fonts/Kenney Future Narrow.ttf', 50)
        font2 = pygame.font.Font('fonts/Kenney Future Narrow.ttf', 40)
        font3 = pygame.font.Font('fonts/Kenney Future Narrow.ttf', 20)
        
        title = font2.render("GAME HISTORY", True, DARKRED)
        goldLabel = font3.render('Gold Earned: ', True, BLACK)
        expLabel = font3.render('EXP Gained: ', True, BLACK)
        
        screen.blit(title, (t*.55, h*.18))
        if len(hero.games) > 0: 
            screen.blit(goldLabel, (t*.65, h*.25))
            screen.blit(expLabel, (t*.8, h*.25))
        
        row = 0 
        for game in hero.games: 
            time = game
            goldEarned = str(hero.games[game]['gold'])
            expEarned = str(hero.games[game]['exp'])
            
            timeText = font3.render(time, True, BLACK)
            goldText = font3.render(goldEarned, True, BLACK)
            expText = font3.render(expEarned, True, BLACK)
            
            screen.blit(timeText, (t*.45, h*.3 + row*20))
            screen.blit(goldText, (t*.7, h*.3 + row*20))
            screen.blit(expText, (t*.85, h*.3 + row*20))
            
            row += 1
            if row > 10: 
                break 
    
# SIDE SCREEN 
class OnePlayerSideScreen(SideScreen): 
    def __init__(self): 
        super().__init__()
        
        # create quit button
        self.quitRect = self.quit.get_rect()
        self.quitRect.x = TOTAL_WIDTH*.9
        self.quitRect.y = SCREEN_HEIGHT*.93
        
        # create shop button 
        self.shopRect = self.shop.get_rect()
        self.shopRect.x = TOTAL_WIDTH*.84
        self.shopRect.y = SCREEN_HEIGHT*.92
        
    # draws next round button 
    def drawNext(self, screen): 
        w, h = TOTAL_WIDTH, SCREEN_HEIGHT
        screen.blit(self.yellowButton, self.yBRect)

    # draws side screen 
    def drawSide(self, screen, hero): 
        s, w, h, t = SIDE_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT, TOTAL_WIDTH
        sR, sC = 13, 5
        
        # draws wood background 
        for row in range(sR): 
            for col in range(sC): 
                if col == 0: 
                    screen.blit(self.woodL, (w, row*self.size))
                elif col == sC-1: 
                    screen.blit(self.woodR, (t-self.size, row*self.size))
                else: 
                    screen.blit(self.wood, (w + col*self.size, row*self.size))
                
        screen.blit(self.quit, self.quitRect)

        smallFont = pygame.font.Font('fonts/Kenney Future Narrow.ttf', 25)
        expText = smallFont.render('EXP:', True, BLACK)
        itemsText = smallFont.render('Items:', True, BLACK)
        screen.blit(expText, (t*.75, h*.3))
        screen.blit(itemsText, (t*.75, h*.8))
        
    # draws content on side screen 
    def drawContent(self, screen, hero): 
        w, h = TOTAL_WIDTH, SCREEN_HEIGHT
        self.heroForward = pygame.image.load("graphics/hero/heroForward.png")
        self.heroForward = pygame.transform.scale(self.heroForward, (60,60))
        screen.blit(self.heroForward, (w*.82, h*.1))
        
        smallFont = pygame.font.Font('fonts/Kenney Future Narrow.ttf', 30)
        nameText = smallFont.render(hero.name, True, BLACK)
        screen.blit(nameText, (w*.82, h*.2))
            
        self.shopRect = screen.blit(self.shop,self.shopRect)
        self.drawMedals(screen, hero)
        self.drawLevelBar(screen, hero)
        self.drawHold(screen, hero)
        
    # draws medals up to level 10 
    def drawMedals(self, screen, hero): 
        w, h = TOTAL_WIDTH, SCREEN_HEIGHT
        wm, hm = .79, .2
        if hero.level == 1: 
            screen.blit(self.levelOne, (w*wm, h*hm))
        elif hero.level == 2: 
            screen.blit(self.levelTwo, (w*wm, h*hm))
        elif hero.level == 3: 
            screen.blit(self.levelThree, (w*wm, h*hm))
        elif hero.level == 4: 
            screen.blit(self.levelFour, (w*wm, h*hm))
        elif hero.level == 5: 
            screen.blit(self.levelFive, (w*wm, h*hm))
        elif hero.level == 6: 
            screen.blit(self.levelSix, (w*wm, h*hm))
        elif hero.level == 7: 
            screen.blit(self.levelSeven, (w*wm, h*hm))
        elif hero.level == 8: 
            screen.blit(self.levelEight, (w*wm, h*hm))
        elif hero.level == 9: 
            screen.blit(self.levelNine,(w*wm, h*hm))
        elif hero.level == 10: 
            screen.blit(self.levelTen, (w*wm, h*hm))

    # draws level bar 
    def drawLevelBar(self, screen, hero): 
        w, h = TOTAL_WIDTH, SCREEN_HEIGHT
        pygame.draw.rect(screen, BLACK, (w*.81, h*.3, 200, 40), 2 )
        pygame.draw.rect(screen, DODGERBLUE, (w*.81, h*.3, hero.exp*2,40))
        
        smallFont = pygame.font.Font('fonts/Kenney Future Narrow.ttf', 15)
        levelText = smallFont.render('Level:' + str(hero.level), True, BLACK)
        screen.blit(levelText, (w*.81, h*.35))
        
    # draws item on hold 
    def drawHold(self, screen, hero): 
        w, h = TOTAL_WIDTH, SCREEN_HEIGHT
        self.needle = pygame.transform.scale(self.needle, (60,60))
        
        if hero.needles > 0: 
            screen.blit(self.needle, (w*.75, h*.85))

            smallFont = pygame.font.Font('fonts/Kenney Future Narrow.ttf', 25)
            needleText = smallFont.render(str(hero.needles) + 'x', True, BLACK)
            screen.blit(needleText, (w*.79, h*.91))
