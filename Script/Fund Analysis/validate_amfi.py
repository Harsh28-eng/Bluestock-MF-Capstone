import pandas as pd

# Load datasets
fund_master = pd.read_csv("Data/Raw/01_fund_master.csv")
nav_history = pd.read_csv("Data/Raw/02_nav_history.csv")

# Get unique AMFI codes
fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

# Find missing codes
missing_codes = fund_codes - nav_codes

print("AMFI CODE VALIDATION REPORT")

print("\nTotal Fund Master Codes:", len(fund_codes))
print("Total NAV History Codes:", len(nav_codes))

if len(missing_codes) == 0:
    print("\n All AMFI Codes are present in NAV History")
else:
    print("\n Missing AMFI Codes:")
    print(missing_codes)

print("\nValidation Complete")