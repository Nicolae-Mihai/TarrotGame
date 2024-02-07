import pygame
from Button import Button
from TextBox import TextBox
class InsertJSON():
    
    def __init__(self,screen,conn):
        self.screen=screen
        self.textColor=(124,73,166)
        self.textBackground=(2,47,64)
        font=pygame.font.Font('tarrot cards/Ldfcomicsans-jj7l.ttf', 32)
        self.text1=font.render("Please provide the path of the json you wish ",True,self.textColor,self.textBackground)
        self.text2=font.render("to upload to the database using the textbox below!",True,self.textColor,self.textBackground)
        self.textBox=TextBox(self.screen.get_width()//2 - 70,434)
        self.textRect1=self.text1.get_rect()
        self.textRect1.center=(screen.get_width()//2,18)
        self.textRect2=self.text2.get_rect()
        self.textRect2.center=(screen.get_width()//2,57)
        self.conn=conn
        self.back=Button(1000,150,94,39,"back",self.screen)
        self.send=Button(self.screen.get_width()//2,500,94,39,"insert",self.screen)
        
    def drawMenu(self):
        miau=(3, 6, 55)
        self.screen.fill(miau)
        self.screen.blit(self.text1,self.textRect1)
        self.screen.blit(self.text2,self.textRect2)
        self.textBox.draw(self.screen)
        self.back.draw()
        self.send.draw()
        
    def eventHandler(self,menu:str)->str:
        if menu=="insert json":
            if self.send.textRect.collidepoint(pygame.mouse.get_pos()) and self.textBox.userText:
                self.insert("insert/"+self.textBox.userText+".json")
                menu="initial"
            else:
                print("Please make sure the JSON you are trying to insert is in the insert folder")
                menu = "insert json"
        return menu
    def insert(self,loc):
        try:
            self.conn.insertJSON(loc)
        except(FileNotFoundError):
            print("the JSON was not found")
        