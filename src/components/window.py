"""Window class representing the main body for GUI elements."""
import tkinter as tk
from tkinter import messagebox, ttk
from src.utils.paths import PHOTOS_DIR
from src.calculations.tax import find_region, get_salary, calculate_tax, region_names
from src.components.title import Title

class MainWindow(tk.Tk):   # JAVA -> Class MainWindow extendes tk.Tk
    """Subclass of Tk for GUI implementation."""
    def __init__(self):    # JAVA -> Constructor MainWindow(){}
        """Constructor for Mainwindow class."""
        super().__init__()


        self.geometry("680x850") # Determines size
        self.title("Italian Tax Calculator") # Title
        self.config(background="#F2EBCB") # Set Background Color


        # Set New Icon
        icon = tk.PhotoImage(file=PHOTOS_DIR/"italia.png")
        self.iconphoto(True, icon)


        # Displaying title label
        self.title_label = Title(self)
        self.title_label.pack(pady=5)


        # Region Drop Down
        tk.Label(self, text="Region of residence:",
                    bg="#F2EBCB", fg="black", font=("Arial", 15)).pack()
        self.clicked = tk.StringVar()
        self.clicked.set("Select a Region")
        self.drop_menu = tk.OptionMenu(self, self.clicked, *region_names)
        self.drop_menu.config(
            width=20,
            font=("Arial", 12),
            bg="lightyellow",
            fg="black",
            activebackground="#2999BE",
            activeforeground="white"
        )
        self.drop_menu.pack(pady=5)


        # Salary input
        tk.Label(self, text="Annual Income:",
                  bg="#F2EBCB", fg="black", font=("Arial", 15)).pack()
        self.salary_entry = tk.Entry(self, width=30)
        self.salary_entry.pack(pady=5)


        # Calculate button
        self.calc_button = tk.Button(self, text="calculate", command=self.calculate,
                                     width=8, height=1, font=("Arial", 12))
        self.calc_button.config(
            width=13,
            font=("Arial", 12),
            bg="#EDEFD6",
            fg="black",
            activebackground="#2999BE",
            activeforeground="white"
        )
        self.calc_button.pack(pady=20)


        # Result label
        self.result_label = tk.Label(self, text="",
                                        bg="#F2EBCB",
                                        fg="black", justify="left", font=("Arial", 16))
        self.result_label.pack(pady=10)


        # Disclaimer
        self.disclaimer_label = tk.Label(
            self,
            text="Disclaimer: This calculator provides estimates only. Actual amount may vary.",
            bg="#F2EBCB",
            fg="#800020",
            font=("Arial", 15)
        )
        self.disclaimer_label.pack(side="bottom", pady=10)


        # Reset Button
        self.reset_button = tk.Button(self, text="Reset", command=self.reset)
        self.reset_button.config(
            font=("Arial", 10),
            bg="#EDEFD6",
            fg="black",
            activebackground="#AC3434",
            activeforeground="white"
        )
        self.reset_button.pack(side="bottom", pady=10)


    def calculate(self):
        """Demonstrates final results based on inputs."""
        # Empty/Invalid cases
        if  not self.salary_entry.get():
            messagebox.showerror("Input error", "Please complete the Income field")
            return
        try:
            region_input = find_region(self.clicked.get())
            gross_annual_salary = get_salary(self.salary_entry.get())

        except (ValueError, TypeError) as error:
            messagebox.showerror("Input error", str(error))

        # Calculate tax
        salary_after_tax = calculate_tax(gross_annual_salary, region_input)
        total_tax = gross_annual_salary - salary_after_tax
        monthly_income = salary_after_tax / 12

        # Display result
        self.result_label.config(
            text=f"Total taxes paid: €{round(total_tax, 2)}\n"
            f"Net salary: €{round(salary_after_tax, 2)}\n"
            f"Monthly income after taxes: €{round(monthly_income, 2)}"
        )


    def reset(self):
        """Reseting the result."""
        self.salary_entry.delete(0, tk.END)
        self.clicked.set("Select a Region")
        self.result_label.config(text="")
