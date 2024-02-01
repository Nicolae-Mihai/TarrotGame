#where the magic happens
import pygame
# import Card
# import Deck
# import Conn
from Conn import Conn
from Deck import Deck
from Card import Card
# pygame setup
pygame.init()
#this sets up the screen size
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
#this sets the ball in the center of the screen (initial position)
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
conn=Conn("mongodb://localhost:27017","Tarrot","Cards")
cards=conn.cardsList()
deck=Deck()
for card in cards:
    deck.addCard(Card(card["_id"],card["name"],card["arcana"],card["suit"],card["img"],card["fortune_telling"],card["keywords"],card.get("meanings",{}).get("light",[]),card.get("meanings",{}).get("shadow",[])))

def drawTable():
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
    click=pygame.mouse.get_pressed()
    
    # if click.get_pressed[pygame.BUTTON_LEFT]:
    #     pass
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    deck.getOneCard().draw()
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    #Refresh rate set 
    dt = clock.tick(60) / 1000

pygame.quit()