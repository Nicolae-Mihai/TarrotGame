from TextBox import TextBox
from Button import Button
import pygame
# name arcana suit img fortuneTelling keywords lightMeanings shadowMeanings
class InsertCard():
    def __init__(self,screen,conn) -> None:
        self.dbf=["name","number","arcana", "suit", "img", "fortune_telling", "keywords", "meanings","light", "shadow"]
        i=100
        j=300
        self.textBox=[]
        for x in self.dbf:
            self.textBox.append(TextBox(i,j,screen,x))
            if not i%700 > 0:
                j+=100
                i=100
            i+=300
        
        
        self.screen=screen
        self.textColor=(124,73,166)
        self.textBackground=(2,47,64)
        font=pygame.font.Font('tarrot cards/Ldfcomicsans-jj7l.ttf', 32)
        self.text=font.render("Please fill the boxes with the required values",True,self.textColor,self.textBackground)
        self.conn=conn
        self.text.get_rect().center=(screen.get_width()//2,21)
        self.back=Button(1000,150,94,39,"back",self.screen)
        self.send=Button(screen.get_width()//2,500,94,39,"insert",screen)
    def drawMenu(self):
        self.screen.fill((3,6,55))
        self.screen.blit(self.text,self.text.get_rect())
        self.back.draw()
        self.send.draw()
        for textBox in self.textBox:
            textBox.draw()
        # for txtbx in self.textBox:
        #     txtbx.draw()
    def insertCard(self):
        self.conn.insertOne()
    def eventHandler(self,menu:str)->str:
        if menu=="insert card":
            if self.send.textRect.collidepoint(pygame.mouse.get_pos()):
                self.insertCard()
        return menu
    def insertCard(self):
        pass
        
        