import pygame
from pysrc.config import *

class Player:
    def __init__(self, player_num, x, y):
        self.x = x
        self.y = y
        self.color = (150, 200, 255) if player_num == 1 else (255, 180, 200)
        self.controls = {
            1: {"up": pygame.K_w, "down": pygame.K_s, "left": pygame.K_a, "right": pygame.K_d, "bomb": pygame.K_SPACE},
            2: {"up": pygame.K_UP, "down": pygame.K_DOWN, "left": pygame.K_LEFT, "right": pygame.K_RIGHT, "bomb": pygame.K_RETURN}
        }[player_num]
        self.alive = True

    def handle_input(self, keys, bombs, game_map):
        if not self.alive:
            return

        if keys[self.controls["up"]] and game_map.is_walkable(self.x, self.y - 1):
            self.y -= 1
        elif keys[self.controls["down"]] and game_map.is_walkable(self.x, self.y + 1):
            self.y += 1
        elif keys[self.controls["left"]] and game_map.is_walkable(self.x - 1, self.y):
            self.x -= 1
        elif keys[self.controls["right"]] and game_map.is_walkable(self.x + 1, self.y):
            self.x += 1

        if keys[self.controls["bomb"]]:
            if all(b.x != self.x or b.y != self.y for b in bombs):
                bombs.append(__import__('pysrc.bomb').bomb.Bomb(self.x, self.y))

    def draw(self, screen):
        rect = pygame.Rect(self.x * TILE_SIZE + 8, self.y * TILE_SIZE + 8, TILE_SIZE - 16, TILE_SIZE - 16)
        pygame.draw.ellipse(screen, self.color, rect)
