# IsKabisat : integer --> boolean
#   IsKabisat(D) true jika tahun D adalah tahun kabisat:
#   habis dibagi 4 tetapi tidak habis dibagi 100, atau habis dibagi 400

def IsKabisat(D):
    if (((D)%4 == 0) or ((D)%400 == 0)) and ((D)%100!=0) :
        return True
    else :
        return False

tahun = int(input("Masukkan tahun: "))

if IsKabisat(tahun):
    print("true")
else:
    print("false")
    
