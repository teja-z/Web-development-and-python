import pandas as pd

# Example Series for demonstration
asking_prices = pd.Series([12000, 15000, 18000, 20000, 22000])
fair_prices = pd.Series([13000, 14000, 18500, 21000, 21500])

# Find where asking price is less than fair price
good_deals = asking_prices < fair_prices

# Get indices of good deals
good_deal_indices = asking_prices[good_deals].index.tolist()

print("Indices of good deals:", good_deal_indices)
