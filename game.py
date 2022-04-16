import pygame.event
from settings import *
from player import Player
from ray_casting import ray_casting
from map import draw_map
from draw import *
from sound import *


def show_fps(sc, clock, width):
    font = pygame.font.SysFont('arial', 25)
    text = font.render("fps:", True, pygame.Color("red"))
    fps = font.render(str(int(clock.get_fps())), True, pygame.Color("red"))
    sc.blit(text, (width - 65, 5))
    sc.blit(fps, (width - 25, 5))


def start(width, height):
    pygame.init()
    sc = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    player = Player()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        player.movement()
        sc.fill(BLACK)
        ray_casting(sc, player.pos(), player.angle)
        show_fps(sc, clock, width)
        draw_map(sc)
        player.draw_yourself(sc)
        pygame.display.flip()
        clock.tick(FPS)


start(520, 320)