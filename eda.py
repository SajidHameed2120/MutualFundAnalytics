import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("data/raw/nav_data.csv")

# Convert Date
df["Date"] = pd.to_datetime(df["Date"], format="%d-%m-%Y")

# Sort data
df = df.sort_values("Date")

# Calculate daily return
df["Daily_Return"] = df["NAV"].pct_change() * 100

# Plot daily returns
fig = px.line(
    df,
    x="Date",
    y="Daily_Return",
    title="Daily NAV Returns (%)"
)

fig.write_html("daily_returns.html")

print("Daily Returns chart created successfully!")