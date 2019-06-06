#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 15:04:56 2018

@author: hbagaria
"""
"""
Q1. (Create a program that fulfills the following specification.)
PastHires.csv


Here, we are building a decision tree to check if a person is hired or not based on certain predictors.

Import PastHires.csv File.

scikit-learn needs everything to be numerical for decision trees to work.

So, use any technique to map Y,N to 1,0 and levels of education to some scale of 0-2.

    Build and perform Decision tree based on the predictors and see how accurate your prediction is for a being hired.

Now use a random forest of 10 decision trees to predict employment of specific candidate profiles:

    Predict employment of a currently employed 10-year veteran, previous employers 4, went to top-tire school, having Bachelor's Degree without Internship.
    Predict employment of an unemployed 10-year veteran, ,previous employers 4, didn't went to any top-tire school, having Master's Degree with Internship.
"""

#importing libraries
import numpy as np
import pandas as pd

#load dataset
dataset = pd.read_csv('PastHires.csv')
X = dataset.iloc[:,:-1].values 
Y = dataset.iloc[:, -1].values

#Y = np.array(Y).reshape(-1,1)
#apply label encoding
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
X[:,1] = labelencoder.fit_transform(X[:,1])
X[:,3] = labelencoder.fit_transform(X[:,3])
X[:,4] = labelencoder.fit_transform(X[:,4])
X[:,5] = labelencoder.fit_transform(X[:,5])
Y = labelencoder.fit_transform(Y)

#apply decision tree classifier
from sklearn.tree import DecisionTreeClassifier
DTC = DecisionTreeClassifier(random_state = 0)
DTC.fit(X,Y)

#defining person1
person1 = [10,1,4,0,1,0]
person1 = np.array(person1).reshape(1,-1)

#defining person2
person2 = [10,0,4,1,0,1]
person2 = np.array(person2).reshape(1,-1)


#apply random forest classifier
from sklearn.ensemble import RandomForestClassifier
RFC = RandomForestClassifier(n_estimators=10,random_state=0)
RFC.fit(X,Y)

#results by decision tree
person1_pred_dtc = DTC.predict(person1)
person2_pred_dtc = DTC.predict(person2)

#results by random forest
person1_pred_rfc = RFC.predict(person1)
person2_pred_rfc = RFC.predict(person2)






