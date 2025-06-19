import pygame
from pysrc.config import *
from pysrc.map import EMPTY, BRICK

class Bomb:
    def __init__(self, x, y, owner=None, fuse_time=3):
        self.x = x
        self.y = y
        self.fuse_time = fuse_time
        self.timer = 0
        self.exploded = False
        self.owner = owner

    def update(self, dt):
        self.timer += dt
        if self.timer >= self.fuse_time:
            self.exploded = True

    def draw(self, screen):
        rect = pygame.Rect(self.x * TILE_SIZE + 12, self.y * TILE_SIZE + 12, TILE_SIZE - 24, TILE_SIZE - 24)
        pygame.draw.circle(screen, (0, 0, 0), rect.center, TILE_SIZE // 4)

    def explode(self, game_map, range_len=1):
        affected_tiles = [(self.x, self.y)]

        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            for i in range(1, range_len + 1):
                tx, ty = self.x + dx * i, self.y + dy * i
                if not (0 <= tx < MAP_WIDTH and 0 <= ty < MAP_HEIGHT):
                    break
                tile = game_map.grid[ty][tx]
                affected_tiles.append((tx, ty))
                if tile == BRICK:
                    break
                elif tile != EMPTY:
                    break

        for x, y in affected_tiles:
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(game_map.surface, (255, 100, 100), rect)
            if game_map.grid[y][x] == BRICK:
                game_map.grid[y][x] = EMPTY
