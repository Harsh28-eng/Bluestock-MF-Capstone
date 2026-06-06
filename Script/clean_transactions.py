import pandas as pd

df = pd.read_csv("Data/Raw/08_investor_transactions.csv")

df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

df = df[df["amount_inr"] > 0]

df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

valid_kyc = [
    "Verified",
    "Pending",
    "Rejected"
]

df = df[df["kyc_status"].isin(valid_kyc)]

df.to_csv(
    "Data/Raw/clean_transactions.csv",
    index=False
)

print("Clean Transactions Successfully")