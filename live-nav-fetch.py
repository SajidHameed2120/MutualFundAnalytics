import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    fund_name = data["meta"]["scheme_name"]

    nav_data = []

    for record in data["data"]:
        nav_data.append({
            "Fund_Name": fund_name,
            "NAV": float(record["nav"]),
            "Date": record["date"]
        })

    df = pd.DataFrame(nav_data)

    df.to_csv("data/raw/nav_data.csv", index=False)

    print("CSV saved successfully!")
    print("Rows:", len(df))
else:
    print("Error:", response.status_code)