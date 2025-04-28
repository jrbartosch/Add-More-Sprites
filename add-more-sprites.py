import pygame
import random
from pygame import mixer
scrnwidth = 800
scrnheight = 500
enemystartymin = 50
enemystartymax = 450
enemystartxmin = 50
enemystartxmax = 750
pygame.init()
mixer.init()
screen = pygame.display.set_mode((scrnwidth, scrnheight))
pygame.display.set_caption('Catch the Enemies')
bg = pygame.image.load('bg.jpg')
clock = pygame.time.Clock()
player = pygame.Rect(400, 300, 50, 50)
player_color = (0, 255, 0)
player_speed_x = 5
player_speed_y = 5
enemies = [pygame.Rect(random.randint(enemystartxmin, enemystartxmax), random.randint(enemystartymin, enemystartymax), 50, 50) for _ in range(7)]
enemy_color = (255, 0, 0)
score = 0
font = pygame.font.Font(None, 64)
mixer.music.load('music.wav')
mixer.music.set_volume(0.7)
mixer.music.play(-1)
running = True
while running:
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_speed_y = -5
    elif keys[pygame.K_DOWN]:
        player_speed_y = 5
    else:
        player_speed_y = 0
    if keys[pygame.K_LEFT]:
        player_speed_x = -5
    elif keys[pygame.K_RIGHT]:
        player_speed_x = 5
    else:
        player_speed_x = 0
    player.x += player_speed_x
    player.y += player_speed_y
    if player.x <= 0:
        player.x = 0
        player_speed_x = 0
    if player.x + player.width >= scrnwidth:
        player.x = scrnwidth - player.width
        player_speed_x = 0
    if player.y <= 0:
        player.y = 0
        player_speed_y = 0
    if player.y + player.height >= scrnheight:
        player.y = scrnheight - player.height
        player_speed_y = 0
    pygame.draw.rect(screen, player_color, player)
    for enemy in enemies[:]:
        pygame.draw.rect(screen, enemy_color, enemy)
        if player.colliderect(enemy):
            enemies.remove(enemy)
            enemies.append(pygame.Rect(random.randint(enemystartxmin, enemystartxmax), random.randint(enemystartymin, enemystartymax), 50, 50))
            score += 1
            mixer.Sound('achievement.wav').play()
    if score >= 50:
        screen.fill((0, 0, 0))
        win_text = font.render('YOU WIN!', True, (pygame.Color('red')))
        screen.blit(win_text, (scrnwidth // 2 - win_text.get_width() // 2, scrnheight // 2 - win_text.get_height() // 2))
        pygame.display.flip()
        pygame.time.wait(3000)
        running = False
    score_text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()