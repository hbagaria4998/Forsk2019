#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 16:51:24 2019

@author: hbagaria
"""

"""
Code Challenge: Simple Linear Regression

  Name: 
    Box Office Collection Prediction Tool
  Filename: 
    Bahubali2vsDangal.py
  Dataset:
    Bahubali2vsDangal.csv
  Problem Statement:
    It contains Data of Day wise collections of the movies Bahubali 2 and Dangal 
    (in crores) for the first 9 days.
    
    Now, you have to write a python code to predict which movie would collect 
    more on the 10th day.
  Hint:
    First Approach - Create two models, one for Bahubali and another for Dangal
    Second Approach - Create one model with two labels
"""
import pandas as pd  
import numpy as np  

dataset = pd.read_csv('Bahubali2_vs_Dangal.csv')

features = dataset.iloc[:, 0:1].values  
labelsbahubali = dataset.iloc[:,1].values 
labelsDangal = dataset.iloc[:,2].values
labels = dataset.iloc[:,1:3]

from sklearn.linear_model import LinearRegression  
regressor1 = LinearRegression()  
regressor1.fit(features, labelsbahubali) 


labels_pred = regressor1.predict(features)
bahubali_day_10 = [10]
bahubali_day_10 = np.array(bahubali_day_10).reshape(1,-1)

regressor1.predict(bahubali_day_10)

regressor2 = LinearRegression()
regressor2.fit(features,labelsDangal)

Dangal_day_10 = [10]
Dangal_day_10 = np.array(Dangal_day_10).reshape(1,-1)
regressor2.predict(Dangal_day_10)

regressor3 = LinearRegression()
regressor3.fit(features,labels)
day_10 = [10]
day_10 = np.array(day_10).reshape(1,-1)
regressor3.predict(day_10)



