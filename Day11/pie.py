#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 17:47:25 2019

@author: hbagaria
"""
"""
Code Challenge

https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area

Scrap the data from State/Territory and National Share (%) columns for top 6 states basis on National Share (%). 
Create a Pie Chart using MatPlotLib and explode the state with largest national share %.
"""

from selenium import webdriver


url = "https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area"
#driver = webdriver.Firefox(executable_path=r'C:/Users/hp/Downloads/geckodriver')
driver = webdriver.Chrome("/usr/bin/chromedriver")

driver.get(url) 

states = []
nationalShare = []
for i in range(1,7):
    state =  driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr['+str(i)+']/td[2]/a')
    ns = driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr['+str(i)+']/td[5]')

    states.append(state.text)
    nationalShare.append(ns.text)
    
import matplotlib.pyplot as plt
plt.pie(x = nationalShare,labels=states)
