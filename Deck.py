#the deck of tarrot cards
import Card
import random

class Deck:
    deck=[]
    #constructor
    def __init__(self):
        pass
    
    #shuffles the deck, doesn't return anything
    def shuffle(self):
        for i in range(0,100):
            #we get a random number based on the size of the deck so we can pop it out of the deck
            rn=random.randint(0,self.__sizeof__())
            #we give the card variable the value of the item we are about to remove
            card=self.__getitem__(rn)
            #we remove the card
            self.remove(rn)
            #we append the just removed card at the end of the list
            self.append(card)
    
    #returns one card without removing it from the deck
    def getOneCard(self):
        return self.deck.__getitem__(0)
    
    #returns one card from the deck and removes it
    def removeOneCard(self):
        return self.deck.pop()
    
    #adds one card to the deck
    def addCard(self,card):
        self.deck.append(card)