import json
import os

INPS_TAX = 0.0919

base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
national_tax_path = os.path.join(base_dir, "data", "national_tax.json")
regional_tax_path = os.path.join(base_dir, "data", "regional_tax.json")


def load_tax_file(file_path: str) -> dict:
    """Opens data files needed by the program."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Tax data file not found: {file_path}")


national_data = load_tax_file(national_tax_path)

IRPEF_BRACKETS = [
    (bracket[0], float('inf') if bracket[1] == "inf" else bracket[1], bracket[2])
    for bracket in national_data.get("IRPEF_BRACKETS", [])
]


regional_data = load_tax_file(regional_tax_path)

REGIONAL_BRACKETS = dict()

for region, brackets in regional_data.items():
    REGIONAL_BRACKETS[region] = [
        (bracket[0], float('inf') if bracket[1] == "inf" else bracket[1], bracket[2])
        for bracket in brackets
    ]


def get_salary(salary_input: str = None) -> float:
    """This function asks the user for an input and check it's validity."""
    try:
        if salary_input is None:
            salary_input = input("How much do you make annually? ")
        salary = float(salary_input)
        return salary
    except ValueError:
        raise ValueError("Invalid format, Please try again with correct format (Float, Integer).")

        
            


def find_region(region_input: str = None) -> str:
    """This function finds the region from a .json data file."""
    if region_input is None:
        region_input = input("Which region do you live in? ").strip()

    for region in REGIONAL_BRACKETS.keys():
        if region_input.lower() in region.lower():
            return region

    raise ValueError("Region not found")


def calculate_tax(gross_annual_salary, region_input):
    """This function is the main logic behind calculating taxes."""
    salary_after_tax: float = gross_annual_salary
    income_after_INPS: float = gross_annual_salary * (1 - INPS_TAX) 
    tax_amount: float = 0
    
    if income_after_INPS <= 12000:
        return income_after_INPS

    for lower, upper, tax in IRPEF_BRACKETS:
        if income_after_INPS > lower:
            taxable_income = min(income_after_INPS, upper) - lower
            tax_amount += taxable_income * tax
   
    for lower, upper, rate in REGIONAL_BRACKETS[region_input]:
        if income_after_INPS > lower:
            taxable_income = min(income_after_INPS, upper) - lower
            tax_amount += taxable_income * rate

    salary_after_tax = income_after_INPS - tax_amount
    
    return salary_after_tax