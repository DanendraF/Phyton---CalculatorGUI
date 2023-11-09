import pygame
import time

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Lirik Lagu")

# Mengatur font untuk lirik
font = pygame.font.Font(None, 36)

# Daftar lirik dan durasi masing-masing baris lirik (per detik)
lyrics = [
    ("Karena bersamamu semua terasa indah", 7),
    ("Gundah gulana hatiku telah hancur sirna", 4.5),
    ("Janjiku takkan kulepas wahai kau bidadariku dari surga", 3),
    ("Tuk selamanya", 7),
]

# Memainkan lagu (ganti dengan path lagu yang sesuai)
pygame.mixer.music.load("D:\\UII\\SSTTT\\Pycharm\\♥️♥️\\NADHIF.wav")
pygame.mixer.music.play()

# Mengatur waktu mulai
start_time = time.time()
lyric_index = 0  # Indeks lirik saat ini
initial_lyric_duration = 3  # Durasi tampilan awal (detik)
fade_duration = 6  # Durasi efek pemudaran (detik)

# Warna teks
text_color = (255, 255, 255)

# Loop utama
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Mengambil waktu saat ini
    current_time = time.time()

    # Menghitung berapa lama lagu telah dimainkan
    elapsed_time = current_time - start_time

    # Menampilkan lirik yang sesuai dengan waktu
    if lyric_index < len(lyrics):
        current_lyric, lyric_duration = lyrics[lyric_index]

        if elapsed_time >= initial_lyric_duration:
            # Efek pemudaran saat lirik berganti
            fade_out_duration = min(fade_duration, elapsed_time - initial_lyric_duration - lyric_index)
            fade_out_alpha = int((1 - (fade_out_duration / fade_duration)) * 255)
            text = font.render(current_lyric, True, text_color)
            text.set_alpha(fade_out_alpha)
            screen.fill((0, 0, 0))  # Hapus lirik sebelumnya
            screen.blit(text, (100, 200))

            if fade_out_duration >= fade_duration:
                lyric_index += 1
                initial_lyric_duration = elapsed_time  # Setel waktu tampilan lirik selanjutnya
                fade_duration = lyric_duration  # Atur durasi pemudaran sesuai durasi lirik

    else:
        # Jika semua lirik sudah ditampilkan, hentikan pemutaran
        running = False

    pygame.display.update()

# Menghentikan pemutaran lagu
pygame.mixer.music.stop()

# Menutup pygame
pygame.quit()
