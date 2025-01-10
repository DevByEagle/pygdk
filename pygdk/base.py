import pygame
pygame.init()

def SetWindowSize(width, height):
    pygame.display.set_mode((width, height))

def Show():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()