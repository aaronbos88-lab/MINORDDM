# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 11:15:00 2024

@author: rbaia
"""

# Exercise computing the natural logarithm of an exponential function
# Investment of 20, return is 3% per month, how long does it take to triple the investment?


# Plot the exponential function
from sympy import symbols
import matplotlib.pyplot as plt
import numpy as np

# Declare the variable x
x = symbols('x')

# Generate values of t
x = np.linspace(0, 100, 1000)

# Define the estimated exponential function
y1 = ____                                              # Fill in

# Plot the function
plt.plot(x, y1)
plt.hlines(60, 0, 40)                                  # Plot a horizontal line at y=60 (the total investment after ? months)
plt.title('Exponential function with e')
plt.xlabel("x (r*t)")
plt.ylabel("y")
plt.xlim([0,40])
plt.ylim([0,80])
plt.legend(loc='lower right')
plt.grid(True)
plt.show()




# Plot the function of the natural logarithm of the exercise
from sympy import symbols
import matplotlib.pyplot as plt
import numpy as np

# Declare the variable x
x = symbols('x')

# Generate values of t
x = np.linspace(0, 100, 1000)

# Define the estimated exponential function
y1 = ____                                              # Fill in

# Plot the function
plt.plot(x, y1)
plt.title('y=ln(x)')
plt.xlabel("x (r*t)")
plt.ylabel("y")
plt.xlim([0,5])
plt.ylim([0,5])
plt.legend(loc='lower right')
plt.grid(True)
plt.show()

