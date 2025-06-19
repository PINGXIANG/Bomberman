import pygame
from pysrc.map import GameMap
from pysrc.player import Player
from pysrc.config import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("可爱泡泡堂 - 双人地图测试")

clock = pygame.time.Clock()

# 初始化地图和玩家
game_map = GameMap()
player1 = Player(1, *game_map.get_spawn_point(1))
player2 = Player(2, *game_map.get_spawn_point(2))

running = True
while running:
    screen.fill(BG_COLOR)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 处理输入
    keys = pygame.key.get_pressed()
    player1.handle_input(keys)
    player2.handle_input(keys)

    # 绘制地图 & 玩家
    game_map.draw(screen)
    player1.draw(screen)
    player2.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
