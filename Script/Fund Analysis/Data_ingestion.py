import pandas as pd

files = [
    "Data/raw/01_fund_master.csv",
    "Data/raw/02_nav_history.csv",
    "Data/raw/03_aum_by_fund_house.csv",
    "Data/raw/04_monthly_sip_inflows.csv",
    "Data/raw/05_category_inflows.csv",
    "Data/raw/06_industry_folio_count.csv",
    "Data/raw/07_scheme_performance.csv",
    "Data/raw/08_investor_transactions.csv",
    "Data/raw/09_portfolio_holdings.csv",
    "Data/raw/10_benchmark_indices.csv"
]

for file in files:

    print("\n" + "="*70)
    print("FILE:", file)

    df = pd.read_csv(file)

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("\nTop 5 Rows:")
    print(df.head())