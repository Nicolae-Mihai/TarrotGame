from Button import Button
import pygame

# This class created the initial menu of the application

class InitialMenu():
    
    y=100
    
    def __init__(self,screen,buttons):
        self.screen=screen
        self.buttonsNames=["reading","insertJSON","insertCard","deleteDB"]
        
        ymulti=1
        for name in self.buttonsNames:
            button=Button((screen.get_width()//2),self.y*ymulti+50,94,39,name,self.screen)
            buttons.append(button)
            ymulti=ymulti+1
        
    def drawInitialMenu(self,buttons,dbDeleted,jsonInserted):
    
        miau=(3, 6, 55)
        mew=(23,54,13)
        self.screen.fill(miau)

        for button in buttons:
            button.draw()
            
        # if the database has been deleted this displays a message
        if dbDeleted:
            pygame.draw.line(self.screen,mew,(0,670),(1300,670),60)
            font=pygame.font.Font('tarrot cards/Ldfcomicsans-jj7l.ttf', 32)
            text=font.render("The DataBase has been deleted!",True,(3,6,55),(23,54,13))
            self.screen.blit(text,pygame.Rect(self.screen.get_width()//2-225,650,1,1))
        
        # if a json has been inserted this displays a message
        if jsonInserted:
            pygame.draw.line(self.screen,mew,(0,670),(1300,670),60)
            font=pygame.font.Font('tarrot cards/Ldfcomicsans-jj7l.ttf', 32)
            text=font.render("The Json has been inserted!",True,(3,6,55),(23,54,13))
            self.screen.blit(text,pygame.Rect(self.screen.get_width()//2-225,650,1,1))