print("\nKONVERTER SATUAN SUHU\n")

### RUMUS ###

print("=====Konversi Celcius=====")

celcius = float(input("Masukkan nilai Celcius : "))
fahrenheit = (9 / 5) * celcius + 32
reamur = (4 / 5) * celcius
kelvin = celcius + 273

# KONVERSI CELCIUS
print("Nilai Celcius : ", celcius, "C")
print("Nilai dalam fahrenheit :", fahrenheit, "F")
print("Nilai dalam reamur :", reamur, "R")
print("Nilai dalam Kelvin :", kelvin, "K")

################################################################

print("\n=====Konversi Fahrenheit=====")

fahrenheit = float(input("Masukkan nilai Fahrenheit : "))
celcius = (5 / 9) * (fahrenheit - 32)
reamur = (4 / 9) * (fahrenheit - 32)
kelvin = (5 / 9) * (fahrenheit - 32) + 273
# KONVERSI FAHRENHEIT
print("Nilai Fahrenheit : ", fahrenheit, "F")
print("Nilai dalam Celcius :", celcius, "C")
print("Nilai dalam reamur :", reamur, "R")
print("Nilai dalam Kelvin :", kelvin, "K")

################################################################

print("\n=====Konversi Reamur=====")

reamur = float(input("Masukkan nilai Reamur : "))
celcius = (5 / 4) * reamur
fahrenheit = (9 / 4) * reamur + 32
kelvin = (5 / 4) * reamur + 273
# KONVERSI REAMUR
print("Nilai reamur :", reamur, "R")
print("Nilai Celcius : ", celcius, "C")
print("Nilai dalam fahrenheit :", fahrenheit, "F")
print("Nilai dalam Kelvin :", kelvin, "K")

################################################################

print("\n=====Konversi Kelvin=====")

kelvin = float(input("Masukkan nilai Kelvin : "))
celcius = kelvin - 273
fahrenheit = (9 / 5) * (kelvin - 273) + 32
reamur = (4 / 5) * (kelvin - 273)
# KONVERSI KELVIN
print("Nilai reamur :", reamur, "R")
print("Nilai Celcius : ", celcius, "C")
print("Nilai dalam fahrenheit :", fahrenheit, "F")
print("Nilai dalam Kelvin :", kelvin, "K")