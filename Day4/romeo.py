#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 17:23:43 2019

@author: hbagaria
"""

import csv

with open("romeo.txt","r") as fp:
    dict1 ={}
    for line in fp:
        for item in line.split():
            if item in dict1.keys():
                dict1[item] += 1
            else:
                dict1[item] = 1
                
print(dict1)
                
                
         
   