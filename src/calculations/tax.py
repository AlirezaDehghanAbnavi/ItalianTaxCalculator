import json
import os

INPS_TAX = 0.0919

base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
nationalTaxPath = os.path.join(base_dir, "data", "national_tax.json")
regionalTaxPath = os.path.join(base_dir, "data", "regional_tax.json")


def loadTaxFile(file_path: str) -> dict:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Tax data file not found: {file_path}")


nationalData = loadTaxFile(nationalTaxPath)

IRPEF_BRACKETS = [
    (bracket[0], float('inf') if bracket[1] == "inf" else bracket[1], bracket[2])
    for bracket in nationalData.get("IRPEF_BRACKETS", [])
]


regionalData = loadTaxFile(regionalTaxPath)

REGIONAL_BRACKETS = dict()

for region, brackets in regionalData.items():
    REGIONAL_BRACKETS[region] = [
        (bracket[0], float('inf') if bracket[1] == "inf" else bracket[1], bracket[2])
        for bracket in brackets
    ]


def getSalary(salaryInput: str = None) -> float:
    try:
        if salaryInput is None:
            salaryInput = input("How much do you make annually? ")
        salary = float(salaryInput)
        return salary
    except ValueError:
        raise ValueError("Invalid format, Please try again with correct format (Float, Integer).")

        
            


def findRegion(regionInput: str = None) -> str:
    if regionInput is None:
        regionInput = input("Which region do you live in? ").strip()

    for region in REGIONAL_BRACKETS.keys():
        if regionInput.lower() in region.lower():
            return region

    raise ValueError("Region not found")


def calculateTax(grossAnnualSalary, regionInput):
    salaryAfterTax: float = grossAnnualSalary
    incomeAfterINPS: float = grossAnnualSalary * (1 - INPS_TAX) 
    amountOfTax: float = 0
    
    if incomeAfterINPS <= 12000:
        return incomeAfterINPS

    for lowerBound, upperBound, taxRate in IRPEF_BRACKETS:
        if incomeAfterINPS > lowerBound:
            taxableIncome = min(incomeAfterINPS, upperBound) - lowerBound
            amountOfTax += taxableIncome * taxRate
   
    for lower, upper, rate in REGIONAL_BRACKETS[regionInput]:
        if incomeAfterINPS > lower:
            taxableIncome = min(incomeAfterINPS, upper) - lower
            amountOfTax += taxableIncome * rate

    salaryAfterTax = incomeAfterINPS - amountOfTax
    
    return salaryAfterTax