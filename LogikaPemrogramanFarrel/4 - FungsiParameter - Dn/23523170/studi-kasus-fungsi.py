#DANENDRAF

def luas(x) :
    hitung = 6*x**2
    return hitung

def volume(x):
    hitung = x*x*x
    return hitung

sisi_1 = 4
sisi_2 = 5
sisi_3 = 7

luas_1 = luas(sisi_1)
luas_2 = luas(sisi_2)
luas_3 = luas(sisi_3)

volume_1 = volume(sisi_1)
volume_2 = volume(sisi_2)
volume_3 = volume(sisi_3)

print("Luas kubus dengan sisi", sisi_1, "adalah:", luas_1)
print("Luas kubus dengan sisi", sisi_2, "adalah:", luas_2)
print("Luas kubus dengan sisi", sisi_3, "adalah:", luas_3)

print()

print("Volume kubus dengan sisi", sisi_1, "adalah:", volume_1)
print("Volume kubus dengan sisi", sisi_2, "adalah:", volume_2)
print("Volume kubus dengan sisi", sisi_3, "adalah:", volume_3)




