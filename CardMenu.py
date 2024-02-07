import pygame
from Button import Button

# this class creates the menu where the game is played

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
        # loads the buttons into the array
        for name in buttonName:
            self.buttons.append(Button(1100,50*ymod+200,94,39,name,self.screen))
            ymod+=1
    
    def drawDrawnCards(self):
            self.screen.blit(self.background,(0,0))
            pygame.draw.line(self.screen,(3,6,55),(0,0),(1300,0),166)

            for button in self.buttons:
                button.draw()
            
            if self.drawnCards:
                for card in self.drawnCards:
                    card.setXandY(200*self.drawnCards.index(card)+350,300)
                    card.draw(self.screen.get_width()//2,self.drawnCards.index(card)*28+13)
            
            # displays a message if the deck has been shuffled
            if self.deck.shuffled:
                font=pygame.font.Font('tarrot cards/Ldfcomicsans-jj7l.ttf', 32)
                text=font.render("The deck is shuffled!",True,(0,0,0),(60,60,60))
                self.screen.blit(text,pygame.Rect(self.screen.get_width()//2-200,650,1,1))
    
    # Checks to see which button from this menu has been pressed
    def eventHandler(self,deck,menu:str) ->str:
    
        if menu =="table":
            for button in self.buttons:
                if button.textRect.collidepoint(pygame.mouse.get_pos()):
                    match button.name:
                    
                        case "shuffle":
                            print(button.name)
                            deck.shuffle()
                            
                        case "draw":
                            print(button.name)
                            if len(self.drawnCards) <=2:
                                self.drawnCards.append(self.deck.removeOneCard())
                            else:
                                font=pygame.font.Font('tarrot cards/Ldfcomicsans-jj7l.ttf', 32)
                                text=font.render("You can't draw any more cards!",True,(3,6,55),(10,10,10))
                                self.screen.blit(text,pygame.Rect(self.screen.get_width()//2-200,650,1,1))
                            self.deck.shuffled=False
                        case "back":
                            print(button.name)
                            menu="initial"
        return menu

