print("=====================================")
print("Selamat Datang di PROGRAM BBM DANEND")
print("=====================================")

def total(liter, harga_per_liter):
    total_harga = liter * harga_per_liter
    return total_harga

# Harga per liter BBM
harga_pertamax = 13500
harga_pertalite = 10000  

while True:
    print("")
    print("-----------------------------------------")
    print("Silahkan pilih jenis BBM yang diinginkan:")
    print("-----------------------------------------")
    print("1. Pertamax")
    print("2. Pertalite")
    print("")

    pilihan_valid = False

    while not pilihan_valid:
        # Meminta pengguna memilih jenis BBM
        pilihan = int(input("Pilih jenis BBM (1/2): "))

        if pilihan in [1, 2]:
            pilihan_valid = True
        else:
            print("")
            print("---------------------------------------------------------------------")
            print("Pilihan tidak tersedia silahkan pilih 1 (Pertamax) atau 2 (Pertalite)")
            print("---------------------------------------------------------------------")
            print("")

    liter_bbm = float(input("Masukkan jumlah liter BBM yang ingin diisi: "))

    if liter_bbm <= 0:
        print("Jumlah liter harus lebih dari 0.")
    else:
        if pilihan == 1:
            total_harga = total(liter_bbm, harga_pertamax)
            jenis_bbm = "Pertamax"
        else:
            total_harga = total(liter_bbm, harga_pertalite)
            jenis_bbm = "Pertalite"

        print(f"Total harga pengisian {jenis_bbm} ({liter_bbm} liter) adalah: Rp {total_harga:.2f}")
        print("")

    ulangi = input("Apakah Anda ingin mengisi BBM lagi? (y/n): ")
    if ulangi.lower() != "y":
        ulangi_program = False

    print("")
    print("😃Terimaksih yowww😃")
    print("")
    break
