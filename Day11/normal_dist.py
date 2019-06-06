#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 17:29:35 2019

@author: hbagaria
"""

"""
Code Challenge
  Name: 
    Normally Distributed Random Data
  Filename: 
    normal_dist.py
  Problem Statement:
    Create a normally distributed random data with parameters:
    Centered around 150.
    Standard Deviation of 20.
    Total 1000 data points.
    
    Plot the histogram using matplotlib (bucket size =100) and observe the shape.
    Calculate Standard Deviation and Variance. 
"""

import numpy as np
import matplotlib.pyplot as plt
data = np.random.normal(150.0, 20.0, 1000)

plt.hist(data,100)

import statistics 
print("Standard Deviation of sample is % s " % (statistics.stdev(data))) 
print("Variance of sample is " + str(np.var(data))) 

