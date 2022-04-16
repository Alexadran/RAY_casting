from settings import *
import pygame
import math


class Player():
    def __init__(self):
        self.x, self.y = 298.6354197533983, 60.4430593490879
        self.angle = player_angle

    def pos(self):
        return self.x, self.y

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.x += player_speed * cos_a
            self.y += player_speed * sin_a
        if keys[pygame.K_s]:
            self.x += -player_speed * cos_a
            self.y += -player_speed * sin_a
        if keys[pygame.K_a]:
            self.x += player_speed * sin_a
            self.y += -player_speed * cos_a
        if keys[pygame.K_d]:
            self.x += -player_speed * sin_a
            self.y += player_speed * cos_a
        if keys[pygame.K_LEFT]:
            if self.angle <= 0:
                self.angle = math.pi * 2 - 0.04 - self.angle
            else:
                self.angle -= 0.04
            if self.angle >= math.pi * 2:
                self.angle = self.angle - math.pi * 2
        if keys[pygame.K_RIGHT]:
            if self.angle <= 0:
                self.angle = math.fabs(self.angle) + 0.03
            else:
                self.angle += 0.03
            self.angle += 0.03
            if self.angle >= math.pi * 2:
                self.angle = self.angle - math.pi * 2

    def draw_yourself(self, sc):
        pygame.draw.circle(sc, "green", (self.x, self.y), 10)
