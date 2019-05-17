#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 18:23:32 2019

@author: hbagaria
"""

userInput = input("Enter a statement : ")
def reverse(ui):
    newList = list(userInput)
    newList = newList[::-1]
    hello ="".join(newList)
    return hello
    
reverse(userInput)  
    
    