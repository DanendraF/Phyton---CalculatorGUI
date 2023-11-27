#DANENDRAF

#SOAL
Angka = [
    95, 40, 98, 65, 36, 69, 40, 31, 65, 48, 91, 50, 73, 54, 59,
    39, 16, 75, 21, 91, 23, 41, 56, 82, 24, 86, 95, 62, 94, 68, 21
]

Pertama = 2
sum = 0
nGanjil = 0

for i in Angka:
    if nGanjil == Pertama:
        break
    elif i%2 == 1:
        nGanjil = nGanjil + 1
        if nGanjil < Pertama:
            sum = sum + i

print("Jumlah ",Pertama," bilangan Ganjil yang pertama dalam daftar",sum)


#DANENDRAF

#Perbaikan
Angka = [
    95, 40, 98, 65, 36, 69, 40, 31, 65, 48, 91, 50, 73, 54, 59,
    39, 16, 75, 21, 91, 23, 41, 56, 82, 24, 86, 95, 62, 94, 68, 21
]

Pertama = 2
sum = 0
nGanjil = 0

for i in Angka:
    if i % 2 == 1:
        nGanjil = nGanjil + 1
        sum = sum + i
    elif nGanjil == Pertama:
        break

print("Jumlah", Pertama, "bilangan Ganjil yang pertama dalam daftar:", sum)
