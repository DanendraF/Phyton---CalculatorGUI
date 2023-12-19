#DANENDRAF

siswa = [['Sinta','Tidak Lulus'], ['Santi','Lulus'], ['Joko','Lulus'], ['Joni','Mundur'], ['Budi','Lulus']]

siswa.sort()

for i in siswa:
    if i[1] == 'Lulus':
        print(i)