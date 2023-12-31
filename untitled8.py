# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10SH0l05AhgafTHmvN_FUvJGOIQgnWGhO
"""

import pandas as pd
import numpy as np

# Simulate demographic data
np.random.seed(42)
population_size = 1000
age = np.random.randint(18, 65, size=population_size)
household_size = np.random.randint(1, 6, size=population_size)

# Simulate water usage data
water_source = np.random.choice(['Street Column', 'Apartment', 'Private House'], size=population_size)
water_consumption = np.zeros(population_size)
sewage_disposal = np.zeros(population_size)

for i in range(population_size):
    if water_source[i] == 'Street Column':
        water_consumption[i] = np.random.uniform(30, 40)
        sewage_disposal[i] = np.random.uniform(0, 10)
    elif water_source[i] == 'Apartment':
        water_consumption[i] = np.random.uniform(300, 320)
        sewage_disposal[i] = np.random.uniform(460, 480)
    elif water_source[i] == 'Private House':
        water_consumption[i] = np.random.uniform(330, 360)
        sewage_disposal[i] = np.random.uniform(470, 500)

# Create a simulated DataFrame
data = pd.DataFrame({
    'Age': age,
    'Household Size': household_size,
    'Water Source': water_source,
    'Water Consumption (liters per day)': water_consumption,
    'Sewage Disposal (liters per day)': sewage_disposal
})

# Save the simulated data to a CSV file
data.to_csv('simulated_water_data_bishkek.csv', index=False)

