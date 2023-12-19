#DANENDRAF

kata_danend = "Apakah Anda masih semangat? Semangat merupakan separuh jalan menuju kesuksesan. Kesuksesan tidak ditentukan hanya oleh bakat / kemampuan. Bakat / kemampuan terkadang menjadi tidak berguna jika tidak memiliki semangat. Jadi, tetap semangat menjalani hari ini!"

kata_danend = kata_danend.replace("?", "").replace(".", "").replace("/", "")

kata = kata_danend.split()

word_count = len(kata)

hasil = [d for d in kata]

jumlah_hasil = len(hasil)

verifikasi = "Anda lolos tahap verifikasi" if jumlah_hasil <= 40 else "Anda tidak lolos tahap verifikasi"

print(hasil)
print(jumlah_hasil)
print(verifikasi)