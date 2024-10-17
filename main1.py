import random
import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/тир.jpg")
pygame.display.set_icon(icon)

target_image = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

# Начальные координаты цели
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Начальные значения для очков и скорости движения цели
score = 0
target_speed_x = random.choice([-3, 3])  # Скорость по оси X
target_speed_y = random.choice([-3, 3])  # Скорость по оси Y

running = True
while running:
    screen.fill((255, 255, 255))  # Задаем белый фон for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                score += 1  # Увеличиваем счет на 1 target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    # Перемещение цели
    target_x += target_speed_x
    target_y += target_speed_y

    # Проверка на столкновение с границами экрана
    if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
        target_speed_x = -target_speed_x  # Изменяем направление по оси X if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
        target_speed_y = -target_speed_y  # Изменяем направление по оси Y

    # Отображение цели screen.blit(target_image, (target_x, target_y))

    # Отображение счета font = pygame.font.Font(None, 36)
    score_text = font.render(f"Очки: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()