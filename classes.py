import pygame
import random

class GameObj(pygame.sprite.Sprite):
    def __init__(self, screen):
        self.screen = screen


        def update(self):
            pass

class Taxi(GameObj):
    def __init__(self):
        super(GameObj,self).__init__()
        self.image = pygame.image.load('Taxi_assets/car5.png')
        self.image = pygame.transform.scale(self.image, (60, 40))
        self.rect = self.image.get_rect()

        self.rect.x = 250
        self.rect.y = 460
        self.pos = 1

    def update(self):
        pass

# 250 150 350
    def move(self, l_r):
        positions = [150,250,350]
        if l_r == 'left' and self.pos > 0:
            self.pos -= 1
        if l_r == 'right' and self.pos < 2:
            self.pos +=1
        self.rect.x = positions[self.pos]


#we need to integrate the spawning logic into this, might have to change it some
class Obstacle(GameObj):
    def __init__(self, ypos, vspeed):
        super(GameObj, self).__init__()
        self.image = pygame.image.load('Taxi_assets/car3.png')
        self.image = pygame.transform.scale(self.image, (60,40))
        self.rect = self.image.get_rect()

        positions = [150,250,350]
        self.rect.x = random.choice(positions)
        self.rect.y = 0
        self.vspeed = 3

    def update(self):
        self.rect.y += self.vspeed
        #if self.rect.y > 460:
            #self.kill()
        positions2 = [150,250,350]
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = random.choice(positions2)

