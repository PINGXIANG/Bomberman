import pygame
import random
from pysrc.config import *
from pysrc.bomb import Bomb

class AIPlayer:
    def __init__(self, player_num, x, y):
        self.x = x
        self.y = y
        self.color = (200, 255, 180)
        self.alive = True
        self.move_timer = 0
        self.dir = random.choice([(1,0), (-1,0), (0,1), (0,-1)])

    def update(self, bombs, game_map):
        if not self.alive:
            return

        self.move_timer += 1
        if self.move_timer % 30 == 0:
            dx, dy = self.dir
            nx, ny = self.x + dx, self.y + dy
            if game_map.is_walkable(nx, ny):
                self.x, self.y = nx, ny
            else:
                self.dir = random.choice([(1,0), (-1,0), (0,1), (0,-1)])

            # 随机放炸弹
            if random.random() < 0.2:
                if all(b.x != self.x or b.y != self.y for b in bombs):
                    bombs.append(Bomb(self.x, self.y))

    def draw(self, screen):
        rect = pygame.Rect(self.x * TILE_SIZE + 10, self.y * TILE_SIZE + 10, TILE_SIZE - 20, TILE_SIZE - 20)
        pygame.draw.rect(screen, self.color, rect)
