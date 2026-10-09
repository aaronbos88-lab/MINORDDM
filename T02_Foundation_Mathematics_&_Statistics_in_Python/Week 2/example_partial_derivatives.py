# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 18:36:07 2024

@author: rbaia
"""

# Example computing partial derivatives

from sympy import symbols, diff
from sympy.plotting import plot3d

# Declare the symbols used
x, y = symbols('x y')

# Specify the function
f = 2*x**3 + 3*y**3

# Compute the derivatives w.r.t. x and y
dx_f = diff(f, x)
dy_f = diff(f, y)

# Print the result
print(dx_f)
print(dy_f)

# Plot the graph
plot3d(f)