import pygame
import random


pygame.init()

# Размер окна игры
screen_width = 640
screen_height = 480

# Создание окна
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ловец листьев")

# Загрузка фонового изображения
background_image = pygame.image.load("fon.png")  
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Загрузка изображения яблока
apple_image = pygame.image.load("listja.png")  
apple_image = pygame.transform.scale(apple_image, (50, 40))

# Загрузка изображения корзины
korzina_image = pygame.image.load("korzina.png")  
korzina_image = pygame.transform.scale(korzina_image, (100, 100))

# Параметры яблока
apple_x = random.randint(0, screen_width - apple_image.get_width())
apple_y = 0
apple_speed = 5

# Параметры корзины
korzina_x = screen_width // 2 - korzina_image.get_width() // 2
korzina_y = screen_height // 1.5
korzina_speed = 10

# Счетчик
score = 0

clock = pygame.time.Clock()
game_over = False

# Функция загрузки изображения
def load_image(file_path):
    image = pygame.image.load(file_path)
    return image

# Основной игровой цикл
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Движение корзины
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        korzina_x -= korzina_speed
    if keys[pygame.K_RIGHT]:
        korzina_x += korzina_speed

    # Перемещение листьев
    apple_y += apple_speed

    # Создание объектов
    apple_rect = pygame.Rect(apple_x, apple_y, apple_image.get_width(), apple_image.get_height())
    korzina_rect = pygame.Rect(korzina_x, korzina_y, korzina_image.get_width(), korzina_image.get_height())

    # Обнаружение столкновения листьев с корзиной
    if apple_rect.colliderect(korzina_rect):
        score += 1
        apple_x = random.randint(0, screen_width - apple_image.get_width())
        apple_y = 0

    # Не пойманные листья
    if apple_y + apple_image.get_height() > screen_height:
        score -= 1
        apple_x = random.randint(0, screen_width - apple_image.get_width())
        apple_y = 0

    screen.blit(background_image, (0, 0))  # Отображение фонового изображения

    # Отрисовка листьев
    screen.blit(apple_image, (apple_x, apple_y))

    # Отрисовка корзины
    screen.blit(korzina_image, (korzina_x, korzina_y))

    # Отрисовка счетчика
    font = pygame.font.Font(None, 36)
    text = font.render("Счет: " + str(score), True, (255, 255, 255))
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

# Завершение игры
pygame.quit()
