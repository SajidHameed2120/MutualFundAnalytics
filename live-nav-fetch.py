import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    fund_name = data["meta"]["scheme_name"]
    nav = data["data"][0]["nav"]
    date = data["data"][0]["date"]

    df = pd.DataFrame({
        "Fund_Name": [fund_name],
        "NAV": [nav],
        "Date": [date]
    })

    df.to_csv("data/raw/nav_data.csv", index=False)

    print("CSV file saved successfully!")