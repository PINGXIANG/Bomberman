import pygame
from pysrc.map import GameMap
from pysrc.player import Player
from pysrc.bomb import Bomb
from pysrc.config import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("可爱泡泡堂 - 炸弹测试")

clock = pygame.time.Clock()

# 初始化地图和玩家
game_map = GameMap()
player1 = Player(1, *game_map.get_spawn_point(1))
player2 = Player(2, *game_map.get_spawn_point(2))

bombs = []

running = True
while running:
    dt = clock.tick(60) / 1000  # 每帧间隔秒数
    screen.fill(BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 处理输入
    keys = pygame.key.get_pressed()
    player1.handle_input(keys, bombs, game_map)
    player2.handle_input(keys, bombs, game_map)

    # 更新炸弹
    for bomb in bombs[:]:
        bomb.update(dt)
        if bomb.exploded:
            bomb.explode(game_map)
            bombs.remove(bomb)

    # 绘制地图、炸弹、玩家
    game_map.draw(screen)
    for bomb in bombs:
        bomb.draw(screen)
    player1.draw(screen)
    player2.draw(screen)

    pygame.display.flip()

pygame.quit()
