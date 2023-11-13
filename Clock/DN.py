import tkinter as tk
from time import strftime

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

root = tk.Tk()
root.title("Jam Digital")

lbl = tk.Label(root, font=('calibri', 40, 'bold'), background='#000000', foreground='white')
lbl.pack(anchor='center')

time()
root.mainloop()
