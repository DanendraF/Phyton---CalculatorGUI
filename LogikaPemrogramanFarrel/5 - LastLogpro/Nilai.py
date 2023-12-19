#DANENDRAF

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

