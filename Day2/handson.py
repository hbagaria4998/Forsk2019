#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  8 08:44:25 2019

@author: hbagaria
"""
#hands on 1
list1 = []
for i in range(1,11):
    list1.append(i)
    
#hands on 2
def leapyear(year):
    if year%4 == 0:
        return True
    else:
        return False
    
#hands on 3
days31 = (1,3,5,7,8,10,12)
days30 = (4,6,9,11)
days28 = (2,)       
def days_in_month(month):
    if month in days31:
        statement = "This month has 31 days"
    elif month in days30:
        statement = "This month has 30 days"
    elif month in days28:
        statement = "This month has 28 days"
    else:
        statement = "Enter valid no."
    return statement
    
    