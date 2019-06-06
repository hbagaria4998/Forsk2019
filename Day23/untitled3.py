#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 17:26:36 2019

@author: hbagaria
"""
"""
Code Challenge:
Datset: Market_Basket_Optimization.csv
Q2. In today's demo sesssion, we did not handle the null values before fitting the data to model, remove the null values from each row and perform the associations once again.
Also draw the bar chart of top 10 edibles.
"""
import pandas as pd
from apyori import apriori

# Data Preprocessing
dataset = pd.read_csv('Market_Basket_Optimisation.csv', header = None)



transactions = []

for i in range(0, 7501):
    #transactions.append(str(dataset.iloc[i,:].values)) #need to check this one
    transactions.append([str(dataset.values[i,j]) for j in range(0, 20) if str(dataset.values[i,j]) != 'nan'])
#    
#for i in range(0,7500):
#    for j in range(0,19):
#        if transactions[i][j] != 'nan':
#            continue
#        else:
#            transactions[i].remove('nan')
#            
            
          
            
        
            
        
            
            
            
    
