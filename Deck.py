#the deck of tarrot cards
import Card
import random

class Deck:
    deck=[]
    x=0
    y=0
    #constructor
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    #shuffles the deck, doesn't return anything
    def shuffle(self):
        for i in range(0,100):
            #we get a random number based on the size of the deck so we can pop it out of the deck
            rn=random.randint(0,self.__sizeof__())
            #we give the card variable the value of the item we are about to remove
            card=self.deck[rn]
            #we remove the card
            self.deck.remove(self.deck[rn])
            #we append the just removed card at the end of the list
            self.deck.append(card)
    
    #returns one card from the deck and removes it
    def removeOneCard(self):
        return self.deck.pop()
    
    #adds one card to the deck
    def addCard(self,card):
        self.deck.append(card)