# Youna Song (younas)
# 12/07/2017
# 15-112 Term Project

"""This is the main file that controls all of the loops and screens
   This should be the first file that is executed
"""

import pygame, datetime
from constants import * 
from screens import * 
from hero import * 
from balloons import * 
from obstacles import * 
from monster import *
from items import *
from input import * 
from oneplayer import * 
from twoplayer import *
from board import *

## GLOBAL VARIABLES 

# global variables 
clock = pygame.time.Clock()
state = 'start'
players = 1
done = False 

# initializes heroes and attributes
hero = Hero()
hero1 = Hero()
hero2 = Hero()
heroes = []
expEarned, goldEarned = 0,0
p1EXP, p2EXP, p1Gold, p2Gold = 0,0,0,0

# initialize boards
board, obstacles, monsters, items = board1()
boardIndex = 0
boards = [board1(), board3(), board2()]

## PYMONGO 
from pymongo import MongoClient

# TO RUN SERVER: 
# mongod
# brew services start mongodb 

client = MongoClient()
db=client.localhost
collection=db['accounts']
cursor = collection.find({})

# RUN THIS TO CLEAR DATABASE
# collection.remove({})

# RUN THIS TO PRINT ALL FILES IN DATABASE
# for document in cursor:
#     print(document)
    
# creates new user account and adds to collection 
def createAccount(username, password, screen): 
    font = pygame.font.Font('fonts/Kenney Future Narrow.ttf', 20)
    w, h = SCREEN_WIDTH, SCREEN_HEIGHT
    
    if collection.find({'username': username}).count() == 0:
        if len(username) > 0 and len(password) > 0: 
            
            # initializes new user 
            gamesDict = dict()
            post = {
                'username': username,
                'password': password,
                'exp': 0,
                'level': 1,
                'gold': 30, 
                'needles': 1,
                'dx': 10, 
                'rounds': 0,
                'games': gamesDict 
            }
            
            # inserts user into database
            collection.insert_one(post)
            
            text = font.render('Account Successfully Created!', True, DARKRED)
            screen.blit(text, (w*.48, h*.93))
        else: 
            text = font.render('Invalid Credentials', True, DARKRED)
            screen.blit(text, (w*.48, h*.93))
    else: 
        text = font.render('Existing Account', True, DARKRED)
        screen.blit(text, (w*.48, h*.93))

