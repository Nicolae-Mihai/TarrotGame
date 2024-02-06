import pygame
from TextBox import TextBox
class InsertJSON():
    
    def __init__(self,screen,conn):
        self.textColor=(124,73,166)
        self.textBackground=(2,47,64)
        font=pygame.font.Font('tarrot cards/Ldfcomicsans-jj7l.ttf', 32)
        self.text1=font.render("Please provide the path of the json you wish ",True,self.textColor,self.textBackground)
        self.text2=font.render("to upload to the database using the textbox below!",True,self.textColor,self.textBackground)
        self.textBox=TextBox(350,350)
        self.textRect1=self.text1.get_rect()
        self.textRect1.center=(screen.get_width()//2,18)
        self.textRect2=self.text2.get_rect()
        self.textRect2.center=(screen.get_width()//2,57)
        self.screen=screen
        self.conn=conn
    def drawMenu(self):
        miau=(3, 6, 55)
        self.screen.fill(miau)
        self.screen.blit(self.text1,self.textRect1)
        self.screen.blit(self.text2,self.textRect2)
        self.textBox.draw(self.screen)
                
    def insert(self,loc):
        self.conn.insertJSON(loc)
