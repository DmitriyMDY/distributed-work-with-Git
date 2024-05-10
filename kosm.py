import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра тир")
icon = pygame.image.load("img/soldat.png")
pygame.display.set_icon(icon)
target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
target_speed = 5

score = 0
font = pygame.font.SysFont(None, 36)


# Функция для создания страшного животного
def spawn_enemy():
    enemy_img = pygame.image.load("img/kosm.png")
    enemy_width = 50
    enemy_height = 50
    enemy_x = random.randint(0, SCREEN_WIDTH - enemy_width)
    enemy_y = random.randint(0, SCREEN_HEIGHT - enemy_height)
    enemy_speed_x = random.randint(-3, 3)  # Случайная скорость по оси X
    enemy_speed_y = random.randint(-3, 3)  # Случайная скорость по оси Y
    return {
        "rect": pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height),
        "img": enemy_img,
        "speed_x": enemy_speed_x,
        "speed_y": enemy_speed_y
    }

# Создаем список страшных животных
enemies = [spawn_enemy() for _ in range(1)]  # Только одно страшное животное

running = True
clock = pygame.time.Clock()
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            target_rect = pygame.Rect(target_x, target_y, target_width, target_height)
            if target_rect.collidepoint(mouse_x, mouse_y):
                score += 1
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        target_x -= target_speed
    if keys[pygame.K_RIGHT]:
        target_x += target_speed
    if keys[pygame.K_UP]:
        target_y -= target_speed
    if keys[pygame.K_DOWN]:
        target_y += target_speed

    screen.blit(target_img, (target_x, target_y))

    # Рисуем и обновляем страшных животных
    for enemy in enemies:
        screen.blit(pygame.image.load("img/kosm.png"), enemy.topleft)

    # Проверка столкновений с врагами
    #for enemy in enemies:
        #if target_img.colliderect(enemy):
            #score -= 1  # Уменьшаем счет при столкновении с врагом

    # Обновляем счет на экране
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()