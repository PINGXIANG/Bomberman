import pygame
from pysrc.config import *

class Explosion:
    def __init__(self, x, y, duration=0.3):
        self.x = x
        self.y = y
        self.timer = 0
        self.duration = duration

    def update(self, dt):
        self.timer += dt

    def is_expired(self):
        return self.timer >= self.duration

    def draw(self, screen):
        rect = pygame.Rect(self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(screen, (255, 100, 100), rect)
