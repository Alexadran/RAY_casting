import math

# game settings
FPS = 60
TILE = 40  # размер квадрата карты

# ray casting settings
FOV = math.pi / 3  # угол видимости
HALF_FOV = FOV / 2
NUM_RAYS = 200  # количество лучей
MAX_DEPTH = 800  # расстояние прорисовки
DELTA_ANGLE = FOV / NUM_RAYS  # угол между углами в FOV
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))  # расстояние игрока до стены независимо от TILE
PROJ_COEFF = 3 * DIST  # реальное расстояние на котором отрисуем стену

SCALE_MAP = 7
MAP_TILE = TILE // SCALE_MAP

player_angle = 2.1031853071795488
player_speed = 2

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 220, 0)
BLUE = (0, 186, 255)
DARKGRAY = (40, 40, 40)
PURPLE = (120, 0, 120)