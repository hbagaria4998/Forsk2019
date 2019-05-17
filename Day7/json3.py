#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:12:59 2019

@author: hbagaria
"""

"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
    
"""


import requests

url = "https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=88a6a90103b89d378fd7"
response = requests.get(url)

url1 = "http://data.fixer.io/api/latest?access_key=3aec6973baf48f28a2254c0a1f6a97b2"
response = requests.get(url1)

jsondata1 = response.json()
print("Rate : " + str(jsondata1['rates']['INR']))