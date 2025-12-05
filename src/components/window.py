import tkinter as tk
from .title import Title
from calculations.tax import *

class MainWindow(tk.Tk):   # JAVA -> Class MainWindow extendes tk.Tk
    def __init__(self):    # JAVA -> Constructor MainWindow(){}
        super().__init__()
 

        self.geometry("590x750") # Determines size
        self.title("Italian Tax Calculator") # Title
        self.config(background="#123456") # Set Background Color


        # Set New Icon
        icon = tk.PhotoImage(file='./photos/italia.png') 
        self.iconphoto(True, icon)


        # Displaying title label
        self.titleLable = Title(self)
        self.titleLable.pack(pady=5)


        # Region input
        tk.Label(self, text="Which region do you live in?", bg="#123456", fg="white", font=("Arial", 15)).pack()
        self.regionEntry = tk.Entry(self, width=30)
        self.regionEntry.pack(pady=5)


        # Salary input
        tk.Label(self, text="How much do you make annually?", bg="#123456", fg="white", font=("Arial", 15)).pack()
        self.salaryEntry = tk.Entry(self, width=30)
        self.salaryEntry.pack(pady=5)


        # Calculate button
        self.calcButton = tk.Button(self, text="calculate", command=self.calculate)
        self.calcButton.pack(pady=20)


        # Result label
        self.resultLabel = tk.Label(self, text="", bg="#123456", fg="white", justify="left", font=("Arial", 15))
        self.resultLabel.pack(pady=10)


        # Reset Button
        self.resetButton = tk.Button(self, text="Reset", command=self.reset)
        self.resetButton.pack(pady=10)


        # Disclaimer
        self.disclaimerLabel = tk.Label(
            self,
            text="Disclaimer: This calculator provides estimates only. Actual tax may vary.",
            bg="#123456",
            fg="red",
            font=("Arial", 15),
            wraplength=550,   # wrap text to fit window width
            justify="center"
        )
        self.disclaimerLabel.pack(side="bottom", pady=10)


    def calculate(self):
        regionInput = findRegion(self.regionEntry.get())
        grossAnnualSalary = getSalary(self.salaryEntry.get())

        # Calculate tax
        salaryAfterTax = calculateTax(grossAnnualSalary, regionInput)
        total_tax = grossAnnualSalary - salaryAfterTax
        monthly_income = salaryAfterTax / 12

        # Display result
        self.resultLabel.config(
            text=f"Your salary after tax is €{round(salaryAfterTax, 2)}\n"
                f"You've paid a total amount of €{round(total_tax, 2)} in taxes\n"
                f"You make €{round(monthly_income, 2)} each month (After taxes)"
        )


    
    def reset(self):
        self.regionEntry.delete(0, tk.END)
        self.salaryEntry.delete(0, tk.END)
        self.resultLabel.config(text="")
        