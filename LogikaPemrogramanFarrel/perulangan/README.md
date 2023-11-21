#DANENDRAF#

- FOR =  untuk melakukan iterasi atau perulangan pada suatu urutan objek, seperti daftar atau list, tupel, string, atau rentang angka. ini juga bisa dipakai untuk mengulangi blok atau baris tertentu sesuai dengan urutan. dengan for kode kita akan lebih efisien dan mudah diimplementasikan. 

🔑-> 1 kondisi#

        Contoh Penulisan FOR -> 
                            for variable in class 

        -> conton ada di file for.py

#====================================================================================================================================================================================#

- FOR ELSE = syntax akan dieksekusi setelah seluruh program selesai, kecuali jika program dihentikan oleh pernyataan break. intinya buat cek semua program sudah selesai atau belum tanpa break.

🔑 -> 2 kondisi#

        contoh Penulisan FOR ELSE ->
                                for variabel in class:

                                    else: 

        -> Contoh di file forelse.py

#====================================================================================================================================================================================#

- BREAK =  menghentikan program secara paksa

🔑 -> berhenti

        -> Penulisan break -> ada di file break.py

#====================================================================================================================================================================================#

- PERULANGAN BERSARANG = ada perulangan didalam perulangan

🔑 -> For in For

        Contoh Penulisan -> 
                        for variabel in class():
                            for variable in class():

        -> Contoh di file perulanganbersarang.py

#====================================================================================================================================================================================#

 - WHILE =  suatu blok syntax dijalankan selama kondisi yang diberikan bernilai True, maka blok syntax akan terus dijalankan berulang kali selama kondisinya tetap benar. Saat kondisi menjadi salah (False), eksekusi program keluar dari blok masuk ke kondisi else

 🔑 -> benar = lanjut

        -> Penulisan break -> ada di file while.py

#====================================================================================================================================================================================#

print(range(10)) -> menampilkan range 10 nilai/bilangan pertama (0-10)

print(list(range(10))) -> menampilkan 10 nilai/bilangan pertama dengan list [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(range(2, 8))) -> menampilkan nilai/bilangan diantara 2 - 8 namun 8 tidak termasuk [2, 3, 4, 5, 6, 7]

print(list(range(0, 25, 4))) -> menampilkan kelipatan 4 dari 0 - 25 [0, 4, 8, 12, 16, 20, 24]


#====================================================================================================================================================================================#

file example1.py

Maksud dari print(I, end='') adalah menampilkan nilai i yang sudah terdapat perintah di baris sebelumnya dimana akan menampilkan output sesuai range nya dan kursor tidak akan pindah baris sebelum selesai mengeksekusi. Jadi misal 1 maka baris pertama muncul hanya ada angka 1, lalu 2 maka baris kedua muncul 2 2, baris 3 maka 3 3 3 dst sampai syntax perintah terpenuhi

#====================================================================================================================================================================================#

file listku3.py

kalo di run error karena di baris 25 kita telah menghapus semua data list namun memanggilnya lagi di baris 26. karena itu tidak ada data yang dipanggil makanya error. jika ingin bisa menghapus perintah print di baris 26 atau menambahkan syntax else

#====================================================================================================================================================================================#

file LogikaPemrograman/2/DnGanjil.py

num -> variable yg ada isinya

ketika num <= 20 maka akan program akan menampilkan nilai yang diikuti tanda (,) dan akan terus bertambah 2 sampai nilai yang ditentukan tadi (20)
#====================================================================================================================================================================================#

file LogikaPemrograman/2/DnGenap.py

bilangan -> variable
genap_list -> variable

mencari bilangan genap di dalam isi variable bilangan dengan ketentuan <=100 
%2 == 0 artinya habis dibagi 2 

.append artinya menambahkan nilai diakhir daftar


