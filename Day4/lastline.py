#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 18:00:49 2019

@author: hbagaria
"""

"""
Code Challenge
  Name: 
    Last Line
  Filename: 
    lastline.py
  Problem Statement:
    Ask the user for the name of a text file. 
    Display the final line of that file.
    Think of ways in which you can solve this problem, 
    and how it might relate to your daily work with Python.
"""
filename = input("Enter the name of a file : ")
list1 = []
with open(filename,"r") as fp:
    for line in fp:
        list1.append(line)
    print(list1[-1])
    
        
