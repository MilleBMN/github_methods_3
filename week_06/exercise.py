#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 17:44:07 2021

@author: millebryske
"""

## assignment is done and only done with "=" (no arrows)
a = 2
# a <- 2 # results in a syntax error
## already assigned variables can be reassigned with basic arithmetic operations
a += 2
print(a)
for index in range(0, 5): # indentation (use tabulation) controls scope of control variables 
    #(no brackets necessary),
    if index == 0: # remember the colon
        value = 0
    else:
        value += index
    print(value)

matrix = np.ones(shape=(5, 5)) # create a matrix of ones
identity = np.identity(5) # create an identity matrix (5x5)
identity[:, 2] = 5 # exchange everything in the second column with 5's

## no dots in names - dots indicate applying a method like the dollar sign $ in R

import matplotlib.pyplot as plt
plt.figure() # create new figure
plt.plot([1, 2], [1, 2], 'b-') # plot a blue line
# plt.show() # show figure
plt.plot([2, 1], [2, 1], 'ro') # scatter plot (red)
# plt.show()
plt.xlabel('a label')
plt.title('a title')
plt.legend(['a legend', 'another legend'])
# plt.show()