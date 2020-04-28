import os
import pygame
import math
import numpy
import random
import config

class Bird():

    def __init__(self):
        self.velx = config.BASE_VEL_Y
        self.vely = config.BASE_VEL_Y
        self.g = config.BASE_G
        self.angel = 0
        self.x = config.BASE_X
        self.y = config.BASE_Y
        self.time = 0

    def update(self, time):
        self.y += - config.BASE_VEL_Y * time + 1/2 * g * time**2
        self.angel = -numpy.arctan((-vel + self.g * time)/vel) /math.pi * 180


class Pipe():
 
    def __init__(self, time):
        self.y = random.randint(0, WINDOW_HEIGHT-1-config.PINE_SPACE)
        self.time_create = time
        self.x = WINDOW_WIDTH

    def update(self, time):
        if self.x < -config.PINE_WIDTH:
            del self
        else:
            self.x = WINDOW_WIDTH - (time - self.time_create)

    def position(self):
        return (self.x, self.y)


if __name__ == "__main__":
    pygame.font.init()

    WINDOW_WIDTH, WINDOW_HEIGHT = 288, 512
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Flappy bird")

    clock = pygame.time.Clock()
    tick = 1
    vel = config.BASE_VEL
    last_click = 0
    y = config.BASE_Y
    x = config.BASE_X
    g = config.BASE_G

    # load images
    BACKGROUND_IMAGE = [
        pygame.image.load(os.path.join("assets", "background-day.png")),
        pygame.image.load(os.path.join("assets", "background-night.png")),
    ]

    PIPE = pygame.image.load(os.path.join("assets", "pipe-green.png"))

    BIRD_IMAGE = [
        pygame.image.load(os.path.join("assets", "yellowbird-upflap.png")),
        pygame.image.load(os.path.join("assets", "yellowbird-midflap.png")),
        pygame.image.load(os.path.join("assets", "yellowbird-downflap.png")),
    ]

    bird = Bird()
    running = True
    while running:
        clock.tick(24)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                print("A keystoke is pressed")
                print('last_click:{} this_click:{}'.format(last_click, pygame.time.get_ticks()))
                last_click = pygame.time.get_ticks()
                
        SCREEN.blit(BACKGROUND_IMAGE[0], (0, 0))
        tick += 1
        time = (pygame.time.get_ticks() - last_click)/1000
        bird.update(time)
        SCREEN.blit(pygame.transform.rotate(BIRD_IMAGE[tick % 3], bird.angel), (bird.x, bird.y))
        print('bird_x:{}, bird_y{}, time:{}'.format(bird.x, bird.y, time))
        pygame.display.update()
 