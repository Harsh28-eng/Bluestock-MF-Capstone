import pandas as pd

df = pd.read_csv("Data/Raw/07_scheme_performance.csv")

df = df.drop_duplicates()

df.to_csv(
    "Data/Raw/clean_performance.csv",
    index=False
)

print("Clean Performance Successfully")