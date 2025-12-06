"""Window class representing the main body for GUI elements."""
import tkinter as tk
from tkinter import messagebox
from utils.paths import PHOTOS_DIR
from calculations.tax import find_region, get_salary, calculate_tax
from .title import Title

class MainWindow(tk.Tk):   # JAVA -> Class MainWindow extendes tk.Tk
    """Subclass of Tk for GUI implementation."""
    def __init__(self):    # JAVA -> Constructor MainWindow(){}
        """Constructor for Mainwindow class."""
        super().__init__()


        self.geometry("590x750") # Determines size
        self.title("Italian Tax Calculator") # Title
        self.config(background="#123456") # Set Background Color


        # Set New Icon
        icon = tk.PhotoImage(file=PHOTOS_DIR/"italia.png")
        self.iconphoto(True, icon)


        # Displaying title label
        self.title_label = Title(self)
        self.title_label.pack(pady=5)


        # Region input
        tk.Label(self, text="Which region do you live in?",
                    bg="#123456", fg="white", font=("Arial", 15)).pack()
        self.region_entry = tk.Entry(self, width=30)
        self.region_entry.pack(pady=5)


        # Salary input
        tk.Label(self, text="How much do you make annually?",
                  bg="#123456", fg="white", font=("Arial", 15)).pack()
        self.salary_entry = tk.Entry(self, width=30)
        self.salary_entry.pack(pady=5)


        # Calculate button
        self.calc_button = tk.Button(self, text="calculate", command=self.calculate)
        self.calc_button.pack(pady=20)


        # Result label
        self.result_label = tk.Label(self, text="",
                                        bg="#123456",
                                        fg="white", justify="left", font=("Arial", 15))
        self.result_label.pack(pady=10)


        # Reset Button
        self.reset_button = tk.Button(self, text="Reset", command=self.reset)
        self.reset_button.pack(pady=10)


        # Disclaimer
        self.disclaimer_label = tk.Label(
            self,
            text="Disclaimer: This calculator provides estimates only. Actual tax may vary.",
            bg="#123456",
            fg="black",
            font=("Arial", 15),
            wraplength=550,   # wrap text to fit window width
            justify="center"
        )
        self.disclaimer_label.pack(side="bottom", pady=10)


    def calculate(self):
        """Demonstrates final results based on inputs."""
        # Empty/Invalid cases
        if not self.region_entry.get() or not self.salary_entry.get():
            messagebox.showerror("Input error", "Please complete both fields")
            return
        try:
            region_input = find_region(self.region_entry.get())
            gross_annual_salary = get_salary(self.salary_entry.get())

        except Exception as error:
            messagebox.showerror("Input error", str(error))

        # Calculate tax
        salary_after_tax = calculate_tax(gross_annual_salary, region_input)
        total_tax = gross_annual_salary - salary_after_tax
        monthly_income = salary_after_tax / 12

        # Display result
        self.result_label.config(
            text=f"Your salary after tax is €{round(salary_after_tax, 2)}\n"
                f"You've paid a total amount of €{round(total_tax, 2)} in taxes\n"
                f"You make €{round(monthly_income, 2)} each month (After taxes)"
        )


    def reset(self):
        """Resetung GUI elements."""
        self.region_entry.delete(0, tk.END)
        self.salary_entry.delete(0, tk.END)
        self.result_label.config(text="")
