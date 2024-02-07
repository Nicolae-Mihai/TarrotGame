import pygame

class Button(pygame.Rect):
    textColor=(114, 4, 85)
    textBackground=(60, 7, 83)
  
    def __init__(self,x,y,width,height,name,screen):
        self.screen=screen
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.name=name
        font=pygame.font.Font('tarrot cards/Ldfcomicsans-jj7l.ttf', 32)
        self.text=font.render(f"button used for {name}",True,self.textColor,self.textBackground)
        self.textRect=self.text.get_rect()
    
    def draw(self):
        self.textRect.x = self.x
        self.textRect.y = self.y
        self.textRect.center=(self.x,self.y)
        self.screen.blit(self.text, self.textRect)
    # verifies if any of the buttons are pushed, mainly in the initial screen and when it's a "back button"
    def isClicked(self,name,point,menu:str)->str:
        
        if self.textRect.collidepoint(point):
            match name:
                case "reading":
                    menu="table"
                case "insertCard":
                    menu="insert card"
                case "insertJSON":
                    menu="insert json"
                case "deleteDB":
                    menu="delete DB"
                case "back":
                    menu="initial"
        return menu