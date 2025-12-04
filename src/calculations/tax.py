import json
import os


base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
data_path = os.path.join(base_dir, "data", "national_tax.json")


with open(data_path, "r") as f:
    try:
        data = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Tax data file not found: {data_path}")


IRPEF_BRACKETS = [
    (bracket[0], float('inf') if bracket[1] == "inf" else bracket[1], bracket[2])
    for bracket in data.get("IRPEF_BRACKETS", [])
]

INPS_TAX = data.get("INPS_TAX", 0.0919)


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