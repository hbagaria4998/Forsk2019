#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:20:24 2019

@author: hbagaria
"""

"""
Code Challenge 

Find the mean, median, mode, and range for the following list of values:
13, 18, 13, 14, 13, 16, 14, 21, 13


Answer : Mean = 15, Median = 14 , Mode = 13 , Range = 21 - 13 = 8
"""
import numpy as np
list1 = [13, 18, 13, 14, 13, 16, 14, 21, 13]

nplist1 = np.array(list1)

print("Mean : " + str(np.mean(nplist1)))
print("Median : " + str(np.median(nplist1)))


mode = np.bincount(nplist1).argmax()
print("Mode : " + str(mode))

r = np.max(nplist1) - np.min(nplist1)
print("Range : " + str(r))
