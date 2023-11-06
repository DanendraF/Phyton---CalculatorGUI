import tkinter as tk
from tkinter import ttk

def total(liter, harga_per_liter):
    total_harga = liter * harga_per_liter
    return total_harga

def hitung_total():
    # Menonaktifkan input dan button
    liter_entry.config(state=tk.DISABLED)
    hitung_button.config(state=tk.DISABLED)

    pilihan = pilihan_var.get()
    liter_bbm_str = liter_entry.get()
    
    try:
        liter_bbm = float(liter_bbm_str)
        
        if liter_bbm <= 0:
            hasil_label.config(text="Jumlah liter harus lebih dari 0.", fg="red")
        else:
            if pilihan == 1:
                jenis_bbm = "Pertamax"
                harga_per_liter = harga_pertamax
            else:
                jenis_bbm = "Pertalite"
                harga_per_liter = harga_pertalite

            total_harga = 0.0

            liter_label.config(text=f"Jumlah liter: 0.0")
            liter_label.pack()  # Menampilkan label liter

            hasil_label.config(text=f"Silahkan Membayar {jenis_bbm} (0.0 liter) Sebanyak : Rp 0.00")

            liter_entry.focus_set()  # Menghilangkan kursor 

            def update_harga(liter, total_harga):
                if liter < liter_bbm:
                    total_harga += harga_per_liter * 0.1
                    liter += 0.1
                    liter_label.config(text=f"Jumlah : {liter:.1f}")
                    hasil_label.config(text=f"Silahkan Membayar {jenis_bbm} ({liter:.1f} liter) Sebanyak : Rp {total_harga:.2f}")
                    root.after(500, update_harga, liter, total_harga)  # Mengatur waktu pengulangan (500ms)
                else:
                    ulangi_button.pack()
                    hitung_button.pack_forget()

            update_harga(0.0, total_harga)

    except ValueError:
        hasil_label.config(text="Masukkan harus berupa angka.", fg="red")

def ulangi_pengisian():

    # Input Nyala Lagi
    liter_entry.config(state=tk.NORMAL)
    hitung_button.config(state=tk.NORMAL)
    pilihan_var.set(1)
    liter_entry.delete(0, "end")
    hasil_label.config(text="", fg="black")
    ulangi_button.pack_forget()
    hitung_button.pack()


#--------------------------------------------------------
#-------------------------GUI----------------------------
#--------------------------------------------------------
root = tk.Tk()
root.title("PROGRAM BBM DANEND")
root.geometry("500x320")
root.resizable(False, False)

harga_pertamax = 13500
harga_pertalite = 10000

pilihan_var = tk.IntVar()
pilihan_var.set(1)

frame = tk.Frame(root, bg="coral")
frame.pack(padx=10, pady=10)

judul_label = tk.Label(frame, text="Selamat Datang di PROGRAM BBM DANEND", bg="coral", font=("Math Sans", 14))
judul_label.pack()

tk.Radiobutton(frame, text="Pertamax", variable=pilihan_var, value=1, bg="coral", font=("Math Sans", 14)).pack(anchor="w")
tk.Radiobutton(frame, text="Pertalite", variable=pilihan_var, value=2, bg="coral", font=("Math Sans", 14)).pack(anchor="w")

liter_label = tk.Label(frame, text="Masukkan jumlah liter BBM yang ingin diisi:", bg="coral")
liter_label.pack()

liter_entry = tk.Entry(frame, font=("Math Sans", 12), justify="center")
liter_entry.pack(pady=5)

hitung_button = tk.Button(frame, text="Hitung Total Harga", command=hitung_total, bg="green", fg="white", font=("Math Sans", 14))
hitung_button.pack(pady=8)

hasil_label = tk.Label(frame, text="", bg="coral")
hasil_label.pack()

judul_label = tk.Label(frame, text="😃😃😃", bg="coral", font=("Math Sans", 14))
judul_label.pack(pady=2)

ulangi_button = tk.Button(frame, text="Ulangi Pengisian", command=ulangi_pengisian, bg="blue", fg="white", font=("Math Sans", 14))

root.mainloop()
