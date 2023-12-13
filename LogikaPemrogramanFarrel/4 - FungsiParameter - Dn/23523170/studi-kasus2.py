#DANENDRAF

# sisi kubus
sisi_1 = 4
sisi_2 = 5
sisi_3 = 7

# menghitung luas kubus
# rumus menghitung volume kubus yaitu 6 x luas sisi kubus
luas_1 = 6*(4*4)
luas_2 = 6*(5*5)
luas_3 = 6*(7*7)

# menghitung volume kubus
# rumus menghitung volume kubus yaitu sisi x sisi x sisi
volume_1 = 4*4*4
volume_2 = 5*5*5
volume_3 = 7*7*7
    
print("Luas kubus dengan sisi ", sisi_1, "yaitu : ", luas_1)
print("Luas kubus dengan sisi ", sisi_2, "yaitu : ", luas_2)
print("Luas kubus dengan sisi ", sisi_3, "yaitu : ", luas_3)

print("")

print("Volume kubus dengan sisi ", sisi_1, "yaitu : ", volume_1)
print("Volume kubus dengan sisi ", sisi_2, "yaitu : ", volume_2)
print("Volume kubus dengan sisi ", sisi_3, "yaitu : ", volume_3)



def luas(x) :
    hitung = 6*x**2
    return hitung