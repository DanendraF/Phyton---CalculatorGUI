def jarak_malang(x1, y1, x2, y2):
    jarak_absis = abs(x1 - x2)
    jarak_ordinat = abs(y1 - y2)
    jarak_malang = jarak_absis + jarak_ordinat
    return jarak_malang

# Contoh penggunaan
x1 = int(input("Masukkan koordinat x1: "))
y1 = int(input("Masukkan koordinat y1: "))
x2 = int(input("Masukkan koordinat x2: "))
y2 = int(input("Masukkan koordinat y2: "))


jarak = jarak_malang(x1, y1, x2, y2)
print("Jarak Malang yang harus ditempuh:", jarak)