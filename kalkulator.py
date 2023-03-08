import tkinter as tk

class CalculatorGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("CalculatorDn")
        self.create_widgets()

    def create_widgets(self):
        # Entry box for input/output
        self.entry = tk.Entry(self.master, width=30, justify="right", font=("Arial", 14))
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Buttons for numbers
        button_list = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]

        row = 1
        col = 0
        for button_text in button_list:
            tk.Button(
                self.master,
                text=button_text,
                width=6,
                height=2,
                font=("Arial", 14),
                background="#BDB76B",
                command=lambda x=button_text: self.button_click(x)
            ).grid(row=row, column=col, padx=3, pady=3)

            col += 1
            if col > 3:
                col = 0
                row += 1

                

        # Button for clearing entry
        tk.Button(
            self.master,
            text="Clear",
            width=6,
            height=2,
            font=("Arial", 14),
            background="#696969",
            command=self.clear_entry
        ).grid(row=row, column=0, padx=3, pady=3)

        # Button for deleting last character
        tk.Button(
            self.master,
            text="Del",
            width=6,
            height=2,
            font=("Arial", 14),
            background="#696969",
            command=self.delete_last_character
        ).grid(row=row, column=1, padx=3, pady=3)

    def button_click(self, button_text):
        if button_text == "=":
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        else:
            self.entry.insert(tk.END, button_text)

    def clear_entry(self):
        self.entry.delete(0, tk.END)

    def delete_last_character(self):
        self.entry.delete(len(self.entry.get())-1, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorGUI(master=root)
    app.mainloop()
