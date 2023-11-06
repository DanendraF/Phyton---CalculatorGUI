from tkinter import *
exp=''
def press(number):
    global exp
    exp+=str(number)
    equation.set(exp)

def equalpress():
    try:
        global exp
        total = str(eval(exp))
        equation.set(total)
        expression = ""
    except :
        equation.set("Syntax Tidak Terbaca")
        exp= ""

def clear():
    global exp
    exp=''
    equation.set('')

tk=Tk()
tk.configure(background="grey")
tk.title('MENUNGGU UTS PAI')
tk.geometry('280x280')

equation=StringVar()
Text_Entry_Box=Entry(tk, textvariable=equation,width=20)
Text_Entry_Box.grid(columnspan=8, ipadx=100)

button1 = Button(tk, text= '1', fg="black", bg='#8f8f8f',
                 command=lambda: press(1), height=2, width=7)
button1.grid(row=2, column=0)

button2 = Button(tk, text= '2', fg="black", bg='#8f8f8f',
                 command=lambda: press(2), height=2, width=7)
button2.grid(row=2, column=1)

button3 = Button(tk, text= '3', fg="black", bg='#8f8f8f',
                 command=lambda: press(3), height=2, width=7)
button3.grid(row=2, column=2)

button4 = Button(tk, text= '4', fg="black", bg='#8f8f8f',
                 command=lambda: press(4), height=2, width=7)
button4.grid(row=3, column=0)

button5 = Button(tk, text= '5', fg="black", bg='#8f8f8f',
                 command=lambda: press(5), height=2, width=7)
button5.grid(row=3, column=1)

button6 = Button(tk, text= '6', fg="black", bg='#8f8f8f',
                 command=lambda: press(6), height=2, width=7)
button6.grid(row=3, column=2)

button6 = Button(tk, text= '7', fg="black", bg='#8f8f8f',
                 command=lambda: press(7), height=2, width=7)
button6.grid(row=4, column=0)

button6 = Button(tk, text= '8', fg="black", bg='#8f8f8f',
                 command=lambda: press(8), height=2, width=7)
button6.grid(row=4, column=1)

button6 = Button(tk, text= '9', fg="black", bg='#8f8f8f',
                 command=lambda: press(9), height=2, width=7)
button6.grid(row=4, column=2)

tk.mainloop()

