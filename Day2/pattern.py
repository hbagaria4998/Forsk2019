#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 17:08:50 2019

@author: hbagaria
"""

num = int(input("Enter a number"))

for i in range(1,num+1):
    print("* "*i) 
    if i == num:
        while True:
            i -= 1
            print("* "*i)
            if i == 0:
                break
        