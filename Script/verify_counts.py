import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

nav_csv = len(
    pd.read_csv(
        "Data/Raw/clean_nav_history.csv"
    )
)

txn_csv = len(
    pd.read_csv(
        "Data/Raw/clean_transactions.csv"
    )
)

perf_csv = len(
    pd.read_csv(
        "Data/Raw/clean_performance.csv"
    )
)

print("Nav CSV Rows:", nav_csv)
print("Transactions CSV Rows:", txn_csv)
print("Performance CSV Rows:", perf_csv)
