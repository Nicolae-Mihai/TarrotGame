from TextBox import TextBox
import pygame
# name arcana suit img fortuneTelling keywords lightMeanings shadowMeanings
class InsertCard():
    def __init__(self,screen) -> None:
        self.textBox=TextBox(300,300)
        self.screen=screen
    def drawMenu(self):
        self.screen.fill("purple")
        self.textBox.draw(self.screen)
        
    def insertCard(self):
        pass
    def eventHandler(self,event):
        self.textBox.clicked(pygame.mouse.get_pos,event)
        