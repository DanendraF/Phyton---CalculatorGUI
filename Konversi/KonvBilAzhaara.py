import Module.Stack as st
stack = st.stack()

print("Pilihan Menu:\n1. Decimal to Biner\n2. Decimal to Octal\n3. Decimal to Hexa\n4. Biner to Decimal\n5. Octal to Decimal\n6. Hexa to Decimal")
pilihan = int(input("Masukkan Kode Pilihan: "))

if pilihan == 1:
    decimal = int(input("Masukkan Bilangan Decimal: "))
    while decimal != 0:
        hasil = decimal % 2
        st.push(stack, hasil)
        decimal = decimal // 2
    for i in range(len(stack)):
        print(st.pop(stack), end="")
elif pilihan == 2:
    octal = int(input("Masukkan Bilangan Decimal: "))
    while octal > 0:
        hasil = octal % 8
        st.push(stack, hasil)
        octal = octal // 8
    for i in range(st.size(stack)):
        print(st.pop(stack), end="")
elif pilihan == 3:
    hexa = int(input("Masukkan Bilangan Decimal: "))
    while hexa > 0:
        hasil = hexa % 16
        if hasil == 10:
            hasil = "A"
        elif hasil == 11:
            hasil = "B"
        elif hasil == 12:
            hasil = "C"
        elif hasil == 13:
            hasil = "D"
        elif hasil == 14:
            hasil = "E"
        elif hasil == 15:
            hasil = "F"
        st.push(stack, hasil)
        hexa = hexa // 16
    for i in range(st.size(stack)):
        print(st.pop(stack), end="")
elif pilihan == 4:
    biner = input("Masukkan Bilangan Biner: ")
    lenBiner = int(len(biner))
    result = 0
    for j in biner:
        lenBiner = lenBiner-1
        hasil = int(j)*(2**(lenBiner))
        st.push(stack, hasil)
    for i in range(st.size(stack)):
        result = result + st.peek(stack)
        print(st.pop(stack), end=" ")
    print(" = ", result)
elif pilihan == 5:
    octal = input("Masukkan Bilangan Octal: ")
    lenOctal = len(octal)
    result = 0
    for i in octal:
        lenOctal = lenOctal-1
        hasil = int(i)*(8**(lenOctal))
        st.push(stack, hasil)
    for j in range(st.size(stack)):
        result = result + st.peek(stack)
        print(st.pop(stack), end=" ")
    print("=", result)
elif pilihan == 6:
    hexa = input("Masukkan Bilangan Hexa: ").upper()
    lenHexa = len(hexa)
    result = 0
    for i in hexa:
        if i == "A":
            i = 10
        elif i == "B":
            i = 11
        elif i == "D":
            i = 12
        elif i == "D":
            i = 13
        elif i == "E":
            i = 14
        elif i == "F":
            i = 15
        lenHexa = lenHexa-1
        hasil = int(i)*(16**(lenHexa))
        st.push(stack, hasil)
    for j in range(st.size(stack)):
        result = result + st.peek(stack)
        print(st.pop(stack), end=" ")
    print("=", result)