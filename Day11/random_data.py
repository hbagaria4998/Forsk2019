#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:50:35 2019

@author: hbagaria
"""

"""
Code Challenge
  Name: 
    Random Data
  Filename: 
    random_data.py
  Problem Statement:
    Create a random array of 40 integers from 5 - 15 using NumPy. 
    Find the most frequent value with and without Numpy.
  Hint:
      Try to use the Counter class
      
"""

import numpy as np
nparray = np.random.randint(5,15,40,"int_")
mode1 = np.bincount(nparray).argmax()
print("Mode with numpy : " + str(mode1))
from collections import Counter
mode2 = Counter(nparray.tolist()).most_common(1)
print("Mode with counter : " + str(mode2[0][0]))

arr = np.array([1,1,1,2,2,2,3,3])
mode2 = Counter(arr.tolist()).most_common(3)
