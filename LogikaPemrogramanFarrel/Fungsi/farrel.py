import math

print("DanendraF")
def hitung_fungsi(x, pilihan_operasi):
    if pilihan_operasi == 1:
        return x ** 2
    elif pilihan_operasi == 2:
        return 2 * x + 1
    elif pilihan_operasi == 3:
        return math.sqrt(x)
    else:
        return "Pilihan operasi tidak valid"
    
print("|| 1. x^2     ||")
print("|| 2. 2x+1    ||")
print("|| 3. akar(x) ||")

x = float(input("Masukkan nilai x: "))
pilihan = int(input("Masukkan pilihan operasi (1/2/3): "))


hasil = hitung_fungsi(x, pilihan)
print("Hasil perhitungan f(x):", hasil)
