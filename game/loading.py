import pygame
from pygame.locals import *
import time
import sys

pygame.init()
 
pygame.display.set_caption('Loading')
size = [800, 600]
screen = pygame.display.set_mode(size)
for i in range(5, 15):
    while True:
        clock = pygame.time.Clock()

        pygame.display.update()
        basicfont = pygame.font.SysFont('Courier New', 48)
        text = basicfont.render('Loading.', True, (255, 255, 255), (0,0,0))
        textrect = text.get_rect()
        textrect.centerx = screen.get_rect().centerx
        textrect.centery = screen.get_rect().centery

        
        screen.fill((0,0,0))
        screen.blit(text, textrect)
        
        pygame.display.update()


        time.sleep(0.5)
        break
    while True:
        clock = pygame.time.Clock()

        pygame.display.update()
        basicfont = pygame.font.SysFont('Courier New', 48)
        text = basicfont.render('Loading..', True, (255, 255, 255), (0,0,0))
        textrect = text.get_rect()
        textrect.centerx = screen.get_rect().centerx
        textrect.centery = screen.get_rect().centery

        
        screen.fill((0,0,0))
        screen.blit(text, textrect)
        
        pygame.display.update()

        time.sleep(0.5)
        break
    while True:
        clock = pygame.time.Clock()

        pygame.display.update()
        basicfont = pygame.font.SysFont('Courier New', 48)
        text = basicfont.render('Loading...', True, (255, 255, 255), (0,0,0))
        textrect = text.get_rect()
        textrect.centerx = screen.get_rect().centerx
        textrect.centery = screen.get_rect().centery

        
        screen.fill((0,0,0))
        screen.blit(text, textrect)
        
        pygame.display.update()
        time.sleep(0.5)
        break

    while True:
        clock = pygame.time.Clock()

        pygame.display.update()
        basicfont = pygame.font.SysFont(None, 58)
        text = basicfont.render('Loaded...', True, (255, 255, 255), (0,0,0))
        textrect = text.get_rect()
        textrect.centerx = screen.get_rect().centerx
        textrect.centery = screen.get_rect().centery

        
        screen.fill((0,0,0))
        screen.blit(text, textrect)
        
        pygame.display.update()
        break

sys.exit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 
    clock.tick(20)