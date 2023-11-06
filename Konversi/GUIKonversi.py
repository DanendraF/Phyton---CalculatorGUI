import tkinter as tk

def binary_to_decimal():
    decimal_number = int(binary_entry.get(), 2)
    decimal_label.config(text=str(decimal_number))

def decimal_to_binary():
    binary_number = bin(int(decimal_entry.get()))
    binary_label.config(text=str(binary_number)[2:])

root = tk.Tk()
root.title("Konversi Bilangan")

# Frame untuk bilangan biner
binary_frame = tk.Frame(root)
binary_frame.pack(padx=10, pady=10)

binary_label = tk.Label(binary_frame, text="Bilangan Biner:")
binary_label.pack(side=tk.LEFT)

binary_entry = tk.Entry(binary_frame)
binary_entry.pack(side=tk.LEFT, padx=5)

binary_button = tk.Button(binary_frame, text="Konversi ke Desimal", command=binary_to_decimal)
binary_button.pack(side=tk.LEFT, padx=5)

decimal_label = tk.Label(binary_frame, text="")
decimal_label.pack(side=tk.LEFT, padx=5)

# Frame untuk bilangan desimal
decimal_frame = tk.Frame(root)
decimal_frame.pack(padx=10, pady=10)

decimal_label = tk.Label(decimal_frame, text="Bilangan Desimal:")
decimal_label.pack(side=tk.LEFT)

decimal_entry = tk.Entry(decimal_frame)
decimal_entry.pack(side=tk.LEFT, padx=5)

decimal_button = tk.Button(decimal_frame, text="Konversi ke Biner", command=decimal_to_binary)
decimal_button.pack(side=tk.LEFT, padx=5)

binary_label = tk.Label(decimal_frame, text="")
binary_label.pack(side=tk.LEFT, padx=5)

root.mainloop()