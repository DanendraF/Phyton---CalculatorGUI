import pygame
import random

# Inisialisasi pygame
pygame.init()

# Ukuran layar
screen_width, screen_height = 1300, 1000

# Warna
black = (0, 0, 0)
white = (255, 255, 255)

# Membuat layar
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Balon Tembak")

# Membuat latar belakang
background = pygame.image.load("D:\\oython\\GAME\\dorr\\ORS97Z0.jpg")

# Membuat balon
balon_image = pygame.image.load("D:\\oython\\GAME\\dorr\\balloon.png")
balon_width, balon_height = 50, 50

# Membuat senjata
senjata_image = pygame.image.load("D:\\oython\\GAME\\dorr\\pointer.png")
senjata_width, senjata_height = 100, 100
senjata_x = screen_width // 2 - senjata_width // 2
senjata_y = screen_height - senjata_height

# Suara tembakan
tembakan_sound = pygame.mixer.Sound("D:\\oython\\GAME\\dorr\\dorr.mp3")

# Waktu
clock = pygame.time.Clock()

# Skor
score = 0

# Fungsi untuk menampilkan skor
def tampilkan_skor(x, y, skor):
    font = pygame.font.Font(None, 36)
    skor_text = font.render("Skor: " + str(skor), True, white)
    screen.blit(skor_text, (x, y))

# Fungsi untuk menampilkan pesan game over
def game_over():
    font = pygame.font.Font(None, 72)
    game_over_text = font.render("Game Over", True, white)
    screen.blit(game_over_text, (screen_width // 2 - 150, screen_height // 2 - 50))
    pygame.display.update()
    pygame.time.delay(2000)

# Fungsi untuk menampilkan tombol "Start"
def tampilkan_tombol_start():
    font = pygame.font.Font(None, 36)
    tombol_text = font.render("Start", True, white)
    screen.blit(tombol_text, (screen_width // 2 - 50, screen_height // 2))

# Variabel status permainan
game_started = False

# Kecepatan pergerakan senjata
senjata_speed = 10

# Kecepatan jatuh balon
balon_speed = 2

# Loop utama
running = True
balon_x = random.randint(0, screen_width - balon_width)
balon_y = -balon_height

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_started:
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if screen_width // 2 - 50 <= x <= screen_width // 2 + 50 and screen_height // 2 <= y <= screen_height // 2 + 50:
                game_started = True

    if game_started:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                tembakan_sound.play()
                if senjata_x < balon_x < senjata_x + senjata_width or senjata_x < balon_x + balon_width < senjata_x + senjata_width:
                    if senjata_y < balon_y < senjata_y + senjata_height or senjata_y < balon_y + balon_height < senjata_y + senjata_height:
                        score += 1
                        balon_x = random.randint(0, screen_width - balon_width)
                        balon_y = -balon_height

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and senjata_x > 0:
        senjata_x -= senjata_speed
    if keys[pygame.K_RIGHT] and senjata_x < screen_width - senjata_width:
        senjata_x += senjata_speed

    screen.fill(black)

    balon_y += balon_speed
    if balon_y > screen_height:
        game_over()
        score = 0
        balon_x = random.randint(0, screen_width - balon_width)
        balon_y = -balon_height

    if not game_started:
        # Tampilkan tombol "Start" jika permainan belum dimulai
        tampilkan_tombol_start()
    else:
        # Tampilkan latar belakang jika permainan sudah dimulai
        screen.blit(background, (0, 0))
        tampilkan_skor(10, 10, score)
        screen.blit(balon_image, (balon_x, balon_y))
        screen.blit(senjata_image, (senjata_x, senjata_y))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
