import pygame
import random
import math
import os
import time
pygame.font.init()

WIN_WIDTH = 290
WIN_HEIGHT = 700

nom_image = pygame.transform.scale2x(pygame.image.load(os.path.join("/home/philippe/Bureau","bg.png")))

def draw_window(win):
    win.blit(nom_image, (0,0))
    pygame.display.update()

def main():
    run = True
    win = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
    clock = pygame.time.Clock()
    while (run):
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
            draw_window(win)

if __name__ == "__main__":
    main()

nom_tableau = [pygame.transform.scale2x(pygame.image.load(os.path.join("/home/philippe/Bureau", "bird1.png"))),
pygame.transform.scale2x(pygame.image.load(os.path.join("/home/philippe/Bureau", "bird2.png"))),
pygame.transform.scale2x(pygame.image.load(os.path.join("/home/philippe/Bureau", "bird3.png")))]

class Bird:
    IMGS = nom_tableau
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_TIME = 5
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
