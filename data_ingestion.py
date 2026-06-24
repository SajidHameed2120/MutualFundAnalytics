import pandas as pd

df = pd.read_csv("data/raw/nav_data.csv")

print("Shape:", df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())
print("\nMissing Values:")
print(df.isnull().sum())