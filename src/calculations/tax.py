IRPEF_BRACKETS = {
    (0, 28000, 0.23), 
    (28001, 50000, 0.35),
    (50001, float("inf"), 0.43)
}
INPS_TAX = 0.0919


def getSalary(salary: str) -> float:
    while True:
        try:
            return float(input(salary))
        except ValueError:
            print("Invalid format, Please try again with correct format (Float, Integer).")


def calculateTax(grossAnnualSalary):
    salaryAfterTax: float = grossAnnualSalary
    incomeAfterINPS: float = grossAnnualSalary * (1 - INPS_TAX) 
    amountOfTax: float = 0
    
    if incomeAfterINPS <= 12000:
        return incomeAfterINPS

    for lowerBound, upperBound, taxRate in IRPEF_BRACKETS:
        if incomeAfterINPS > lowerBound:
            taxableIncome = min(incomeAfterINPS, upperBound) - lowerBound
            amountOfTax += taxableIncome * taxRate

    salaryAfterTax = incomeAfterINPS - amountOfTax
    return salaryAfterTax