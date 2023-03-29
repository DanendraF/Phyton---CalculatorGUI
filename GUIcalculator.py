from tkinter import *

window = Tk()
screenSize = "298x510"
window.geometry(screenSize)
window.resizable(0, 0)
window.title("CalculatorDn")

def clickButton(item):
    global expression
    inputText.set(inputText.get()+(str(item)))

def clearButton():
    global expression
    expression = ""
    inputText.set(inputText.get()[0:-1])

def clearAll():
    inputText.set("")

def equalButton():
    result = ""
    try:
        result = eval(inputText.get())
        inputText.set(result)
    except:
        result = "error"
        inputText.set(result)

expression = ""
inputText = StringVar()

inputFrame = Frame(window, width=312, height=50, bd=0, highlightbackground="gray", highlightcolor="gray", highlightthickness=2, bg="white")
inputFrame.pack(side=TOP)
inputField = Entry(inputFrame, font=('arial', 25, ), textvariable=inputText, width=50,fg="white", bg="black", bd=0, justify=CENTER)
inputField.grid(row=0, column=0)
inputField.pack(ipady=13)

mainFrame = Frame(window, width=312, height=272.5, bg="black")
mainFrame.pack()

tujuh = Button(mainFrame, text="7", fg="white",  bd=2, bg="#000000", command=lambda: clickButton(7)).grid(row=1, column=0, ipadx=27, ipady=27)

delapan = Button(mainFrame, text="8", fg="black", bd=2, bg="#F8F8FF", command=lambda: clickButton(8)).grid(row=1, column=1, ipadx=27, ipady=27)

sembilan = Button(mainFrame, text="9", fg="white", bd=2, bg="#000000", command=lambda: clickButton(9)).grid(row=1, column=2, ipadx=27, ipady=27)

empat = Button(mainFrame, text="4", fg="black", bd=2, bg="#F8F8FF", command=lambda: clickButton(4)).grid(row=2, column=0, ipadx=27, ipady=27)

lima = Button(mainFrame, text="5", fg="white",bd=2, bg="#000000", command=lambda: clickButton(5)).grid(row=2, column=1, ipadx=27, ipady=27)

enam = Button(mainFrame, text="6", fg="black", bd=2, bg="#F8F8FF", command=lambda: clickButton(6)).grid(row=2, column=2, ipadx=27, ipady=27)

satu = Button(mainFrame, text="1", fg="white", bd=2, bg="#000000", command=lambda: clickButton(1)).grid(row=3, column=0, ipadx=27, ipady=27)

dua = Button(mainFrame, text="2", fg="black", bd=2, bg="#F8F8FF", command=lambda: clickButton(2)).grid(row=3, column=1, ipadx=27, ipady=27)

tiga = Button(mainFrame, text="3", fg="white", bd=2, bg="#000000", command=lambda: clickButton(3)).grid(row=3, column=2, ipadx=27, ipady=27)

nol = Button(mainFrame, text="0", fg="white",bd=2, bg="#000000", command=lambda: clickButton(0)).grid(row=4, column=1, ipadx=27, ipady=27)

tambah = Button(mainFrame, text="+", fg="black", bd=2, bg="#F8F8FF", command=lambda: clickButton("+")).grid(row=3, column=3, ipadx=26, ipady=27)

kali = Button(mainFrame, text="x", fg="black", bd=2, bg="#F8F8FF", command=lambda: clickButton("*")).grid(row=1, column=3, ipadx=27, ipady=27)

bagi = Button(mainFrame, text=":", fg="white", bd=2, bg="#000000", command=lambda: clickButton("/")).grid(row=0, column=3, ipadx=28, ipady=27, columnspan=2)

kurang = Button(mainFrame, text="-", fg="white", bd=2, bg="#000000", command=lambda: clickButton("-")).grid(row=2, column=3, ipadx=27, ipady=27)

titik = Button(mainFrame, text=".", fg="black", bd=2, bg="#F8F8FF", command=lambda: clickButton(".")).grid(row=4, column=0, ipadx=28, ipady=27)

sama = Button(mainFrame, text="=",  fg="black", bd=2, bg="#F8F8FF", command=lambda: equalButton()).grid(row=4, column=2, columnspan=2, ipadx=61, ipady=27)

ac = Button(mainFrame, text="AC", fg="white",  bd=2, bg="#000000", command=lambda: clearAll()).grid(row=0, column=0,columnspan=2, ipadx=57, ipady=27)

clear = Button(mainFrame, text="del", fg="black", bd=2, bg="#F8F8FF", command=lambda: clearButton()).grid(row=0, column=2, ipadx=23, ipady=27)

window.mainloop()