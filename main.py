import pygame
from pysrc.map import GameMap
from pysrc.player import Player
from pysrc.bomb import Bomb
from pysrc.ai import AIPlayer
from pysrc.config import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("可爱泡泡堂 - AI测试")

clock = pygame.time.Clock()

game_map = GameMap()
player1 = Player(1, *game_map.get_spawn_point(1))
player2 = Player(2, *game_map.get_spawn_point(2))
ai_player = AIPlayer(3, MAP_WIDTH // 2, MAP_HEIGHT // 2)

players = [player1, player2, ai_player]
bombs = []
explosions = []

running = True
while running:
    dt = clock.tick(60) / 1000
    screen.fill(BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if player1.alive:
        player1.handle_input(keys, bombs, game_map)
    if player2.alive:
        player2.handle_input(keys, bombs, game_map)

    if ai_player.alive:
        ai_player.update(bombs, game_map)

    # 炸弹处理
    for bomb in bombs[:]:
        bomb.update(dt)
        if bomb.exploded:
            new_explosions = bomb.explode(game_map)
            explosions.extend(new_explosions)
            bombs.remove(bomb)

    # 更新所有爆炸
    for explosion in explosions[:]:
        explosion.update(dt)
        if explosion.is_expired():
            explosions.remove(explosion)

    # 玩家死亡检测
    for explosion in explosions:
        for p in players:
            if p.alive and (p.x, p.y) == (explosion.x, explosion.y):
                p.alive = False    

    # 绘制爆炸
    for explosion in explosions:
        explosion.draw(screen)

    # 清除过时爆炸
    if explosions:
        explosions = explosions[1:] if len(explosions) > 10 else explosions

    # 绘制地图、炸弹、爆炸、玩家
    game_map.draw(screen)

    for ex in explosions:
        rect = pygame.Rect(ex.x * TILE_SIZE, ex.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(screen, (255, 120, 120), rect)

    for bomb in bombs:
        bomb.draw(screen)

    for p in players:
        if p.alive:
            p.draw(screen)

    pygame.display.flip()

pygame.quit()
