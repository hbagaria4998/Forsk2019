#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:45:34 2019

@author: hbagaria
"""




"""
Code Challenge:
  Name: 
    Bid Plus
  Filename: 
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
"""


from selenium import webdriver


url = "https://bidplus.gem.gov.in/bidlists"
#driver = webdriver.Firefox(executable_path=r'C:/Users/hp/Downloads/geckodriver')
driver = webdriver.Chrome("/usr/bin/chromedriver")

driver.get(url)    # Opening the submission url

a = []
b = []
c = []
d = []
e = []
f = []

for i in range(1,11):
    a1 =  driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a')
    b1 = driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span')
    c1 = driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]/span')
    d1 = driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]/p[2]')
    e1 = driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span')
    f1 = driver.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span')
    
    a.append(a1.text)
    b.append(b1.text)
    c.append(c1.text)
    d.append(d1.text)
    e.append(e1.text)
    f.append(f1.text)

import pandas as pd
from collections import OrderedDict

col_name = ["Position","Team","Weighted Matches","Points","Rating"]
col_data = OrderedDict(zip(col_name,[a,b,c,d,e,]))
df = pd.DataFrame(col_data) 
df.to_csv("gov.csv")
