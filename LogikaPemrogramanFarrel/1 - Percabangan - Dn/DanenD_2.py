#AKHIRNYANGODINGJUGAAYANENNDDDDD
#NIM, Tgl, Bulan
x = 23523170
y = 19
z = 05

#============================================================================================================================================#
def menu_operator():
    while True:
        print("|===============================================|")
        print("|==========W E L C O M E    B R O W W W=========|")
        print("|===============================================|")
        print("| Pilih operasi:                                |")
        print("| 1. Operator Logika (and, or, not)             |")
        print("| 2. Operator Pembanding (==, !=, <, <=, >, >=) |")
        print("| 3. Keluar                                     |")

        print("|===============================================|")
        choice = input("| Yang Mana : ")
        print("|===============================================|")

        if choice == '3':
            print("|================Program selesai.================|")
            break

        if choice not in ['1', '2']:
            print("Pilihan tidak valid")
            continue

        if choice == '1':
            operator = input("Pilih operator logika (and, or, not): ")
            if operator not in ['and', 'or', 'not']:
                print("Operator logika tidak valid")
                continue
            operand1 = input("Masukkan operand pertama (True atau False): ")
            operand2 = input("Masukkan operand kedua (jika diperlukan, True atau False): ")
            if operator == 'not':
                result = not (operand1 == 'True')
            else:
                if operand2:
                    result = (operand1 == 'True') and (operand2 == 'True') if operator == 'and' else (operand1 == 'True') or (operand2 == 'True')
                else:
                    print("Operand kedua diperlukan untuk operator and dan or.")
                    continue
        elif choice == '2':
            operator = input("Pilih operator pembanding (==, !=, <, <=, >, >=): ")
            if operator not in ['==', '!=', '<', '<=', '>', '>=']:
                print("Operator pembanding tidak valid")
                continue
            operand1 = float(input("Masukkan operand pertama: "))
            operand2 = float(input("Masukkan operand kedua: "))
            if operator == '==':
                result = operand1 == operand2
            elif operator == '!=':
                result = operand1 != operand2
            elif operator == '<':
                result = operand1 < operand2
            elif operator == '<=':
                result = operand1 <= operand2
            elif operator == '>':
                result = operand1 > operand2
            else:
                result = operand1 >= operand2

        print(f"Hasil operasi: {result}")

        ulangi = input("Apakah Anda ingin melanjutkan? (ya/tidak): ")
        if ulangi.lower() != 'ya':
            print("Program selesai.")
            break

menu_operator()

