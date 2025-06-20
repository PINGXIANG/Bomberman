import pygame
import random
from pysrc.config import *
from pysrc.bomb import Bomb

class BaseAI:
    def __init__(self, player_num, x, y):
        self.x = x
        self.y = y
        self.color = (200, 255, 180)
        self.alive = True

    def is_safe(self, x, y, bombs):
        for b in bombs:
            if b.x == x or b.y == y:
                if abs(b.x - x) <= 1 or abs(b.y - y) <= 1:
                    return False
        return True

    def draw(self, screen):
        rect = pygame.Rect(self.x * TILE_SIZE + 10, self.y * TILE_SIZE + 10, TILE_SIZE - 20, TILE_SIZE - 20)
        pygame.draw.rect(screen, self.color, rect)


class SimpleRandomAI(BaseAI):
    def __init__(self, player_num, x, y):
        super().__init__(player_num, x, y)
        self.dir = random.choice([(1,0), (-1,0), (0,1), (0,-1)])
        self.move_timer = 0

    def update(self, bombs, game_map):
        if not self.alive:
            return

        self.move_timer += 1
        if self.move_timer % 30 == 0:
            dx, dy = self.dir
            nx, ny = self.x + dx, self.y + dy
            if game_map.is_walkable(nx, ny) and self.is_safe(nx, ny, bombs):
                self.x, self.y = nx, ny
            else:
                self.dir = random.choice([(1,0), (-1,0), (0,1), (0,-1)])

            if random.random() < 0.2:
                if all(b.x != self.x or b.y != self.y for b in bombs):
                    bombs.append(Bomb(self.x, self.y))


class SimpleChaseAI(BaseAI):
    def __init__(self, player_num, x, y, get_targets_fn):
        super().__init__(player_num, x, y)
        self.get_targets = get_targets_fn

    def update(self, bombs, game_map):
        if not self.alive:
            return

        # 寻找最近的玩家
        targets = [p for p in self.get_targets() if p.alive]
        if not targets:
            return

        target = min(targets, key=lambda p: abs(p.x - self.x) + abs(p.y - self.y))
        dx = dy = 0
        if target.x < self.x:
            dx = -1
        elif target.x > self.x:
            dx = 1
        elif target.y < self.y:
            dy = -1
        elif target.y > self.y:
            dy = 1

        nx, ny = self.x + dx, self.y + dy
        if game_map.is_walkable(nx, ny) and self.is_safe(nx, ny, bombs):
            self.x, self.y = nx, ny

        # 靠近玩家时放炸弹
        if abs(self.x - target.x) + abs(self.y - target.y) <= 1:
            if all(b.x != self.x or b.y != self.y for b in bombs):
                bombs.append(Bomb(self.x, self.y))
