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
        equation.set("error")
        exp= ""
        
def clear():
    global exp
    exp = ''
    equation.set('')
    
tk=Tk()
tk.configure(background="grey")
tk.title('DANENDCALCULATE')
tk.geometry('315x280')

#=======================================#

equation=StringVar()
Text_Entry_Box = Entry(tk, textvariable=equation,width=20)
Text_Entry_Box.grid(columnspan=8, ipadx=100)

Button1= Button(tk, text='1', fg='black', bg='#8f8f8f', 
                command=lambda: press(1), height=2,width=7)
Button1.grid(row=2, column=0)

Button2= Button(tk, text='2', fg='black', bg='#8f8f8f', 
                command=lambda: press(2), height=2,width=7)
Button2.grid(row=2, column=1)

Button3= Button(tk, text='3', fg='black', bg='#8f8f8f', 
                command=lambda: press(3), height=2,width=7)
Button3.grid(row=2, column=2)

Button4= Button(tk, text='4', fg='black', bg='#8f8f8f', 
                command=lambda: press(4), height=2,width=7)
Button4.grid(row=3, column=0)

Button5= Button(tk, text='5', fg='black', bg='#8f8f8f', 
                command=lambda: press(5), height=2,width=7)
Button5.grid(row=3, column=1)

Button6= Button(tk, text='6', fg='black', bg='#8f8f8f', 
                command=lambda: press(6), height=2,width=7)
Button6.grid(row=3, column=2)

Button7= Button(tk, text='7', fg='black', bg='#8f8f8f', 
                command=lambda: press(7), height=2,width=7)
Button7.grid(row=4, column=0)

Button8= Button(tk, text='8', fg='black', bg='#8f8f8f', 
                command=lambda: press(8), height=2,width=7)
Button8.grid(row=4, column=1)

Button9= Button(tk, text='9', fg='black', bg='#8f8f8f', 
                command=lambda: press(9), height=2,width=7)
Button9.grid(row=4, column=2)

Button0= Button(tk, text='0', fg='black', bg='#8f8f8f', 
                command=lambda: press(0), height=2,width=7)
Button0.grid(row=5, column=0)

plus= Button(tk, text='+', fg='black', bg='#8f8f8f', 
                command=lambda: press("+"), height=2,width=7)
plus.grid(row=2, column=3)

minus= Button(tk, text='-', fg='black', bg='#8f8f8f', 
                command=lambda: press("-"), height=2,width=7)
minus.grid(row=3, column=3)

divide= Button(tk, text='÷', fg='black', bg='#8f8f8f', 
                command=lambda: press("÷"), height=2,width=7)
divide.grid(row=4, column=3)

kali= Button(tk, text='x', fg='black', bg='#8f8f8f', 
                command=lambda: press("x"), height=2,width=7)
kali.grid(row=5, column=3)

equal= Button(tk, text='=', fg='black', bg='#8f8f8f', 
                command=equalpress, height=2,width=7)
equal.grid(row=5, column=2)

clear= Button(tk, text='clear', fg='black', bg='#8f8f8f', 
                command=clear, height=2,width=7)
clear.grid(row=5, column=1)

tk.mainloop()