import pygame
import random
from pysrc.config import *

# 地图元素定义
WALL = "W"
BRICK = "B"
EMPTY = " "

class GameMap:
    def __init__(self):
        self.grid = [[EMPTY for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
        self._generate_map()

    def _generate_map(self):
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                if x == 0 or y == 0 or x == MAP_WIDTH - 1 or y == MAP_HEIGHT - 1:
                    self.grid[y][x] = WALL
                elif x % 2 == 0 and y % 2 == 0:
                    self.grid[y][x] = WALL
                elif random.random() < 0.7:
                    self.grid[y][x] = BRICK

        # 留出生点（左上 & 右下）
        self._clear_spawn_area(1)
        self._clear_spawn_area(2)

    def _clear_spawn_area(self, player_num):
        if player_num == 1:
            sx, sy = 1, 1
        else:
            sx, sy = MAP_WIDTH - 2, MAP_HEIGHT - 2
        for dx in range(2):
            for dy in range(2):
                self.grid[sy - dy][sx - dx] = EMPTY

    def draw(self, screen):
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                tile = self.grid[y][x]
                rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                color = {
                    WALL: (120, 120, 120),
                    BRICK: (245, 180, 130),
                    EMPTY: (255, 240, 250)
                }[tile]
                pygame.draw.rect(screen, color, rect)

    def get_spawn_point(self, player_num):
        return (1, 1) if player_num == 1 else (MAP_WIDTH - 2, MAP_HEIGHT - 2)
