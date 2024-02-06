from Button import Button
import pygame
class InitialMenu():
    
    y=100
    
    def __init__(self,screen,buttons):
        self.screen=screen
        self.buttonsNames=["reading","insertJSON","insertCard","deleteDB"]
        
        ymulti=1
        for name in self.buttonsNames:
            button=Button((screen.get_width()//2)-150,self.y*ymulti+50,94,39,name)
            buttons.append(button)
            ymulti=ymulti+1
        
    def drawInitialMenu(self,buttons):
    
        miau=(3, 6, 55)
        self.screen.fill(miau)

        for button in buttons:
            button.draw(self.screen)