import pygame, sys
from pygame.locals import QUIT
pygame.init()
shape = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Q4Picture')

blue = (0, 0, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
pygame.draw.rect(shape, blue, (0, 0, 400, 250))
pygame.draw.circle(shape, yellow, (10, 10), 50)
pygame.draw.polygon(shape, red, [(100, 200), (300, 200), (200, 50)])
pygame.draw.rect(shape, black, (2, 2, 15, 15))
pygame.draw.rect(shape, black, (36, 2, 15, 15))
pygame.draw.rect(shape, black, (17, 6, 19, 5))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()