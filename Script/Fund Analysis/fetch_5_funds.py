import requests
import pandas as pd

funds = {
    "119551": "sbi_bluechip",
    "120503": "icici_bluechip",
    "118632": "nippon_largecap",
    "119092": "axis_bluechip",
    "120841": "kotak_bluechip"
}

for code, name in funds.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        df = pd.DataFrame(data["data"])

        df.to_csv(
            f"Data/Raw/{name}.csv",
            index=False
        )

        print(f"{name}.csv saved successfully")

    else:
        print(f"Failed to fetch {name}")