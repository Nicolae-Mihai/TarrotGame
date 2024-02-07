import pygame

# this class creates the text boxes

class TextBox():

    def __init__(self,x,y,screen,name) -> None:
        self.rect=pygame.Rect(x,y,140,32)
        self.font=pygame.font.Font('tarrot cards/Ldfcomicsans-jj7l.ttf',32)
        self.activeColor=pygame.Color('lightskyblue3')
        self.inactiveColor=pygame.Color('chartreuse4')
        self.userText=''
        self.color=self.inactiveColor
        self.active=False
        self.screen=screen
        self.name=name
    
    # this checks if the checkbox has been clicked and then keeps listening for key events so it can display and load them
    def clicked(self,point,event,name):
        if self.rect.collidepoint(point) and self.name == name:
            self.active=True
        else:
            self.active=False
        
        if self.active:
            self.color=self.activeColor
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.userText=self.userText[:-1]
                else:
                    self.userText += event.unicode
        else:
            self.color=self.inactiveColor 
    
    def draw(self):
        
        self.textSurface=self.font.render(self.userText,True,(255,255,255))
        self.rect.w = max(400, self.textSurface.get_width()+10) 
        pygame.draw.rect(self.screen,self.color,self.rect)
        self.screen.blit(self.textSurface,(self.rect.x+5,self.rect.y+5))