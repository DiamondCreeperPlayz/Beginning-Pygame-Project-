import pygame
import time

pygame.init()

gameSurface=pygame.display.set_mode((800,600)) 
gameSurface.fill((0,0,0)) 

bglogo = pygame.image.load("loading.jpg").convert_alpha() 
gameSurface.blit(bglogo,(0,0)) 
pygame.display.update()
time.sleep(15)