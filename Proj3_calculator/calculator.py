from tkinter import * 

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.task=""
        self.UserIn = StringVar()
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.user_input = Entry(self, bg = "#5BC8AC", bd = 29, insertwidth=4, width=24, font = ("Verdana", 20, "bold"), textvariable= self.UserIn, justify=RIGHT)
        self.user_input.grid(columnspan=4)

        self.user_input.insert(0, "0")

        self.button1 = Button(self, bg="#98DBC6", bd=12, text="7", padx=33, pady=25, font=("Helvetica", 20, "bold"), command=lambda : self.buttonClick(1))
        self.button1.grid(row=2, column=0, sticky=W)

        self.button2 = Button(self, bg="#98DBC6", bd=12, text="8", padx=33, pady=25, font=("Helvetica", 20, "bold"), command=lambda : self.buttonClick(2))
        self.button2.grid(row=2, column=1, sticky=W)
        
        self.button3 = Button(self, bg="#98DBC6", bd=12, text="9", padx=33, pady=25, font=("Helvetica", 20, "bold"), command=lambda : self.buttonClick(3))
        self.button3.grid(row=2, column=2, sticky=W)
        
        self.button4 = Button(self, bg="#98DBC6", bd=12, text="4", padx=33, pady=25, font=("Helvetica", 20, "bold"), command=lambda : self.buttonClick(4))
        self.button4.grid(row=3, column=0, sticky=W)
        
        self.button5 = Button(self, bg="#98DBC6", bd=12, text="5", padx=33, pady=25, font=("Helvetica", 20, "bold"), command=lambda : self.buttonClick(5))
        self.button5.grid(row=3, column=1, sticky=W)
        
        self.button6 = Button(self, bg="#98DBC6", bd=12, text="6", padx=33, pady=25, font=("Helvetica", 20, "bold"), command=lambda : self.buttonClick(6))
        self.button6.grid(row=3, column=2, sticky=W)
        
        self.button7 = Button(self, bg="#98DBC6", bd=12, text="1", padx=33, pady=25, font=("Helvetica", 20, "bold"), command=lambda : self.buttonClick(1))
        self.button7.grid(row=4, column=0, sticky=W)
        
        self.button8 = Button(self, bg="#98DBC6", bd=12, text="2", padx=33, pady=25, font=("Helvetica", 20, "bold"), command=lambda : self.buttonClick(2))
        self.button8.grid(row=4, column=1, sticky=W)
        
        self.button9 = Button(self, bg="#98DBC6", bd=12, text="3", padx=33, pady=25, font=("Helvetica", 20, "bold"), command=lambda : self.buttonClick(3))
        self.button9.grid(row=4, column=2, sticky=W)
        
        self.button10 = Button(self, bg="#98DBC6", bd=12, text="0", padx=33, pady=25, font=("Helvetica", 20, "bold"), command=lambda : self.buttonClick(0))
        self.button10.grid(row=5, column=0, sticky=W)
        
        self.AddButton = Button(self, bg="#98DBC6", bd=12, text="+", padx=33, pady=25, font=("Helvetica", 20, "bold"), command=lambda : self.buttonClick("+"))
        self.AddButton.grid(row=2, column=3, sticky=W)
        
        self.SubButton = Button(self, bg="#98DBC6", bd=12, text="-", padx=33, pady=25, font=("Helvetica", 20, "bold"), command=lambda : self.buttonClick("-"))
        self.SubButton.grid(row=3, column=3, sticky=W)
        
        self.MulButton = Button(self, bg="#98DBC6", bd=12, text="*", padx=33, pady=25, font=("Helvetica", 20, "bold"), command=lambda : self.buttonClick("*"))
        self.MulButton.grid(row=4, column=3, sticky=W)

        self.DivButton = Button(self, bg="#98DBC6", bd=12, text="/", padx=33, pady=25, font=("Helvetica", 20, "bold"), command=lambda : self.buttonClick(7))
        self.DivButton.grid(row=5, column=3, sticky=W)

        self.EqualButton = Button(self, bg="#98DBC6", bd=12, text="=", padx=100, pady=25, font=("Helvetica", 20, "bold"), command=self.CalculateTask)
        self.EqualButton.grid(row=5, column=1, sticky=W, columnspan=2)
        
        self.ClearButton = Button(self, bg="#98DBC6", bd=12, text="AC", padx=7, width=28, font=("Helvetica", 20, "bold"), command=self.ClearDisplay)
        self.ClearButton.grid(row=1, columnspan=4, sticky=W)
        
    def buttonClick(self, number):
        self.task = str(self.task) + str(number)
        self.UserIn.set(self.task)

    def CalculateTask(self):
        self.data = self.user_input.get()
        try:
            self.answer = eval(self.data)
            self.displayText(self.answer)
            self.task = ""
        
        except SyntaxError as e:
            self.displayText("Invalid Input")
            self.task = ""
    
    def displayText(self, value):
        self.user_input.delete(0, END)
        self.user_input.insert(0, value)

    def ClearDisplay(self):
        self.tasl = ""
        self.user_input.delete(0, END)
        self.user_input.insert(0, "0")

calculator = Tk()
calculator.title("Calculator")
App = Application(calculator)

calculator.resizable(width=False, height=False)

calculator.mainloop()
