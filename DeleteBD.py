import pygame
from Button import Button

# this class creates the delete database screen

class deleteDB():
    
    def __init__(self,screen,conn):
        self.screen=screen
        self.conn=conn
        self.textColor=(124,73,166)
        self.textBackground=(2,47,64)
        font=pygame.font.Font('tarrot cards/Ldfcomicsans-jj7l.ttf',32)
        self.text=font.render("Are you sure that you want to delete the database?",True,self.textColor,self.textBackground)
        self.textRect=self.text.get_rect()
        self.textRect.center=(screen.get_width()//2,200,)
        self.yes=Button(screen.get_width()//4,550,94,39,"yes",self.screen)
        self.no=Button(screen.get_width()//4*3,550,94,39,"no",self.screen)
        self.deleted=False
    
    def draw(self):
        miau=(3,6,55)
        self.screen.fill(miau)
        self.screen.blit(self.text,self.textRect)
        self.yes.draw()
        self.no.draw()
    
    # This checks which button has been pressed
    def eventHandler(self,menu:str) ->str:
        if menu=="delete DB":
            if self.yes.textRect.collidepoint(pygame.mouse.get_pos()):
                self.conn.delete("database",1)
                menu="initial"
                self.deleted=True
            elif self.no.textRect.collidepoint(pygame.mouse.get_pos()):
                menu="initial"
        return menu