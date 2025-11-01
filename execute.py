import pandas as pd

rain = pd.read_csv("data/rainfall.csv")
crop = pd.read_csv("data/crop_production.csv")

# Just print column names first to verify
print("Rainfall columns:", rain.columns)
print("Crop columns:", crop.columns)

# Adjust these based on actual columns
# Rename for consistency
rain = rain.rename(columns={'year': 'Year', 'actual': 'Rainfall'})
rain = rain[['Year', 'Rainfall']]

# For crop_production.csv, use actual column names you showed earlier:
# _sl_no,name_of_the_state_ut,capacity_in_mt
crop = crop.rename(columns={'name_of_the_state_ut': 'State', 'capacity_in_mt': 'Production'})
crop = crop[['State', 'Production']]

print("\nCleaned Rainfall Data:")
print(rain.head())

print("\nCleaned Crop Data:")
print(crop.head())
