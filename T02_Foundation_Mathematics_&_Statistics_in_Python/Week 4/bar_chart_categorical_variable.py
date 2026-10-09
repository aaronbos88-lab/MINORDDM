# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 21:40:59 2024

@author: rbaia
"""

# Plot a bar chart showing the distribution of a categorical variable

import pandas as pd
import matplotlib.pyplot as plt

data = ['ab', 'ab', 'pg', 'sd', 'pg']
data = pd.Series(data)                          # The data has be convered to a pandas dataframe to use value_counts()

# Count the frequencies of each unique value
frequencies = data.value_counts().sort_index()

# To plot the distribution
plt.figure(figsize=(8, 6))                      # Set figure size
plt.bar(frequencies.index, frequencies.values, edgecolor='black')  # Frequencies.index are the categories, frequencies.values are the counts
plt.title('Distribution of some categorical variable')
plt.xlabel("Category")
plt.ylabel("Frequency")
plt.xticks(frequencies.index)                   # Ensure the x-ticks align with the categories
plt.show()