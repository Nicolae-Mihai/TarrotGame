import pygame

class Button(pygame.Rect):
    
    def __init__(self,x,y,width,height,name):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.name=name
        font=pygame.font.Font('tarrot cards/Ldfcomicsans-jj7l.ttf', 32)
        self.text=font.render(f"button used for {name}",True,"green","blue")
        self.textRect=self.text.get_rect()
    def draw(self,screen):
        pygame.draw.rect(screen,"red",self)
        self.textRect.center=(self.x//2,self.y//2)
        screen.blit(self.text, self.textRect)
    
    def isClicked(self,name,point):
        if self.collidepoint(point):
            match name:
                case "reading":
                    print(self.name)
                    pass
                case "insertJSON":
                    print(self.name)
                    pass
                case "insertCard":
                    print(self.name)
                    pass
                case "deleteDB":
                    print(self.name)
                    pass