#===============================#
#DANENDRAF - Nilai
#===============================#

ujian = int(input("Masukan Nilai Ujian : "))
tugas = int(input("Masukan Nilai Tugas : "))
hadir = int(input("Masukan Kehadiran : "))

if hadir > 11:
    if ujian >= 80:
        nilai = 'A'
    elif ujian >= 60:
        nilai = 'B'
    elif tugas >= 80:
        nilai = 'B'
    elif tugas < 60:
        nilai = 'C'
    else:
        nilai = 'D' 
    print("Lulus")
else:
    nilai = 'D'
    print("Tidak Lulus")
    


#===============================#
#DANENDRAF - Calculator
#===============================#

def kalkulator(x, y, opr):
    sementara = 0
    if opr == '+':
        sementara = x + y
    elif opr == '-':
        sementara = x - y
    elif opr == '*':
        sementara = x * y
    elif opr == '/':
        sementara = x / y
    return sementara

hasil = kalkulator(15, 20, '+')
hasil = kalkulator(0, 15, '-')
hasil = kalkulator(7, 5, '*')
hasil = kalkulator(200, 40, '/')
hasil = kalkulator(4, 5, 'x')
Ngitung = hasil
    


#===============================#
#DANENDRAF - DaftarHadir
#===============================#

siswa = [['Sinta','Tidak Lulus'], ['Santi','Lulus'], ['Joko','Lulus'], ['Joni','Mundur'], ['Budi','Lulus']]

siswa.sort()

for i in siswa:
    if i[1] == 'Lulus':
        print(i)
        


#===============================#
#DANENDRAF - KataBijak
#===============================#

kata_bijak = '/Kesuksesan bukanlah kunci kebahagiaan, /Namun kebahagiaanlah kunci kesuksesan.'
tanda_baca = ["," , "." , "/"]

def hapus_tandabaca(word):
    temp = ""
    for w in word:
        hapus = False
        i = 0
        while (i<len(tanda_baca) and (not hapus)):
            if(w==tanda_baca[i]):
                hapus = True
            else :
                i = i + 1
        if not hapus:
            temp = temp + w
    return temp

tanpa_tandabaca = hapus_tandabaca(kata_bijak)

l = tanpa_tandabaca.split()
jumlah = len(l)

print(kata_bijak)
print(tanpa_tandabaca)
print(l)
print(jumlah)


#===============================#
#DANENDRAF - kata_bijak_danend
#===============================#

kata_danend = "Apakah Anda masih semangat? Semangat merupakan separuh jalan menuju kesuksesan. Kesuksesan tidak ditentukan hanya oleh bakat / kemampuan. Bakat / kemampuan terkadang menjadi tidak berguna jika tidak memiliki semangat. Jadi, tetap semangat menjalani hari ini!"

kata_danend = kata_danend.replace("?", "").replace(".", "").replace("/", "")

kata = kata_danend.split()

word_count = len(kata)

hasil = [d for d in kata]

jumlah_hasil = len(hasil)

verifikasi = "Anda lolos tahap verifikasi" if jumlah_hasil <= 40 else "Anda tidak lolos tahap verifikasi"

print(hasil)
print(jumlah_hasil)
print(verifikasi)

