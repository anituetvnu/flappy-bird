import os
import pygame

pygame.font.init()

WIDTH, HEIGHT = 288, 512
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy bird")

clock = pygame.time.Clock()
tick = 1
x = 10
y = 300
g = 17  # acceleration
vel = 10
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
    pass


print(BIRD_IMAGE[0])
running = True
while running:
    clock.tick(24)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            print(pygame.time.get_ticks())
            last_click = pygame.time.get_ticks()
            vel = 10
    SCREEN.fill((255, 255, 255))
    tick += 1
    time = (pygame.time.get_ticks() - last_click)/1000
    y += -vel * time + 1/2 * g * time**2

    SCREEN.blit(BIRD_IMAGE[tick % 3], (x, y))
    pygame.display.update()
