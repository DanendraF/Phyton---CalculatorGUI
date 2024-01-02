def f(X):
    return X ** 2

def hitung_nilai_maksimal(K, N, M):
    nilai_maksimal = 0
    for i in range(N):
        daftar = K[i]
        for elemen in daftar:
            nilai_f = f(elemen)
            hasil = (nilai_maksimal + nilai_f) % M
            if hasil > nilai_maksimal:
                nilai_maksimal = hasil
    return nilai_maksimal

# Contoh penggunaan
K = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
N = len(K)
M = 10

nilai_maksimal = hitung_nilai_maksimal(K, N, M)
print("Nilai maksimal S:", nilai_maksimal)