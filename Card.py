#card class where it recieves the variables
import random
import pygame

class Card:
    width=150
    height=300
    def __init__(self,x,y,id,name,arcana,suit,img,fortuneTelling,keywords,lightMeanings,shadowMeanings):
        self.rectangle=pygame.Rect(x,y,self.width,self.height)
        self.id=id
        self.name=name
        self.arcana=arcana
        self.suit=suit
        self.img=pygame.image.load("tarrot cards/images/"+img)
        self.img=pygame.transform.scale(self.img,(self.width,self.height))
        self.fortuneTelling=fortuneTelling
        self.keywords=keywords        
        self.lightMeanings:lightMeanings
        self.shadowMeanings:shadowMeanings
        self.faceUp=False
        self.light=random.randint(0,1)
        self.cardBack = pygame.image.load('tarrot cards/images/back.jpeg')
        self.cardBack= pygame.transform.scale(self.cardBack, (self.width, self.height))
    
    def draw(self,screen):
        
        if self.faceUp:
            screen.blit(self.img,self.rectangle)
        else:
            screen.blit(self.cardBack,self.rectangle)
        self.cardBack
    
    def clicked(self,point):
        if self.rectangle.collidepoint(point):
            self.faceUp=True
    
    def meaning(self):
        if self.light:
            print("This is a light card and its meaning"+ self.lightMeanings[random.randint(0,self.lightMeanings.__size__)])
        else:
            print("The card is a shadow one and it meaning"+ self.lightMeanings[random.randint(0,self.lightMeanings.__size__)])
    
    def getPos(self):
        return [self.posX,self.posY]
    
    def setXandY(self,x,y):
        self.rectangle.x=x
        self.rectangle.y=y