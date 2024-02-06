import pygame
from TextBox import TextBox
class InsertJSON():
    
    def __init__(self,screen,conn):
        self.textBox=TextBox(350,350)
        self.screen=screen
        self.conn=conn
    def drawMenu(self):
        self.screen.fill("purple")
        self.textBox.draw(self.screen)
        for event in pygame.event.get():
                self.textBox.clicked(pygame.mouse.get_pos,event)
                
    def insert(self,loc):
        self.conn.insertJSON(loc)
