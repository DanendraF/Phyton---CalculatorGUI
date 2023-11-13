import pygame
import time

# Inisialisasi pygame
pygame.init()

# Inisialisasi layar
screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Lirik Lagu")

# Mengatur font untuk lirik
font = pygame.font.Font(None, 36)

# Membuat daftar lirik lagu
lyrics = [
    "Karena bersamamu semua terasa indah",
    "Gundah gulana hatiku telah hancur sirna",
    "Janjiku takkan kulepas wahai kau bidadariku dari surga",
    "Tuk selamanya",
]

# Memainkan lagu (ganti dengan path lagu yang sesuai)
pygame.mixer.music.load("D:\\oython\\LopeSong♥️\\NADHIF.mp3")
pygame.mixer.music.play()

# Mengatur waktu mulai
start_time = time.time()

# Loop utama
running = True
line_index = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mengambil waktu saat ini
    current_time = time.time()

    # Menghitung berapa lama lagu telah dimainkan
    elapsed_time = current_time - start_time

    # Menampilkan lirik yang sesuai dengan waktu
    while line_index < len(lyrics) and elapsed_time >= line_index * 5:
        line = lyrics[line_index]
        text = font.render(line, True, (255, 255, 255))
        screen.blit(text, (50, 100))
        line_index += 1

    pygame.display.update()

# Menghentikan pemutaran lagu
pygame.mixer.music.stop()

# Menutup pygame
pygame.quit()
