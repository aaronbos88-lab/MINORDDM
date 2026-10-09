# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 21:06:12 2024

@author: rbaia
"""

# Example of how to compute integrals


import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

# Define the demand function with only weekly peaks
def demand(t):
    daily_demand = 45 + 20 * np.sin((2 * np.pi / 7) * t)      # Weekly fluctuation, with 7-day cycles
    return daily_demand

# Generate data points for plotting
t = np.linspace(0, 90, 300)   # Time period from 0 to 30 days
demand_values = demand(t)     # Demand over time

# Plot the demand curve
plt.figure(figsize=(10, 6))
plt.xlim(0, 90)                                       # Set x-axis limits (0 to 30 days)
plt.ylim(0, 80)                                       # Set y-axis limits (70 to 130 units of demand)
plt.xlabel("Days")                                    # Label for x-axis
plt.ylabel("Demand (units)")                          # Label for y-axis
plt.plot(t, demand_values, label='Demand over time')  # Plot demand curve
#plt.fill_between(t, demand_values, color='tomato', where=t<30, alpha=0.5, label='Demand coming month')  # Fill the area under the curve
plt.title("Demand for electronic gadgets over time")  # Title of the plot
plt.legend()
plt.show()

# Compute the integral, i.e., total demand, by integrating the demand function from 0 to 30 days
total_demand, error = quad(demand, 0, 30)

# Print the result
print(f'Total demand over 30 days: {total_demand:.2f} units')