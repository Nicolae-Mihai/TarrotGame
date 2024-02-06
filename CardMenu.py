import pygame
from Button import Button
class CardMenu():
    
    def __init__(self,deck,screen,drawnCards) -> None:
        self.deck=deck
        self.drawnCards=drawnCards
        self.screen=screen
        self.background=pygame.image.load("tarrot cards/images/table.png") 
        self.background=pygame.transform.scale(self.background,(1280,720))
        buttonName=["back","shuffle","draw"]
        self.buttons=[]    
        ymod=0
        for name in buttonName:
            self.buttons.append(Button(1100,50*ymod+200,94,39,name,self.screen))
            ymod+=1
    def drawDrawnCards(self):
            self.screen.blit(self.background,(0,0))
            for button in self.buttons:
                button.draw()
            if self.drawnCards:
                for card in self.drawnCards:
                    card.setXandY(200*self.drawnCards.index(card)+350,300)
                    card.draw(self.screen)
    def eventHandler(self,deck,menu:str) ->str:
        if menu =="table":
            for button in self.buttons:
                if button.textRect.collidepoint(pygame.mouse.get_pos()):
                    match button.name:
                        case "shuffle":
                            print(button.name)
                            deck.shuffle()
                            menu="table"
                        case "draw":
                            print(button.name)
                            if len(self.drawnCards) <=2:
                                self.drawnCards.append(self.deck.removeOneCard())
                                menu="table"
                            else:
                                menu="table"
                                print("You can't draw any more cards!")
                        case "back":
                            print(button.name)
                            menu="initial"
                    return menu
        return menu

