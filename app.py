import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson, norm

# Copy your statistical functions and data here
# ... (Your existing functions)

# Water usage data in million cubic meters
years = np.array([2015, 2016, 2017, 2018])
total_water_usage = np.array([5224.5, 4668.7, 5072.4, 5088.7])
industrial_usage = np.array([86.5, 67.2, 69.1, 82.5])
agricultural_usage = np.array([4922.2, 4435.3, 4821.6, 4817.0])
domestic_usage = np.array([194.1, 155.6, 157.0, 161.1])
other_usage = np.array([21.7, 10.6, 24.6, 28.0])

def main():
    st.title("Water Usage Statistics and Visualization")

    # Sidebar for user input
    st.sidebar.header("User Input")

    # Display raw data
    st.subheader("Water Usage Data")
    st.table({
        "Year": years,
        "Total Water Usage": total_water_usage,
        "Industrial Usage": industrial_usage,
        "Agricultural Usage": agricultural_usage,
        "Domestic Usage": domestic_usage,
        "Other Usage": other_usage,
    })

    # Visualization
    st.subheader("Visualization")

    # Line plot for Total Water Usage over the years
    st.line_chart(pd.DataFrame({"Year": years, "Total Water Usage": total_water_usage}).set_index("Year"))

    # Bar chart for Conditional Probability
    event_a = industrial_usage > 80.0
    event_b = total_water_usage > 5000.0
    conditional_prob = conditional_probability(event_a, event_b)
    st.bar_chart(pd.DataFrame({"P(Industrial Usage > 80 | Total Water Usage > 5000)": [conditional_prob]}))

    # Line plot for Probability Distribution (Normal Distribution)
    x_values = np.linspace(-3, 3, 100)
    pdf_values = calculate_probability_distribution('normal', mean=0, std_dev=1, x=x_values)
    st.line_chart(pd.DataFrame({"X": x_values, "Probability Density": pdf_values}).set_index("X"))

    # Scatter plot for Covariance and Correlation
    scatter_data = pd.DataFrame({
        "Year": years,
        "Agricultural Usage": agricultural_usage,
        "Domestic Usage": domestic_usage
    })
    st.scatter_chart(scatter_data.set_index("Year"))

if __name__ == "__main__":
    main()
