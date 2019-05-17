#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:37:20 2019

@author: hbagaria
"""
#Taking scores from user
A1 = int(input("Score of assignment 1"))
A2 = int(input("Score of assignment 2"))
A3 = int(input("Score of assignment 3"))

E1 = int(input("Score of exam 1"))
E2 = int(input("Score of exam 2"))

#Formula
weighted_score = ( A1 + A2 + A3 )*0.1 + (E1 + E2 ) * 0.35

#Displaying results
print(weighted_score)

