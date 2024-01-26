#where the magic happens
import pygame
import Card

# pygame setup
pygame.init()
#this sets up the screen size
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
card=Card.card
#this sets the ball in the center of the screen (initial position)
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

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
    pygame.draw.circle(screen, "red", player_pos, 40)

    #key pressing controll
    click=pygame.mouse
    
    # if click.get_pressed[pygame.BUTTON_LEFT]:
    #     card.clicked()
        
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_w]:
    #     player_pos.y -= 300 * dt
    # if keys[pygame.K_s]:
    #     player_pos.y += 300 * dt
    # if keys[pygame.K_a]:
    #     player_pos.x -= 300 * dt
    # if keys[pygame.K_d]:
    #     player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    #Refresh rate set 
    dt = clock.tick(60) / 1000

pygame.quit()