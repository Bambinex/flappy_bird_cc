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
        inclinaison = 0
        compteur1 = 0
        velocity = 0
        hauteur = y
        compteur2 = 0
        image = IMGS
    def jump(self):
        self.velocity = 3
        self.tick_count = 0
        self.height = self.y
    def move(self):
        self.tick_count = self.tick_count+1
        d = self.velocity*self.tick_count+0.5*3*self.tick_count**2


        if (d >= 16):
            d = ((d/abs(d))*16)
        if (d <= 0):
            d = d-2
        self.y = self.y + d
        if (d < 0 or self.y < self.height + 50):
            if (self.tilt  < self.MAX_ROTATION):
                self.tilt = self.MAX_ROTATION
        else:
            if (self.tilt > -90):
                self.tilt = self.tilt - self.ROT_VEL
    def draw(self,win):
        img_count += 1
        if (img_count < ANIMATION_TIME):
            img = IMGS[0]
        elif(img_count < ANIMATION_TIME * 2):
            img =IMGS[1]
        elif(img_count < ANIMATION_TIME * 3):
            img = IMGS[2]
        if(self.tilt <= -80):
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TRUE*2
        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft = (self.x, self.y)).center)
        win.blit(rotated_image,new_rect.topleft)
    def get_mask(self):
        return pygame.mask.from_surface(sel.img)

    
def main():
    run = True
    win = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
    clock = pygame.time.Clock()
    while (run):
        clock.tick(30)
        draw_window(win)
        draw_window(Bird)
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

