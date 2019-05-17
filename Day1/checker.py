#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 16:50:59 2019

@author: hbagaria
"""
number = 0
while number<7:
    if number%2 == 0:
        print("* "*8)
    else:
        print(" *"*8)
    number += 1