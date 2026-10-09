# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 21:45:18 2024

@author: rbaia
"""

# Plot a histogram showing the distribution of a numerical variable

import matplotlib.pyplot as plt

# Decimal (rational) data
data = [1.2, 2.3, 4.1, 5.6, 1.8, 4.9, 3.3, 5.2, 3.7, 4.4, 6.1]

# Plot the histogram
plt.figure(figsize=(8, 6))                                 # Set figure size
plt.hist(data, bins=6, color='green', edgecolor='black')   # 'bins' specifies the number of columns, 'edgecolor' outlines the bars
plt.title('Distribution of some numerical variable')
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()