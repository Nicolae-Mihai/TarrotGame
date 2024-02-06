import pygame
from Button import Button
class CardMenu():
    
    def __init__(self,deck,screen,drawnCards) -> None:
        self.deck=deck
        self.drawnCards=drawnCards
        self.screen=screen
        self.background=pygame.image.load("tarrot cards/images/table.png") 
        self.background=pygame.transform.scale(self.background,(1280,720))
        buttonName=["shuffle","draw","back"]
        self.buttons=[]    
        ymod=0
        for name in buttonName:
            self.buttons.append(Button(1200,50*ymod+50,94,39,name))
            ymod+=1
    def drawDrawnCards(self):
        self.screen.blit(self.background,(0,0))
        for button in self.buttons:
            button.draw(self.screen)
        if self.drawnCards:
            for card in self.drawnCards:
                card.setXandY(200*self.drawnCards.index(card)+350,300)
                card.draw(self.screen)
    def eventHandler(self,deck,menu:str) ->str:
        for button in self.buttons:
            print(button.name)
            if button.textRect.collidepoint(pygame.mouse.get_pos()):
                match button.name:
                    case "shuffle":
                        deck.shuffle()
                        menu="table"
                    case "draw":
                        self.drawnCards.append(self.deck.removeOneCard())
                        menu="table"
                    case "back":
                        menu="initial"
                return menu
        return menu

