#where the magic happens
import pygame
import random
import time

from Button import Button
from Conn import Conn
from Deck import Deck
from Card import Card

# pygame setup
pygame.init()

y=150
ymulti=1
#this sets up the screen size
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Tarrot: The power within the cards')
clock = pygame.time.Clock()
running = True
# dt = 0
drawnCards=[]
buttons=[]

#this sets the ball in the center of the screen (initial position)
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
conn=Conn("mongodb://localhost:27017","Tarrot","Cards")
cards=conn.cardsList()
deck=Deck(100,100)

for card in cards:
    deck.addCard(Card(deck.x+random.randint(0,200),deck.y+random.randint(0,200),card["_id"],card["name"],card["arcana"],card["suit"],card["img"],card["fortune_telling"],card["keywords"],card.get("meanings",{}).get("light",[]),card.get("meanings",{}).get("shadow",[])))
def drawMenu():
    screen.fill("pink")
    buttonsNames=["reading","insertJSON","insertCard","DeleteDB"]
    ymulti=1
    for name in buttonsNames:
        button=Button(screen.get_width()//2,y*ymulti,300,100,name)
        buttons.append(button)
        ymulti=ymulti+1

    for button in buttons:
        button.draw(screen)
    
def drawDrawnCards(screen):
    if drawnCards:
        for card in drawnCards:
            card.setXandY(200*drawnCards.index(card)+400,300)
            card.draw(screen)
            
def drawTable(screen):
    pass


def eventHandler(event):
    match event:
        case "draw":
            drawnCards.append(deck.removeOneCard())
        case "shuffle":
            deck.shuffle()
        case 3:
            pass
        case 4:
            pass
        case 5:
            pass
        case 6:
            pass



while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("blue")

    #drawing is done like this
    pygame.draw.rect(screen, "red",(player_pos[0],player_pos[1],10,10))

    #key pressing controll
    
    
    if pygame.mouse.get_pressed()[0]:
        for drawn in drawnCards:
            drawn.clicked(pygame.mouse.get_pos())
        
        for button in buttons:
            button.isClicked(button.name,pygame.mouse.get_pos())
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_s]:
        eventHandler("shuffle")
    
    if keys[pygame.K_f] and len(drawnCards) !=3:
        eventHandler("draw")
    
    drawDrawnCards(screen)

    
    
    drawMenu()   
    
    # flip() the display to put your work on screen
    pygame.display.flip()
    
    #time sleep is here to controll the input delay so the keys are not registered as geting pressed multiple times
    time.sleep(0.12)

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    #Refresh rate set 
    # dt = clock.tick(60) / 1000


pygame.quit()