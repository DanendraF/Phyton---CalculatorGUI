#DANENDRAF

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
