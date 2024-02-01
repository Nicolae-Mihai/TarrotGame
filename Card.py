#card class where it recieves the variables
import random
import pygame

class Card:
    id:int
    name:str
    arcana:str
    suit:str
    img:str
    fortuneTelling:list
    keywords:list
    lightMeanings:list
    shadowMeanings:list
    faceUp:bool
    light:bool
    posX:int
    posY:int
    
    def __init__(self,id,name,arcana,suit,img,fortuneTelling,keywords,lightMeanings,shadowMeanings):
        
        self.id=id
        self.name=name
        self.arcana=arcana
        self.suit=suit
        self.img=pygame.image.load("tarrot cards/images/"+img)
        self.img=pygame.transform.scale(self.img,(int(75),int(150)))
        self.fortuneTelling=fortuneTelling
        self.keywords=keywords        
        self.lightMeanings:lightMeanings
        self.shadowMeanings:shadowMeanings
        self.faceUp=False
        self.light=random.randint(0,1)
        cardBack = pygame.image.load('tarrot cards/images/back.jpeg')
        self.cardBack=cardBack = pygame.transform.scale(cardBack, (int(75), int(150)))
    
    def draw(self,screen,rectangle):
        # myimage = pygame.image.load("myimage.bmp")
        # imagerect = myimage.get_rect()

        # while 1:
        #     your_code_here

        #     screen.fill(black)
        #     screen.blit(myimage, imagerect)
        #     pygame.display.flip()
        
        if not self.faceUp:
            screen.blit(self.img,rectangle)
        else:
            screen.blit(self.cardBack,rectangle)
        self.cardBack
    
    def clicked(self):
        self.faceUp=True
    
    def meaning(self):
        if self.light:
            print("This is a light card and its meaning"+ self.lightMeanings[random.randint(0,self.lightMeanings.__size__)])
        else:
            print("The card is a shadow one and it meaning"+ self.lightMeanings[random.randint(0,self.lightMeanings.__size__)])
    def getPos(self):
        return [self.posX,self.posY]