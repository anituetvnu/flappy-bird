import os
import pygame
import math
import numpy

pygame.font.init()

WIDTH, HEIGHT = 288, 512
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy bird")

clock = pygame.time.Clock()
tick = 1
x = 130
y = 300
g = 30  # acceleration
basevel = 20
vel = basevel
last_click = 0

# load images
BACKGROUND_IMAGE = [
    pygame.image.load(os.path.join("assets", "background-day.png")),
    pygame.image.load(os.path.join("assets", "background-night.png")),
]

GREEN_PIPE = pygame.image.load(os.path.join("assets", "pipe-green.png"))

BIRD_IMAGE = [
    pygame.image.load(os.path.join("assets", "yellowbird-upflap.png")),
    pygame.image.load(os.path.join("assets", "yellowbird-midflap.png")),
    pygame.image.load(os.path.join("assets", "yellowbird-downflap.png")),
]


class Bird():
    basevely = 10

    def __init__(self):
        velx = basevely
        vely = basevely
        g = 10
        angel = 0
        x = 130
        y = 300
        time = 0

    def update(self, time):
        y += - basevely * time + 1/2 * g**2
        angel = -numpy.arctan((-vel + g * time)/vel) /math.pi * 180


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
            vel = basevel
    SCREEN.blit(BACKGROUND_IMAGE[0], (0, 0))
    tick += 1
    time = (pygame.time.get_ticks() - last_click)/1000
    y += -vel * time + 1/2 * g * time**2
    angel = -numpy.arctan((-vel + g * time)/20) / math.pi * 180
    SCREEN.blit(pygame.transform.rotate(BIRD_IMAGE[tick % 3], angel), (x, y))
    pygame.display.update()
