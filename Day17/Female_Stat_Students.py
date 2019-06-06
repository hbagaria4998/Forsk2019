#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 15:41:47 2019

@author: hbagaria
"""

"""
Q. (Create a program that fulfills the following specification.)
Female_Stats.Csv

Female_Stat_Students.py

 

Import The Female_Stats.Csv File

The Data Are From N = 214 Females In Statistics Classes At The University Of California At Davi.

Column1 = Student’s Self-Reported Height,

Column2 = Student’s Guess At Her Mother’s Height, And

Column 3 = Student’s Guess At Her Father’s Height. All Heights Are In Inches.

 

Build A Predictive Model And Conclude If Both Predictors (Independent Variables) Are Significant For A Students’ Height Or Not
When Father’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Mother’s Height.
When Mother’s Height Is Held Constant, The Average Student Height Increases By How Many Inches For Each One-Inch Increase In Father’s Height.
"""
# -*- coding: utf-8 -*-
"""

@author: Kunal
"""

# Polynomial Regression

# Importing the libraries
import pandas as pd
import matplotlib.pyplot as plt

# Importing the dataset
dataset = pd.read_csv('Female_Stats.csv')
features = dataset.iloc[:, 1:3].values
labels = dataset.iloc[:, 0].values

#let's first analyze the data
# Visualising the Linear Regression results
#plt.scatter(features[:,1], labels)

# Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg_1 = LinearRegression()
lin_reg_1.fit(features, labels)

prediction = lin_reg_1.predict(features)

x = lin_reg_1.coef_
print('When Father’s Height Is Held Constant, The Average Student Height Increases By '+str(x[0]) +' Inches For Each One-Inch Increase In Mother’s Height.')
print('When Mother’s Height Is Held Constant, The Average Student Height Increases By '+str(x[1]) +' Inches For Each One-Inch Increase In Father’s Height.')


