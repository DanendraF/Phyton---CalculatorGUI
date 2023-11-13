#AKHIRNYANGODINGJUGAAYANENNDDDDD
#NIM, Tgl, Bulan
x = 23523170
y = 19
z = 5

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    if b == 0:
        return "Tidak dapat dibagi oleh nol"
    return a / b

#============================================================================================================================================#
def menu_operator():
    while True:
        print("|=======================================|")
        print("|======W E L C O M E    B R O W W W=====|")
        print("|=======================================|")
        print("| Pilih operasi:     |")
        print("| 1. Penambahan (+)  |")
        print("| 2. Pengurangan (-) |")
        print("| 3. Perkalian (x)   |")
        print("| 4. Pembagian (/)   |")
        print("| 5. Keluar          |")

        print("|=================================================================|")
        choice = input("| monggo dipilih : ")
        print("|=================================================================|")

        if choice == '5':
            print("|==============================thx y==============================|")
            print("|=========================D A N E N D R A=========================|")
            print("|========================== F A R R E L ==========================|")
            print("|===================== A D R I A N S Y A H =======================|")
            print("|=================================================================|")
            break

        if choice not in ['1', '2', '3', '4']:
            print("| Pilihan tidak valid                                          |")
            continue
        
        variable1_choice = input("| Pilih variabel pertama (x, y, z):")
        variable2_choice = input("| Pilih variabel kedua (x, y, z):")
        print("|==================================================================|")

        if variable1_choice not in ['x', 'y', 'z'] or variable2_choice not in ['x', 'y', 'z']:
            print("| Pilihan variabel tidak valid                                 |")
            continue

        if variable1_choice == 'x':
            variable1 = x
        elif variable1_choice == 'y':
            variable1 = y
        elif variable1_choice == 'z':
            variable1 = z

        if variable2_choice == 'x':
            variable2 = x
        elif variable2_choice == 'y':
            variable2 = y
        elif variable2_choice == 'z':
            variable2 = z

        if choice == '1':
            result = tambah(variable1, variable2)
            operator = "+"
        elif choice == '2':
            result = kurang(variable1, variable2)
            operator = "-"
        elif choice == '3':
            result = kali(variable1, variable2)
            operator = "x"
        elif choice == '4':
            result = bagi(variable1, variable2)
            operator = "/"

        print(f"| Hasil ({variable1_choice} {operator} {variable2_choice}): {result}                                          |")

        ulangi = input("| Apakah Anda ingin melanjutkan? (iyo/gak): ")
        if ulangi.lower() != 'iyo':
            print("")
            print("|=================================================================|")
            print("|=========================Program Selesai=========================|")
            print("|=================================================================|")
            print("|======================== D A N E N D R A ========================|")
            print("|========================== F A R R E L ==========================|")
            print("|===================== A D R I A N S Y A H =======================|")
            print("|=================================================================|")
            break

menu_operator()