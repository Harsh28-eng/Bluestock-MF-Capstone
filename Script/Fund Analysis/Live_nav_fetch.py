import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

data = response.json()

df = pd.DataFrame(data["data"])

df.to_csv("Data/Raw/hdfc_top100_nav.csv", index=False)

print("File saved successfully")