#card class where it recieves the variables
import random
import pygame

class card:
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
    def __init__(self,id,name,arcana,suit,img,fortuneTelling,keywords,lightMeanings,shadowMeanings) -> None:
        
        self.id=id
        self.name=name
        self.arcana=arcana
        self.suit=suit
        self.img=img
        self.fortuneTelling=fortuneTelling
        self.keywords=keywords        
        self.lightMeanings:lightMeanings
        self.shadowMeanings:shadowMeanings
        self.faceUp=False
        self.light=random.randint(0,1)
    
    def draw(self):
        if self.faceUp:
            pygame.image.load("/images/"+self.img+".jpg")
        else:
            pygame.image.load("/images/back.jpg")
    
    def clicked(self):
        self.faceUp=True
    
    def meaning(self):
        if self.light:
            print("This is a light card and its meaning"+ self.lightMeanings[random.randint(0,self.lightMeanings.__size__)])
        else:
            print("The card is a shadow one and it meaning"+ self.lightMeanings[random.randint(0,self.lightMeanings.__size__)])
    def getPos(self):
        return [self.posX,self.posY]
    
    def draw():
        pass