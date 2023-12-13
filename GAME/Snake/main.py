import pygame
import time

pygame.init()

# Ukuran layar
width = 800
height = 600

# Warna
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Inisialisasi layar
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Permainan Ular')

# Kecepatan dan ukuran ular
snake_speed = 15
snake_block = 20

# Font untuk skor
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

def gameLoop():
    game_over = False
    game_close = False

    # Koordinat awal ular
    x1 = width / 2
    y1 = height / 2

    # Perubahan koordinat
    x1_change = 0
    y1_change = 0

    # Daftar koordinat badan ular
    snake_List = []
    Length_of_snake = 1

    # Koordinat makanan
    foodx = round((round(width / snake_block) / 2) * snake_block)
    foody = round((round(height / snake_block) / 2) * snake_block)

    while not game_over:

        while game_close == True:
            screen.fill(black)
            message("Kamu kalah! Tekan Q untuk keluar atau C untuk main lagi", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill(black)
        pygame.draw.rect(screen, blue, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round((round(width / snake_block) / 2) * snake_block)
            foody = round((round(height / snake_block) / 2) * snake_block)
            Length_of_snake += 1

        clock = pygame.time.Clock()
        clock.tick(snake_speed)

    pygame.quit()

gameLoop()