## MAIN 
def main():
    pygame.init()
    
    # initialize all screens 
    w, h = SCREEN_WIDTH, SCREEN_HEIGHT
    background = MainScreen()
    start = StartScreen()
    onePlayerSide = OnePlayerSideScreen()
    twoPlayerSide = TwoPlayerSideScreen()
    twoPlayerLogin = TwoPlayerLoginScreen()
    onePlayerProfile = OnePlayerProfile()
    shop = shopScreen()
    
    # import and initialize variables 
    global players, state, done, board, hero
    balloons = []
    heroOneBalloons = [] 
    heroTwoBalloons = [] 
    
    # Set the height and width of the screen
    size = [TOTAL_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("15-112 TP")
    
    # make text input boxes for accounts 
    input1 = InputBox(w/2, h*.75)
    input2 = InputBox(w/2, h*.8)
    p1Username = InputBox(w*.4, h*.3)
    p1Password = InputBox(w*.4, h*.35)
    p2Username = InputBox(w*.9, h*.3)
    p2Password = InputBox(w*.9, h*.35)
    
    # main while loop 
    while not done: 
        dt = clock.tick(60)/1000
        
        # initiate start screen 
        if state == 'start': 
            startLoop(screen, start, input1, input2)
        
        # intitate shop screen 
        elif state == 'shop': 
            shopLoop(screen, shop, hero)
            
        # initiate one player play 
        elif state == 'oneplayer':
            singlePlayer(onePlayerSide, screen, dt, background, balloons)
            
        # initiate profile screen 
        elif state == 'oneplayerprofile': 
            onePlayerProfileLoop(onePlayerProfile, screen, input1, input2)
    
        # initiate two player login screen 
        elif state == 'twoplayerlogin': 
            twoPlayerStart(twoPlayerLogin, screen, p1Username, p1Password, p2Username, p2Password, input1, input2)
            
        #initiate two player play  
        elif state == 'twoplayer':
            twoPlayer(twoPlayerSide, screen, dt, background, heroes, heroOneBalloons, heroTwoBalloons)
        
## START SCREEN 
def startLoop(screen, start, input1, input2): 
    global state, hero , heroes, board
    w, h = SCREEN_WIDTH, SCREEN_HEIGHT
    font = pygame.font.Font('fonts/Kenney Future Narrow.ttf', 20)
    
    # draw screen
    start.drawGround(screen)
    start.drawStart(screen)
    input1.draw(screen)
    input2.draw(screen)
 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
        
        # handle textbox input 
        input1.handle_event(event)
        input2.handle_event(event)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            
            # BUTTONS
            singleButton = start.singleRect
            twoButton = start.twoRect
            quitButton = start.quitRect
            createButton = start.createRect
            loginButton = start.loginRect
            
            # quits game
            if quitButton.collidepoint(pos): 
                pygame.quit()
                done = True 

            # creates account 
            elif createButton.collidepoint(pos): 
                created = createAccount(input1.text, input2.text, screen)
                
            # logs in and changes to profile page 
            elif loginButton.collidepoint(pos): 
            
                post = collection.find_one({'username': input1.text})
                if post != None: 
                    password = post['password']
                    
                    # since account is valid, go to profile screen 
                    if input2.text == password: 
                    
                        level, exp, dx = post['level'], post['exp'], post['dx']
                        gold, needles = post['gold'], post['needles']
                        rounds, games = post['rounds'], post['games']
                        hero = Hero(input1.text, exp, level, gold, needles, dx, rounds, games)
                        heroes = [hero]
                        
                        state = 'oneplayerprofile'
                        return 
                        
                    else: 
                        text = font.render('Incorrect Password', True, DARKRED)
                        screen.blit(text, (w*.48, h*.93))
                        break
                else:
                    text = font.render('Account does not exist', True, DARKRED)
                    screen.blit(text, (w*.48, h*.93))
                    break
            
            # change to single player with guest 
            elif singleButton.collidepoint(pos):
                board, obstacles, monsters, items = board1()
                input1.text, input2.text = '',''
                state = 'oneplayer'
                return  
            
            # change state to two player login screen  
            elif twoButton.collidepoint(pos): 
                state = 'twoplayerlogin'
                return
        
    pygame.display.flip()
    
## SHOP

def shopLoop(screen, shop, hero): 
    global state 
    w, h = TOTAL_WIDTH, SCREEN_HEIGHT
    font = pygame.font.Font('fonts/Kenney Future Narrow.ttf', 20)
    
    # draws screen 
    shop.drawShop(screen, hero)
    
    # update database
    collection.find_one_and_update( {'username': hero.name}, 
                                    {'$set': {'exp': hero.exp, 
                                              'level': hero.level, 
                                              'gold': hero.gold, 
                                              'dx': hero.dx, 
                                              'needles': hero.needles}})

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            
            # BUTTONS
            needleButton = shop.needleBuyRect
            expButton = shop.expBuyRect
            skateButton = shop.skateBuyRect
            backButton = shop.leftArrowRect
            
            purchased = font.render('Purchased', True, BLUE)
            insufficient = font.render('Insufficient Funds', True, BLUE)

            
            # buy needle 
            if needleButton.collidepoint(pos):
                if hero.gold >= 20: 
                    screen.blit(purchased, (w*.35, h*.29))
                    hero.needles += 1
                    hero.gold -= 20
                else: 
                    screen.blit(insufficient, (w*.35, h*.29))
                
            # buy exp 
            elif expButton.collidepoint(pos):
                if hero.gold >= 50: 
                    screen.blit(purchased, (w*.35, h*.44))
                    hero.exp += 10
                    hero.gold -= 50
                else: 
                    screen.blit(insufficient, (w*.35, h*.29))
                
            # buy skates 
            elif skateButton.collidepoint(pos):
                if hero.gold >= 100: 
                    screen.blit(purchased, (w*.35, h*.59))
                    hero.dx += 5
                    hero.gold -= 100
                else: 
                    screen.blit(insufficient, (w*.35, h*.29))
            
            # go back to profiel page 
            if backButton.collidepoint(pos): 
                state = 'oneplayerprofile'
                return
        
    pygame.display.flip()
    
## ONE PLAYER PROFILE

def onePlayerProfileLoop(onePlayerProfile, screen, input1, input2):
    global state, hero, heroes, board, obstacles, monsters, items, balloons

    # draw 
    onePlayerProfile.drawProfileScreen(screen, hero)

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT: 
            done = True 
            
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            
            # BUTTONS
            backButton = onePlayerProfile.leftArrowRect
            startButton = onePlayerProfile.loginRect
            shopButton = onePlayerProfile.shopRect
            
            # go back to start 
            if backButton.collidepoint(pos): 
                input1.text, input2.text = '', '' 
                state = 'start'
                return 
                
            # start one player game 
            if startButton.collidepoint(pos): 
                board, obstacles, monsters, items = board1()
                hero.rect.x, hero.rect.y = 6*CELL_SIZE, 7*CELL_SIZE
                state = 'oneplayer'
                hero.isDead, hero.isTrapped, hero.timer, balloons = False, False, 3, [] 
                return 
                
            # go to sohp 
            if shopButton.collidepoint(pos): 
                state = 'shop'
                return 

    pygame.display.flip()
        
## SINGLE PLAYER GAME LOOP 

def singlePlayer(onePlayerSide, screen, dt, background, balloons):
    global clock, boards, boardIndex, obstacles, monsters, board, items, state, goldEarned, expEarned, hero
    
    # keeps track of game time 
    now = datetime.datetime.now()
    if now.minute < 10: 
        minute = '0' + str(now.minute)
    else: 
        minute = now.minute
    date = "%d/%d/%d   %d:%s" % (now.month, now.day, now.year, now.hour, minute)
        
        
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
            
        # BUTTONS
        quitButton = onePlayerSide.quitRect
        shopButton = onePlayerSide.shopRect
        nextButton = onePlayerSide.yBRect
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            
            # quits game 
            if quitButton.collidepoint(pos): 
                pygame.quit()
                done = True 
                
            # goes to shop 
            elif shopButton.collidepoint(pos): 
                board, obstacles, monsters, items = board1()
                state = 'shop'
                return 
            
            # ends round when all monsters are killed 
            if len(monsters) == 0: 
                if nextButton.collidepoint(pos): 
                    boardIndex += 1 # go to next board 
                    
                    # if there are no more rounds left, end game 
                    if boardIndex >= len(boards) : 
                        board, obstacles, monsters, items = board1()
                        
                        # update database with current game statistics 
                        currGame = dict()
                        currGame['gold'] = goldEarned
                        currGame['exp'] = expEarned
                        hero.games[date] = currGame
                        hero.rounds +=1
                        collection.find_one_and_update(
                            {'username': hero.name}, {'$set': {'games': hero.games, 'rounds':hero.rounds}})
                
                        state = 'oneplayerprofile'
                        goldEarned, expEarned = 0, 0
                        hero.rect.x, hero.rect.y = 6*CELL_SIZE, 7*CELL_SIZE
                        hero.numBalloons = 1
                        hero.dx, hero.balloonRange = 10, 1

                        return 
                    
                    hero.rect.x, hero.rect.y = 6*CELL_SIZE, 7*CELL_SIZE
                    board, obstacles, monsters, items = boards[boardIndex]
                   
            
    keys = pygame.key.get_pressed()
    
    # moves hero with keys 
    if not hero.isDead: 
        if keys[pygame.K_LEFT] == 1:
            hero.goLeft()
        elif keys[pygame.K_RIGHT] == 1:
            hero.goRight()
        elif keys[pygame.K_UP] == 1:
            hero.goUp()
        elif keys[pygame.K_DOWN] == 1:
            hero.goDown()
        elif keys[pygame.K_LSHIFT] == 1: 
            hero.useHoldItem()
       
        # drops balloon when space is pressed
        if not hero.isTrapped: 
            if keys[pygame.K_SPACE] == 1:
                r, c = hero.row, hero.col 
                if board[r][c] == None and len(balloons) < hero.numBalloons:
                    board[r][c] = Balloon(r,c, hero)
                    balloons.append(Balloon(r,c, hero))
           
    # DRAW CODE 
    background.drawGround(screen)
    onePlayerSide.drawSide(screen, hero)
    onePlayerSide.drawContent(screen, hero)
    # background.drawBoard(screen)
    
    hero.update(screen, dt)
    hero.checkCollisions(obstacles, balloons, monsters)
    hero.isValidStep()
    
    # kills hero if trapped for more than 3 seconds 
    if hero.timer <= 0: 
        hero.isTrapped = False
        hero.isDead = True 
        
    if not hero.isTrapped and not hero.isDead: 
        hero.drawHero(screen)
        
    if hero.isDead: 
        board, obstacles, monsters, items = board1()
        
        # update database with current game statistics 
        currGame = dict()
        currGame['gold'], currGame['exp'] = goldEarned, expEarned
        hero.games[date] = currGame
        hero.rounds +=1
        collection.find_one_and_update(
            {'username': hero.name}, {'$set': {'games': hero.games, 'rounds':hero.rounds}})

        state = 'oneplayerprofile'
        goldEarned, expEarned = 0, 0
        hero.rect.x, hero.rect.y = 6*CELL_SIZE, 7*CELL_SIZE
        hero.numBalloons, hero.balloonRange = 1, 1
        hero.dx = 10 
        return 

            
    # use item if hero collides with them 
    for item in items: 
        if not hero.isTrapped and not hero.isDead: 
            if hero.rect.colliderect(item.rect):
                goldEarned = item.useItem(hero, items, board, goldEarned)
        item.drawItem(screen)
    
    # controls monster movements and collisions
    for monster in monsters: 
        monster.animate()
        monster.drawMonster(screen)
        monster.update()
        monster.checkCollisions(obstacles, balloons, hero)
        monster.moveMonster(screen)

    # draw next round arrow 
    if len(monsters) == 0: 
        onePlayerSide.drawNext(screen)
        
    # controls balloon animations and collisions
    for balloon in balloons: 
        balloon.update(dt, screen, board, hero)
        balloon.animate()
        balloon.drawBalloon(screen)
    
    # explodes balloon
    if len(balloons) > 0: 
        for balloon in balloons: 
            if balloon.timer <= 0:
                balloon.explodeBalloon(screen, board, balloons, obstacles, monsters, items,hero, heroes)
                expEarned = balloon.checkCollisions(board, obstacles, monsters, items, heroes, expEarned) 
                board[balloon.row][balloon.col] = None 
                balloons.remove(balloon)
        
    # obstacle controls
    for obstacle in obstacles: 
        obstacle.drawObstacle(screen, board)

    # update database 
    collection.find_one_and_update( {'username': hero.name}, 
                                    {'$set': {'exp': hero.exp, 
                                              'level': hero.level, 
                                              'gold': hero.gold, 
                                              'needles': hero.needles}})

    pygame.display.flip()
    
## TWO PLAYER LOGIN SCREEN 

def twoPlayerStart(twoPlayerLogin, screen, p1Username, p1Password, p2Username, p2Password, input1, input2):
    font = pygame.font.Font('fonts/Kenney Future Narrow.ttf', 20)
    global state, hero1, hero2, heroes, heroOneBalloons, heroTwoBalloons
    w, h, c = SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE
     
    # draw screen and input boxes 
    twoPlayerLogin.drawLoginScreen(screen)
    p1Username.draw(screen)
    p1Password.draw(screen)
    p2Username.draw(screen)
    p2Password.draw(screen)


    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True 
    
        # handle account input 
        p1Username.handle_event(event)
        p1Password.handle_event(event)
        p2Username.handle_event(event)
        p2Password.handle_event(event)
    
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            
            # BUTTONS
            backButton = twoPlayerLogin.leftArrowRect
            loginButton = twoPlayerLogin.loginRect
            
            # go back to main menu 
            if backButton.collidepoint(pos): 
                input1.text, input2.text = '',''
                state = 'start'

            elif loginButton.collidepoint(pos): 
                # check that playerOne's account is valid 
                playerOne = collection.find_one({'username': p1Username.text})
                
                if playerOne != None: 
                
                    level, exp, dx = playerOne['level'], playerOne['exp'], playerOne['dx']
                    gold, needles = playerOne['gold'], playerOne['needles']
                    rounds, games = playerOne['rounds'], playerOne['games']
                    password = playerOne['password']
                
                    # make player one
                    if p1Password.text == password: 
                        hero1 = Hero(p1Username.text, exp, level, gold, needles, dx, rounds, games)
                        hero1.rect.x, hero1.rect.y = c*2, c*5

                    else: 
                        text = font.render('Player 1: Incorrect Password', True, DARKRED)
                        screen.blit(text, (w/2, h*.43))
                        break
                else:
                    text = font.render('Player 1: Account does not exist', True, DARKRED)
                    screen.blit(text, (w/2, h*.43))
                    break
                    
                # check that playerTwo's account is valid 
                playerTwo = collection.find_one({'username': p2Username.text})
                if playerTwo != None: 
                    password = playerTwo['password']
                    level, exp, dx = playerTwo['level'], playerTwo['exp'], playerTwo['dx']
                    gold, needles = playerTwo['gold'], playerTwo['needles']
                    rounds, games = playerTwo['rounds'], playerTwo['games']
                    
                    # since both players are valid, change state to start 
                    if p2Password.text == password: 
                        state = 'twoplayer'
                        hero2 = Hero(p2Username.text, exp, level, gold, needles, dx, rounds, games)
                        hero2.rect.x, hero2.rect.y = c*11, c*10
                        heroes, heroOneBalloons, heroOneBalloons = [hero1, hero2], [], []
                        board, obstacles, monsters, items = board1()
                        return  
                    else: 
                        text = font.render('Player 2: Incorrect Password', True, DARKRED)
                        screen.blit(text, (w*.5, h*.43))
                        break
                else:
                    text = font.render('Player 2: Account does not exist', True, DARKRED)
                    screen.blit(text, (w*.5, h*.43))
                    break
    
    pygame.display.flip() 
    

## TWO PLAYER PLAY LOOP 
def twoPlayer(twoPlayerSide, screen, dt, background, heroes, heroOneBalloons, heroTwoBalloons):
    global clock, obstacles, board, items, state, p1EXP, p2EXP, p1Gold, p2Gold, hero1, hero2
    monsters = []
    w, h, c = SCREEN_WIDTH, SCREEN_HEIGHT, CELL_SIZE
    
    # keeps track of game time 
    now = datetime.datetime.now()
    if now.minute < 10: 
        minute = '0' + str(now.minute)
    else: 
        minute = now.minute
    date = "%d/%d/%d   %d:%s" % (now.month, now.day, now.year, now.hour, minute)

    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
            
    keys = pygame.key.get_pressed()
   
    # move hero1 if not dead 
    
    if not hero1.isDead: 
        if keys[pygame.K_LEFT] == 1:
            hero1.goLeft()
        elif keys[pygame.K_RIGHT] == 1:
            hero1.goRight()
        elif keys[pygame.K_UP] == 1:
            hero1.goUp()
        elif keys[pygame.K_DOWN] == 1:
            hero1.goDown()
        elif keys[pygame.K_SPACE] == 1: 
            hero1.useHoldItem()
        
        if not hero1.isTrapped: 
            # drops balloon when rshift is pressed
            if keys[pygame.K_RSHIFT] == 1:
                r, c = hero1.row, hero1.col 
                if board[r][c] == None and len(heroOneBalloons) < hero1.numBalloons:
                    board[r][c] = Balloon(r,c, hero1)
                    heroOneBalloons.append(Balloon(r,c, hero1))
            
    # move hero2 if not dead 
    if not hero2.isDead: 
        if keys[pygame.K_a] == 1:
            hero2.goLeft()
        elif keys[pygame.K_d] == 1:
            hero2.goRight()
        elif keys[pygame.K_w] == 1:
            hero2.goUp()
        elif keys[pygame.K_s] == 1:
            hero2.goDown()
        elif keys[pygame.K_LCTRL] == 1: 
            hero2.useHoldItem()
            
        if not hero2.isTrapped: 
            # drops balloon when lshift is pressed
            if keys[pygame.K_LSHIFT] == 1:
                r, c = hero2.row, hero2.col 
                if board[r][c] == None and len(heroTwoBalloons) < hero2.numBalloons:
                    board[r][c] = Balloon(r,c, hero2)
                    heroTwoBalloons.append(Balloon(r,c, hero2))
            
    # draw background and side screen 
    background.drawGround(screen)
    twoPlayerSide.drawSide(screen)
    twoPlayerSide.drawContent(screen, hero1, hero2)
            
    balloons = heroOneBalloons + heroTwoBalloons
    
    # checks collisions with obstacles and balloons
    hero1.checkCollisions(obstacles, heroOneBalloons, monsters)
    hero2.checkCollisions(obstacles, heroTwoBalloons, monsters)
    
    # updates each hero 
    for hero in heroes: 
        hero.update(screen, dt)
        hero.isValidStep()
    
        if not hero.isTrapped and not hero.isDead: 
            hero.drawHero(screen)
            
        for balloon in balloons: 
            balloon.update(dt, screen, board, hero)
            balloon.animate()
            balloon.drawBalloon(screen)
            
        # kills hero if in bubble for more than 3 sec 
        if hero.timer <= 0: 
            hero.isTrapped = False
            hero.isDead = True 

    # intiates hero interaction with items and draws them 
    for item in items: 
        if hero1.rect.colliderect(item.rect):
            item.useItem(hero1, items, board, p1Gold)
        if hero2.rect.colliderect(item.rect):
            item.useItem(hero2, items, board, p2Gold)
        item.drawItem(screen)
            
    # draws obstacles 
    for obstacle in obstacles: 
        obstacle.drawObstacle(screen, board)
    
    # explodes hero1's balloons
    if len(heroOneBalloons) > 0: 
        for balloon in heroOneBalloons: 
            if balloon.timer <= 0:
                balloon.explodeBalloon(screen, board,heroOneBalloons , obstacles, monsters, items, hero1, heroes)
                balloon.checkCollisions(board, obstacles, monsters, items, heroes, p1EXP) 
                board[balloon.row][balloon.col] = None 
                heroOneBalloons.remove(balloon)

    # explodes hero2's balloons
    if len(heroTwoBalloons) > 0: 
        for balloon in heroTwoBalloons: 
            if balloon.timer <= 0:
                balloon.explodeBalloon(screen, board, heroTwoBalloons, obstacles, monsters, items, hero2, heroes)
                balloon.checkCollisions(board, obstacles, monsters, items, heroes, p2EXP) 
                board[balloon.row][balloon.col] = None
                heroTwoBalloons.remove(balloon)
                
    # gives exp and gold to the winner
    if hero1.isDead or hero2.isDead: 
        if hero1.isDead: 
            hero2.exp += 30
            p2EXP += 30 
            hero2.gold += 20
            p2Gold += 20 
            collection.find_one_and_update(
                {'username': hero2.name}, {'$set': {'exp': hero2.exp, 'gold':hero2.gold}})
        if hero2.isDead: 
            hero1.exp += 30 
            p1EXP += 30
            hero1.gold += 20
            p1Gold += 20 
            collection.find_one_and_update(
                {'username': hero1.name}, {'$set': {'exp': hero1.exp, 'gold':hero1.gold}})
        
        # update player 1 data in database
        currGame1 = dict()
        currGame1['gold'], currGame1['exp'] = p1Gold, p1EXP
        hero1.games[date] = currGame1
        hero1.rounds += 1
        
        collection.find_one_and_update(
            {'username': hero1.name}, {'$set': {'games': hero1.games, 'rounds':hero1.rounds}})
            
        # update player 2 data in database
        currGame2 = dict()
        currGame2['gold'] = p2Gold
        currGame2['exp'] = p2EXP
        hero2.games[date] = currGame2
        hero2.rounds += 1
        hero.dx = 10 
        hero2.numBalloons, hero2.balloonRange = 1, 1

        
        collection.find_one_and_update(
            {'username': hero2.name}, {'$set': {'games': hero2.games, 'rounds':hero2.rounds}})
            
        # reinitialize heroes
        p1Gold, p2Gold, p2EXP,p1EXP  = 0, 0, 0, 0
        hero1.rect.x, hero1.rect.y = c*2, c*5
        hero2.rect.x, hero2.rect.y = c*11, c*10
        hero1.isTrapped, hero1.isDead, hero2.isTrapped, hero2.isDead = False, False, False, False 
        hero1.timer, hero2.timer = 3, 3
        board, obstacles, monsters, items = board1()
        hero.dx = 10 
        hero1.numBalloons, hero1.numBalloons = 1, 1

        state = 'twoplayerlogin'
        return 

    # update hero1 in database
    collection.find_one_and_update( {'username': hero1.name}, 
                                    {'$set': {'exp': hero1.exp, 
                                              'level': hero1.level, 
                                              'gold': hero1.gold, 
                                              'needles': hero1.needles}})
        
    # update hero2 in database 
    collection.find_one_and_update( {'username': hero2.name}, 
                                    {'$set': {'exp': hero2.exp, 
                                              'level': hero2.level, 
                                              'gold': hero2.gold, 
                                              'needles': hero2.needles}})
    
    pygame.display.flip()
        
if __name__ == "__main__":
    main()