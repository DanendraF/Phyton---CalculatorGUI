#DanendraF #11/20/2023

#perulangan for setiap elemen
buah = ["Apple","orange","Avocado", "Grape"]
for x in buah:
    print (x)
    
# perulangan dalam string
for x in "Avocado":
    print(x)

# Jumlah angka dalam List
numbers = [7, 2, 17, 37, 73, 9, 23, 57]

# sum seperti kantong sumbangan yang kosong 
sum = 0

# sum seperti isi kantong 
# akan terus bertambah
for val in numbers: 
    sum = sum + val
    print (sum)
    
# Perulangan dalam Interval Nilai
for x in range(17):
    print(x)
    
for x in range (17, 73, 37):
    print (x)
    
for x in range(5,1,-1):
    print(x)