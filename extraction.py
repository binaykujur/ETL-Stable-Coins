import requests
import pandas as pd

# CoinGecko API endpoint for stablecoins
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",  # Prices in USD
    "category": "stablecoins",  # Filter by stablecoins
    "order": "market_cap_desc",  # Order by market cap
    "per_page": 100,  # Number of results (max 100)
    "page": 1,  # Page number
    "sparkline": False  # Exclude sparkline data
}

# Fetch data from CoinGecko API
response = requests.get(url, params=params)
data = response.json()

# Check if data is fetched successfully
if response.status_code == 200:
    print(f"Fetched {len(data)} stablecoins.")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
    exit()

# Convert data to a pandas DataFrame
df = pd.DataFrame(data)

# Select relevant columns
columns = [
    "id", "symbol", "name", "current_price", "market_cap", "total_volume",
    "high_24h", "low_24h", "price_change_percentage_24h", "last_updated"
]
df = df[columns]

# Rename columns for better readability
df.columns = [
    "ID", "Symbol", "Name", "Current Price (USD)", "Market Cap (USD)", "Total Volume (USD)",
    "High 24h (USD)", "Low 24h (USD)", "Price Change % (24h)", "Last Updated"
]

# Save DataFrame to a CSV file
csv_file = "stablecoins_data.csv"
df.to_csv(csv_file, index=False)
print(f"Data saved to {csv_file}")