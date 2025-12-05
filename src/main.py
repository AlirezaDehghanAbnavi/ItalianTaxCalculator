from components.window import MainWindow
from calculations.tax import *


def main():
    # app = MainWindow()
    # app.mainloop()
    regionInput = findRegion("Which region do you live in?")
    grossAnnualSalary = getSalary("How much do you make annually? ")
    salaryAfterTax = calculateTax(grossAnnualSalary, regionInput)
    result = (f"Your salary after tax is €{round(salaryAfterTax, 2)}\n"
             f"You've paid a total amount of €{round(grossAnnualSalary-salaryAfterTax, 2)} in taxes\n"
             f"You make €{round(salaryAfterTax/12, 2)} each month (After taxes)")
    
    print(result)


if __name__ == "__main__":
    main()