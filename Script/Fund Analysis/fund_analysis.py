import pandas as pd

# Load dataset
df = pd.read_csv("Data/Raw/01_fund_master.csv")

print("Fund Master Analysis")

# Total Schemes
print("\nTotal Schemes:")
print(df.shape[0])

# Total Fund Houses
print("\nTotal Fund Houses:")
print(df["fund_house"].nunique())

# Unique Fund Houses
print("\nFund Houses:")
print(df["fund_house"].unique())

# Categories
print("\nCategories:")
print(df["category"].unique())

# Sub Categories
print("\nSub Categories:")
print(df["sub_category"].unique())

# Risk Categories
print("\nRisk Categories:")
print(df["risk_category"].unique())

# Scheme Count by Fund House
print("\nSchemes per Fund House:")
print(df["fund_house"].value_counts())

# Scheme Count by Category
print("\nSchemes per Category:")
print(df["category"].value_counts())

# Scheme Count by Risk Category
print("\nSchemes per Risk Category:")
print(df["risk_category"].value_counts())