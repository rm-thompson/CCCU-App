#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: rm-thompson
"""
import numpy as np

# Example arrays
A = np.ones((3,3), int) # 3x3 array of ones
B = np.array([[1,0,0],
              [0,1,0],
              [1,0,1]])

def matrix_multiplication(A,B):
    C = np.zeros((A.shape[0],B.shape[1])) # Create an empty matrix to populate
    for n in range(C.shape[0]):    # For every row in C
        for m in range(C.shape[1]):  # For every column in C
            for k in range(A.shape[1]):  # For each element along row in A
                C[n][m] += A[n][k] * B[k][m] 
    return C
    
'''
Compare how long the above function takes to compute compared to A@B:
    
In an IPython console, run the magic commands

%timeit A@B

and

%timeit matrix_multiplication(A,B)

How do the outputs compare?
'''