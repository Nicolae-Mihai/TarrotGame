#card class where it recieves the variables
import random
import pygame

class Card:
    width=150
    height=300
    def __init__(self,x,y,id,name,arcana,suit,img,fortuneTelling,keywords,lightMeanings,shadowMeanings,screen):
        self.screen=screen
        self.textColor=(124,73,166)
        self.textBackground=(2,47,64)
        self.font=pygame.font.Font('tarrot cards/Ldfcomicsans-jj7l.ttf', 24)
        self.rectangle=pygame.Rect(x,y,self.width,self.height)
        self.id=id
        self.name=name
        self.arcana=arcana
        self.suit=suit
        self.img=pygame.image.load("tarrot cards/images/"+img)
        self.img=pygame.transform.scale(self.img,(self.width,self.height))
        self.fortuneTelling=fortuneTelling
        self.keywords=keywords
        self.faceUp=False
        
        self.light=random.randint(0,1)
        self.filler=self.font.render("                                                                                                                                                                                                                                                                                                                       ",True,self.textColor,self.textBackground)
        self.fillerRect=self.filler.get_rect()
        self.fillerRect.center=(screen.get_width()//2,15)
        if self.light:
            self.meaning="This light card means "+lightMeanings[random.randint(0,len(lightMeanings)-1)]        
        else:
            self.meaning="The shadow card means "+shadowMeanings[random.randint(0,len(shadowMeanings)-1)]
        
        self.cardBack = pygame.image.load('tarrot cards/images/back.jpeg')
        self.cardBack= pygame.transform.scale(self.cardBack, (self.width, self.height))
    def draw(self):
        
        if self.faceUp:
            self.screen.blit(self.img,self.rectangle)
            self.text=self.font.render(self.meaning,True,self.textColor,self.textBackground)
            self.textRect=self.text.get_rect()
            self.textRect.center=(self.screen.get_width()//2,14)
            self.screen.blit(self.filler,self.fillerRect)
            self.screen.blit(self.text,self.textRect)

            
        else:
            self.screen.blit(self.cardBack,self.rectangle)
        self.cardBack
    
    def clicked(self,point):
        if self.rectangle.collidepoint(point):
            self.faceUp=True
            
    
    # def meaning(self)->str:
    #     if self.light:
    #         meaning="This is a light card and its meaning"
    #         return meaning
    #     else:
    #         meaning="The card is a shadow card and it meaning"
    #         return meaning
    
    def getPos(self):
        return [self.posX,self.posY]
    
    def setXandY(self,x,y):
        self.rectangle.x=x
        self.rectangle.y=y