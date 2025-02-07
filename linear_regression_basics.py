import yfinance as yf
import pandas as pd

# Get data for Google (GOOGL)
df = yf.download("GOOGL", start="2023-01-01", end="2024-01-01")

# Rename the columns
df = df.rename(columns={
    'Open': 'Adj. Open',
    'High': 'Adj. High',
    'Low': 'Adj. Low',
    'Close': 'Adj. Close',
    'Volume': 'Adj. Volume'
})

# Now you can use your original code:
df = df[['Adj. Open', 'Adj. High','Adj. Low','Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df [['Adj. Close','HL_PCT','PCT_change','Adj. Volume']]

print(df.head())