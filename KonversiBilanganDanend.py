from os import replace, system

def judul():
    system('cls')
    print('=====================================')
    print('Program Konversi Bilangan'.center(40))
    print('=====================================')

def menu():
    judul()
    print('| 1. Desimal                        |')
    print('| 2. Biner                          |')
    print('| 3. Oktal                          |')
    print('| 4. Hexadecimal                    |')
    print('| 5. keluar                         |')
    print('=====================================')
    pilih2 = input('Pilih Menu : ')
    if pilih2 == '1':
        desimal()
    elif pilih2 == '2':
        biner()
    elif pilih2 == '3':
        oktal()
    elif pilih2 == '4':
        hexadecimal()
    elif pilih2 == '5':
        keluar()
    else:
        salah()
def salah():
    salah1 = input("Menu Tidak Ada ! [Enter]")
    menu()

def desimal():
    judul()
    try:
        angka = int(input("Masukkan Bilangan Desimal : "))
    except ValueError:
        error = input ("Bilangan Tidak Sesuai! ulangi [Enter]")
        desimal()
    bineri = bin(angka).replace("0b","")
    oktal = oct(angka).replace("0o","")
    heks = hex(angka).replace("0x","")
    
    print('=====================================')
    print('| Biner : ',bineri)
    print('| Oktal : ',oktal)
    print('| Hexa  : ',heks)
    print('=====================================')
    kembali = input('Ulangi Konversi? [y/t]')
    if kembali == "y" or kembali == "Y":
        desimal()
    else:
        menu()

def biner():
    judul()
    try:
        angka = int(input("Masukkan Bilangan Biner : "),2)
    except ValueError:
        error = input ("Bilangan Tidak Sesuai! ulangi[Enter]")
        biner()
    oktal = oct(angka).replace("0o","")
    heks = hex(angka).replace("0x","")

    print('=====================================')
    print('| Decimal : ',angka)
    print('| Oktal   : ',oktal)
    print('| Hexa    : ',heks)
    print('=====================================')
    kembali = input('Ulangi Konversi? [y/t]')
    if kembali == "y" or kembali == "Y":
        biner()
    else:
        menu()

def oktal():
    judul()
    try:
        angka = int(input("Masukkan Bilangan Oktal : "),8)
    except ValueError:
        error = input ("Bilangan Tidak Sesuai! ulangi[Enter]")
        oktal()
    biner = bin(angka).replace("0b","")
    heks = hex(angka).replace("0x","")

    print('=====================================')
    print('| Decimal : ',angka)
    print('| biner   : ',biner)
    print('| Hexa    : ',heks)
    print('=====================================')
    kembali = input('Ulangi Konversi? [y/t]')
    if kembali == "y" or kembali == "Y":
        oktal()
    else:
        menu()

def hexadecimal():
    judul()
    try:
        angka = int(input("Masukkan Bilangan Hexa : "),16)
    except ValueError:
        error = input ("Bilangan Tidak Sesuai! ulangi[Enter]")
        hexadecimal()
    biner = bin(angka).replace("0b","")
    oktal = oct(angka).replace("0o","")
    
    print('=====================================')
    print('| Decimal : ',angka)
    print('| Biner   : ',biner)
    print('| Oktal   : ',oktal)
    print('=====================================')

    kembali = input('Ulangi Konversi? [y/t]')
    if kembali == "y" or kembali == "Y":
        hexadecimal()
    else:
        menu()

def keluar():
    exit()
menu()

