import pygame
import time
import random

display_width = 800
display_height = 600
 
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
 
block_color = (53,115,255)
 
bg = pygame.image.load('loading.jpg')



gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("Menu")
clock = pygame.time.Clock()
pygame.init()


def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

intro = True

while intro:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
                
    gameDisplay.fill(black)
    basicfont = pygame.font.SysFont('Courier New', 115)
    TextSurf, TextRect = text_objects("Jake Leroux", basicfont)
    TextRect.center = ((display_width/2),(display_height/2))
    gameSurface=pygame.display.set_mode((800,600)) 
    gameSurface.fill((0,0,0)) 

    bglogo = pygame.image.load("loading.jpg").convert_alpha() 
    gameSurface.blit(bglogo,(0,0)) 
    pygame.display.update()
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    clock.tick(15)
    time.sleep(5.0)