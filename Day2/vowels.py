#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 15:57:35 2019

@author: hbagaria
"""

state_name = [ 'alabama', 'californi', 'oklahoma', 'florida']
vowels = "aeiou"
new_list =[]

for state in state_name:
    strnew = ""
    for char in state:
        if char not in vowels:
            strnew = strnew + char
    new_list.append(strnew)       
print(new_list)
    