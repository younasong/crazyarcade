# Youna Song (younas)
# 12/07/2017
# 15-112 Term Project

"""
This class controls the text input for user accounts 
Code is NOT my own and was taken and modified from: 
    https://stackoverflow.com/questions/47491451/how-to-implement-two-input-boxes-in-pygame-without-having-to-repeat-code
"""

import pygame
from constants import * 

class InputBox():
    def __init__(self, x, y):
        self.font = pygame.font.Font('fonts/Kenney Future Narrow.ttf', 20)
        self.inputBox = pygame.Rect(x, y, 140, 32)
        self.colorInactive = BLACK
        self.colorActive = BLACK
        self.color = self.colorInactive
        self.text = ''
        self.active = False

    def handle_event(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.inputBox.collidepoint(event.pos)
            self.color = self.colorActive if self.active else self.colorInactive
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def draw(self, screen):
        txtSurface = self.font.render(self.text, True, self.color)
        width = max(200, txtSurface.get_width()+10)
        self.inputBox.w = width
        screen.blit(txtSurface, (self.inputBox.x+5, self.inputBox.y+5))
        pygame.draw.rect(screen, self.color, self.inputBox, 2)
        self.color = BLACK
        