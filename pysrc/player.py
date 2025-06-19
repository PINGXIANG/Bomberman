import pygame
from pysrc.config import *

class Player:
    def __init__(self, player_num, x, y):
        self.x = x
        self.y = y
        self.color = (150, 200, 255) if player_num == 1 else (255, 180, 200)
        self.controls = {
            1: {"up": pygame.K_w, "down": pygame.K_s, "left": pygame.K_a, "right": pygame.K_d},
            2: {"up": pygame.K_UP, "down": pygame.K_DOWN, "left": pygame.K_LEFT, "right": pygame.K_RIGHT}
        }[player_num]

    def handle_input(self, keys):
        if keys[self.controls["up"]]:
            self.y = max(1, self.y - 1)
        elif keys[self.controls["down"]]:
            self.y = min(MAP_HEIGHT - 2, self.y + 1)
        elif keys[self.controls["left"]]:
            self.x = max(1, self.x - 1)
        elif keys[self.controls["right"]]:
            self.x = min(MAP_WIDTH - 2, self.x + 1)

    def draw(self, screen):
        rect = pygame.Rect(self.x * TILE_SIZE + 8, self.y * TILE_SIZE + 8, TILE_SIZE - 16, TILE_SIZE - 16)
        pygame.draw.ellipse(screen, self.color, rect)
