import pygame
import random
import sys
from duck import Duck

pygame.init()

module_charge = pygame.init()
print(module_charge)

clock = pygame.time.Clock()

ecran = pygame.display.set_mode((1000,600))
ecran.fill((255, 255, 255))
pygame.display.set_caption("Duck Hunt")

# Set background image
wood_bg = pygame.image.load('./assets/background.png')

# Set Crosshair image
DEFAULT_IMAGE_SIZE = (100, 100)
crosshair = pygame.image.load('./assets/crosshair.png')
crosshair = pygame.transform.scale(crosshair, DEFAULT_IMAGE_SIZE)

# Duck object


# create duck list
ducks = []

for x in range(10):
    Duck.draw(Duck, ecran)
    ducks.append(Duck)


while True:
    # While loop for keep the window open

    # Key actions functions
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            crosshair_rect = crosshair.get_rect( center = event.pos )
        if event.type == pygame.MOUSEBUTTONUP:
            print("j'ai cliqué")
            click = posX, posY = pygame.mouse.get_pos()
            print(ducks.duck_pos)
            print(click)

    # Applying background (background always on top)
    ecran.blit(wood_bg, (0, 0))

    for duck_rect in ducks:
        ecran.blit(duck, duck_rect)

    ecran.blit(crosshair,crosshair_rect)
    pygame.display.update()
    clock.tick(100)
