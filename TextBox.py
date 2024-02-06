import pygame

class TextBox():

    def __init__(self,x,y) -> None:
        self.rect=pygame.Rect(x,y,140,32)
        self.font=pygame.font.Font('tarrot cards/Ldfcomicsans-jj7l.ttf',32)
        self.activeColor=pygame.Color('lightskyblue3')
        self.inactiveColor=pygame.Color('chartreuse4')
        self.userText=''
        self.color=self.inactiveColor
        self.active=False
    
    def clicked(self,point,event):
        if self.rect.collidepoint(point):
            self.active=True
        else:
            self.active=False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.k_BACKSPACE:
                user_text=user_text[:-1]
            else:
                user_text += event.unicode
        
        if self.active:
            self.color=self.activeColor
        else:
            self.color=self.inactiveColor 
    
    def draw(self,screen):
        
        pygame.draw.rect(screen,self.color,self.rect)
        self.textSurface=self.font.render(self.userText,True,(255,255,255))
        
        screen.blit(self.textSurface,(self.rect.x+5,self.rect.y+5))
        self.rect.w = max(100, self.textSurface.get_width()+10) 