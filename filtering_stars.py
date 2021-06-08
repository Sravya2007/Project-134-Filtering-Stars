import pandas as pd
import matplotlib.pyplot as plt

star_data = pd.read_csv("star_data.csv")

distance_column = pd.to_numeric(star_data['Distance (ly)'], errors = 'coerce').dropna()

gravity_column = star_data['Surface Gravity (m/s²)']

star_data = star_data[(distance_column <= 100) & ((gravity_column >= 150) & (gravity_column <= 350))]

print("Solar systems of", len(star_data), "stars are habitable")

star_data.to_csv("habitable_star_data.csv", index = False)

print("CSV file created!")