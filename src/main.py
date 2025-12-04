from components.window import MainWindow
from calculations.tax import *


def main():
    app = MainWindow()
    app.mainloop()
    grossAnnualSalary = getSalary("How much do you make annually? ")
    salaryAfterTax = calculateTax(grossAnnualSalary)
    print(f"Your salary after tax is €{round(salaryAfterTax, 2)}")
    print(f"You make €{round(salaryAfterTax/12, 2)} each month (After taxes)")


if __name__ == "__main__":
    main()