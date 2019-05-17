#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 17:53:20 2019

@author: hbagaria
"""
flag = 1
pattern = " qwertyuiopasdfghjklzxcvbnm"
string = input("Enter a Statement")
for i in pattern:
    if i not in string:
        print("not pangram")
        flag = 0
        break
    else:
        continue
if flag:
    print("pangram")


        
    