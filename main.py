import os
import pygame
import math
import numpy
import random
import config

class Bird():

    def __init__(self):
        self.velx = config.BASE_VEL
        self.vely = config.BASE_VEL_Y
        self.g = config.BASE_G
        self.angel = 0
        self.x = config.BASE_X
        self.y = config.BASE_Y
        self.time = 0
        self.start = False
        self.end = False

    def update(self, time):
            self.y += - config.BASE_VEL_Y * time + 1/2 * g * time**2
            self.angel = -numpy.arctan((-vel + self.g * time)/vel) /math.pi * 180

    def position(self):
        return (self.x, self.y)

    def begin(self):
        self.start = True

    def die(self):
        self.end = True

    def is_started(self):
        return self.start

    def is_ended(self):
        return self.end

class Pipe():
 
    def __init__(self, time):
        self.y = random.randint(20, WINDOW_HEIGHT-1-config.PIPE_SPACE-112)
        self.time_create = time
        self.x = WINDOW_WIDTH
        self.on_screen = True

    def __str__(self):
        return 'x:{}, y:{}, time_create:{}, on_screen:{}'.format(self.x, self.y, self.time_create, self.on_screen)

    def update(self, time):
        if self.x < -config.PINE_WIDTH:
            self.on_screen = False
        elif self.on_screen == True:
            self.x = WINDOW_WIDTH - (time - self.time_create)/10

    def up_pipe(self):
        return (self.x, self.y - 320)

    def down_pipe(self):
        return (self.x, self.y + config.PIPE_SPACE)


if __name__ == "__main__":
 
    # init pygame,val, ..
    pygame.font.init()
    WINDOW_WIDTH, WINDOW_HEIGHT = 288, 512
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Flappy bird")
    clock = pygame.time.Clock()
    tick = 1
    vel = config.BASE_VEL_Y
    last_click = 0
    y = config.BASE_Y
    x = config.BASE_X
    g = config.BASE_G
    pipes = []
    bird = Bird()

    # load images
    BACKGROUND_IMAGE = [
        pygame.image.load(os.path.join("assets", "background-day.png")),
        pygame.image.load(os.path.join("assets", "background-night.png")),
    ]

    BASE_IMAGE = pygame.image.load(os.path.join("assets", "base.png")).convert_alpha()
    BASE_MASK = pygame.mask.from_surface(BASE_IMAGE)
    BASE_POS = (0, 400)

    START_GAME_IMAGE = pygame.image.load(os.path.join("assets", "message.png"))
    GAME_OVER_IMAGE = pygame.image.load(os.path.join("assets", "gameover.png"))

    DOWN_PIPE_IMAGE = pygame.image.load(os.path.join("assets", "pipe-green.png")).convert_alpha()
    DOWN_PIPE_MASK = pygame.mask.from_surface(DOWN_PIPE_IMAGE)
    UP_PIPE_IMAGE = pygame.transform.rotate(DOWN_PIPE_IMAGE, 180)
    UP_PIPE_MASK = pygame.mask.from_surface(UP_PIPE_IMAGE)

    BIRD_IMAGE = [
        pygame.image.load(os.path.join("assets", "yellowbird-upflap.png")).convert_alpha(),
        pygame.image.load(os.path.join("assets", "yellowbird-midflap.png")).convert_alpha(),
        pygame.image.load(os.path.join("assets", "yellowbird-downflap.png")).convert_alpha(),
    ]

    BIRD_MASK = pygame.mask.from_surface(BIRD_IMAGE[0])

    # game loop
    running = True
    while running:
        clock.tick(24)
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                bird.begin()
                last_click = current_time

        # genarate pipe
        if current_time//3000 > len(pipes):
            pipes.append(Pipe(current_time))


        # update pipe and bird
        tick += 1
        time = (current_time - last_click)/1000
        if bird.is_started():
            bird.update(time)
        for pipe in pipes:
            pipe.update(current_time) 

        # check collision
        for pipe in pipes:
            distance_to_up_pipe = (math.floor(pipe.up_pipe()[0] - bird.x), math.floor(bird.y - pipe.up_pipe()[1]))
            distance_to_down_pipe = (math.floor(pipe.down_pipe()[0] - bird.x), math.floor(bird.y - pipe.down_pipe()[1]))
            if DOWN_PIPE_MASK.overlap(BIRD_MASK, distance_to_down_pipe):
                print('hit_down_pipe')
                bird.die()
            if UP_PIPE_MASK.overlap(BIRD_MASK, distance_to_up_pipe):
                print('hit_up_pipe')
                bird.die()
        if BASE_MASK.overlap(BIRD_MASK, (math.floor(bird.x), math.floor(BASE_POS[1]-bird.y))):
            print('hit_base')
            bird.die()

        # update screen
        SCREEN.blit(BACKGROUND_IMAGE[0], (0, 0))
        for pipe in pipes:
            SCREEN.blit(UP_PIPE_IMAGE, pipe.up_pipe())
            SCREEN.blit(DOWN_PIPE_IMAGE, pipe.down_pipe())
        SCREEN.blit(BASE_IMAGE, BASE_POS)
        SCREEN.blit(pygame.transform.rotate(BIRD_IMAGE[tick % 3], bird.angel), bird.position())

        # start game or game over screen
        if not bird.is_started() and not bird.is_ended():
            SCREEN.blit(START_GAME_IMAGE, (52, 123))
        if bird.is_started() and bird.is_ended():
            SCREEN.blit(GAME_OVER_IMAGE, (48, 180))
        pygame.display.update()
