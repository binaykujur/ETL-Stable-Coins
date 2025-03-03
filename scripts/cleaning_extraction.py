# Import necessary libraries
import pandas as pd
import numpy as np

# Load the dataset
file_path = 'raw_data/stablecoins_data.csv'
data = pd.read_csv(file_path)

# 1. Handle missing values: Fill with column mean for numerical columns
data['High_24h_USD'].fillna(data['High_24h_USD'].mean(), inplace=True)
data['Low_24h_USD'].fillna(data['Low_24h_USD'].mean(), inplace=True)
data['Price_Change_24h'].fillna(data['Price_Change_24h'].mean(), inplace=True)

# 2. Convert 'Last_Updated' to datetime format
data['Last_Updated'] = pd.to_datetime(data['Last_Updated'])

# 3. Remove duplicates
data.drop_duplicates(inplace=True)

# 4. Standardize column names
data.columns = data.columns.str.lower().str.replace(' ', '_')

# 5. Create new features

# a. Price volatility (difference between high and low prices in 24h)
data['price_volatility_24h'] = data['high_24h_usd'] - data['low_24h_usd']

# b. Market cap to volume ratio
data['market_cap_to_volume_ratio'] = data['market_cap_usd'] / data['total_volume_usd']

# c. Normalized price (min-max scaling)
data['normalized_price'] = (data['current_price_usd'] - data['current_price_usd'].min()) / \
                           (data['current_price_usd'].max() - data['current_price_usd'].min())

# d. Price movement category
data['price_movement_category'] = pd.cut(
    data['price_change_24h'],
    bins=[-float('inf'), -0.01, 0.01, float('inf')],
    labels=['down', 'stable', 'up']
).astype('category')

# e. Log transformation to reduce skewness
data['log_market_cap_usd'] = np.log1p(data['market_cap_usd'])
data['log_total_volume_usd'] = np.log1p(data['total_volume_usd'])

# f. Extract time-based features
data['hour_of_day'] = data['last_updated'].dt.hour
data['day_of_week'] = data['last_updated'].dt.dayofweek

# 6. Reorder columns for better readability
data = data[['id', 'symbol', 'name', 'current_price_usd', 'market_cap_usd', 'total_volume_usd',
             'high_24h_usd', 'low_24h_usd', 'price_change_24h', 'price_volatility_24h',
             'market_cap_to_volume_ratio', 'normalized_price', 'price_movement_category',
             'log_market_cap_usd', 'log_total_volume_usd', 'hour_of_day', 'day_of_week', 'last_updated']]

# 7. Reset index
data.reset_index(drop=True, inplace=True)

# 8. Save cleaned and feature-engineered dataset to a new CSV file
cleaned_file_path = 'cleaned_data/stablecoins_data_cleaned.csv'
data.to_csv(cleaned_file_path, index=False)

print(f"Dataset saved successfully as {cleaned_file_path}")
