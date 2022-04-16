import pygame.draw

from settings import *

map = (
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1),
    (1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1),
    (1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1),
    (1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1),
    (1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1),
    (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1),
)


def draw_map(sc):
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x]:
                pygame.draw.rect(sc, "white", (x * TILE, y * TILE, TILE, TILE), 1)


world_map = set()
for y, row in enumerate(map):
    for x, char in enumerate(row):
        if char:
            world_map.add((x, y))
