#where the magic happens
import pygame
import random
import time
from InsertCard import InsertCard
from InsertJson import InsertJSON
from InitialMenu import InitialMenu
from CardMenu import CardMenu
from Conn import Conn
from Deck import Deck
from Card import Card

# pygame setup
pygame.init()

menu="initial"
#this sets up the screen size
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Tarrot: The power within the cards')
clock = pygame.time.Clock()
running = True
drawnCards=[]
buttons=[]
conn=Conn("mongodb://localhost:27017","Tarrot","Cards")
cards=conn.cardsList()
deck=Deck(100,100)
cardMenu=CardMenu(deck,screen,drawnCards)
initialMenu=InitialMenu(screen,buttons)
insertCard=InsertCard(screen)
insertJson=InsertJSON(screen,conn)
for card in cards:
    deck.addCard(Card(deck.x+random.randint(0,200),deck.y+random.randint(0,200),card["_id"],card["name"],card["arcana"],card["suit"],card["img"],card["fortune_telling"],card["keywords"],card.get("meanings",{}).get("light",[]),card.get("meanings",{}).get("shadow",[])))


while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
        #mouse clicks controll
        if event.type==pygame.MOUSEBUTTONDOWN:   
        
            for drawn in drawnCards:
                drawn.clicked(pygame.mouse.get_pos())
            if menu=="initial":
                for button in buttons:
                    menu=button.isClicked(button.name,pygame.mouse.get_pos(),menu)    
            if menu=="table":
                menu=cardMenu.eventHandler(deck,menu)
        #key pressing controll
        # merge all events into their spcecific classes
        if event.type == pygame.KEYDOWN:
                
            if event.key==pygame.K_d and len(drawnCards) !=3:
                cardMenu.eventHandler(deck,"draw")
                
            if event.key==pygame.K_s:
                cardMenu.eventHandler(deck,"shuffle")
            
        
    match menu:
        case "initial":
            initialMenu.drawInitialMenu(buttons)
        case "table":
            cardMenu.drawDrawnCards()
        case "insert card":
            insertCard.drawMenu()
        case "insert json":
            insertJson.drawMenu()
        case "delete DB":
            conn.delete("database",1)
        
    pygame.display.flip()
    
    #time sleep is here to controll the input delay so the keys are not registered as geting pressed multiple times
    time.sleep(0.12)


pygame.quit()