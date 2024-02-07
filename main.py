import pygame
import random
import time
from DeleteBD import deleteDB
from InsertCard import InsertCard
from InsertJson import InsertJSON
from InitialMenu import InitialMenu
from CardMenu import CardMenu
from Conn import Conn
from Deck import Deck
from Card import Card

# this is the main class and starts the whole application and checks if some buttons have been pressed
# pygame configuration
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Tarrot: The power within the cards')
clock = pygame.time.Clock()
running = True

menu="initial"
drawnCards=[]
buttons=[]

conn=Conn("mongodb://localhost:27017","Tarrot","Cards")
cards=conn.cardsList()

deck=Deck(100,100)
cardMenu=CardMenu(deck,screen,drawnCards)
initialMenu=InitialMenu(screen,buttons)
insertCard=InsertCard(screen,conn)
insertJson=InsertJSON(screen,conn)
deleteDb=deleteDB(screen, conn)

# this loads the cards from the database into the deck
for card in cards:
    deck.addCard(Card(deck.x+random.randint(0,200),deck.y+random.randint(0,200),card["_id"],card["name"],card["arcana"],card["suit"],card["img"],card["fortune_telling"],card["keywords"],card.get("meanings",{}).get("light",[]),card.get("meanings",{}).get("shadow",[]),screen))

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
        #mouse clicks controll
        if event.type==pygame.MOUSEBUTTONDOWN:   
        
            for drawn in drawnCards:
                drawn.clicked(pygame.mouse.get_pos())
            
            if menu == "initial":
                for button in buttons:
                    menu=button.isClicked(button.name,pygame.mouse.get_pos(),menu)    
                    deleteDb.deleted=False
                    insertJson.inserted=False
            if menu == "table":
                menu=cardMenu.eventHandler(deck,menu)
            
            if menu== "insert card":
                menu=insertCard.back.isClicked(insertCard.back.name,pygame.mouse.get_pos(),menu)           
                menu=insertCard.eventHandler(menu)
            if menu == "insert json":
                menu=insertJson.eventHandler(menu)
                menu=insertJson.back.isClicked(insertJson.back.name,pygame.mouse.get_pos(),menu)
            
            if menu == "delete DB":
                menu=deleteDb.eventHandler(menu)
        
        # this next two if's need to be here for the application to work
        if menu== "insert card":
            for x in insertCard.textBox:
                    x.clicked(pygame.mouse.get_pos(),event,x.name)
        
        if menu == "insert json":
            insertJson.textBox.clicked(pygame.mouse.get_pos(),event,"json")

    # this checks what menu has been selected and changes to it acordingly        
    match menu:
        case "initial":
            initialMenu.drawInitialMenu(buttons,deleteDb.deleted,insertJson.inserted)
        case "table":
            cardMenu.drawDrawnCards()
        case "insert card":
            insertCard.drawMenu()
        case "insert json":
            insertJson.drawMenu()
        case "delete DB":
            deleteDb.draw()
        
    # this displays the screen 
    pygame.display.flip()
    
    #time sleep is here to controll the input delay so the keys are not registered as geting pressed multiple times
    time.sleep(0.12)


pygame.quit()