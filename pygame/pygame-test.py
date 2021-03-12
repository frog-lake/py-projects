# code referenced from here: https://realpython.com/pygame-a-primer/

# currently unfinished attempt at a game in pygame

# simple pygame program

# import and init the pygame library
import pygame
pygame.init()

# set up drawing window
screen = pygame.display.set_mode([500, 500])

# run until the user asks to quit
running = True
while running:

    # check if user tries to close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # fill bg with white
    screen.fill((255, 255, 255))

    # draw a solid blue circle in the center
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    # flip the display
    pygame.display.flip()

pygame.quit()
