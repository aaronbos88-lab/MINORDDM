# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 18:16:03 2024

@author: rbaia
"""

# Normal probability plot of heights of Olympic Athletes

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm
import scipy.stats as stats

# Load the data
data = pd.read_csv("olympic_athlete_database.csv")  # read the dataset and assign it a name (e.g., 'data')

# Get height data and drop NaN values if necessary
#heights = data['height'].dropna()

# Parameters for the normal distribution
mu = np.mean(data['height'])  # Mean of the distribution
sigma = np.std(data['height'])  # Standard deviation

print(mu, sigma)



# Plotting a PDF of heights
plt.hist(data['height'], bins=30, density=True, edgecolor='black', label='Olympian heights')  # density=True normalizes the histogram
plt.title('PDF of Heights of Olympians')
plt.xlabel('Height')
plt.ylabel('Probability density')
plt.legend()
plt.show()



# Plot a PDF of the heights (with parameters from the dataset) including the data
# I used the following example: https://stackoverflow.com/questions/55096595/how-to-plot-normal-distribution-curve-along-with-central-limit-theorem
count, bins, ignored = plt.hist(data['height'], bins=30, density=True, edgecolor='black', label='Olympian heights')

xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax)

max_density = stats.norm.pdf(mu, mu, sigma)
scale = count.max() / max_density

plt.plot(x, scale * stats.norm.pdf(x, mu, sigma), label='Normal distribution')
#plt.vlines(x=176.3, ymin=0, ymax=0.05, color='red', linestyles='dashed', label='Mean')
plt.title(f'PDF of Heights of Olympians (Mean={mu:.2f}, std={sigma:.2f})')
plt.xlabel('Height')
plt.ylabel('Probability density')
plt.legend(loc='upper left')
plt.show()




