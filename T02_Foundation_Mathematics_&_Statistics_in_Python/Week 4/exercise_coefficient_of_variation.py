# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 08:26:19 2024

@author: rbaia
"""

# Computing the coefficient of variation for the minor survey data

import numpy as np

# Specify the survey data
data = ___                  # Specify your data


# Lambda is a keyword in Python for defining an anonymous function. 
# Contrary to the def f(x) function, it does not have a return keyword. 
# The anonymous function will automatically return the result of the expression in the 
# function once it is executed. You can use it for making simple expressions. So with 
# cv(data[‘age’]) in the cv function we defined, we replace x by the data from the column age

cv = lambda x: ___          # Insert the function to compute CV
                            # Should you make a correction with ddof=1 when computing the std?

# Compute cv for the variables
cv_1 = cv(data['___'])
cv_2 = cv(data['___'])

# Print the results
print('CV ___:', cv_1)
print('CV ___:', cv_2)