#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 14:27:59 2019

@author: hbagaria
"""
"""
Code Challenge 01: (Prostate Dataset)
Load the dataset from given link: 
pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat")

This is the Prostate Cancer dataset. Perform the train test split before you apply the model.

(a) Can we predict lpsa from the other variables?
(1) Train the unregularized model (linear regressor) and calculate the mean squared error.
(2) Apply a regularized model now - Ridge regression and lasso as well and check the mean squared error.

(b) Can we predict whether lpsa is high or low, from other variables?
"""

import numpy as np
import pandas as pd

df = pd.read_csv("http://www.stat.cmu.edu/~ryantibs/statcomp/data/pros.dat",delimiter = ' ')

X = df.iloc[:,:-1].values
y = df.iloc[:,-1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

from sklearn.linear_model import LinearRegression
LR = LinearRegression()
LR.fit(X_train,y_train)
y_pred = LR.predict(X_test)

print ("RSquare Value for Simple Regresssion TEST data is-") 
print (np.round (LR.score(X_test,y_test)*100,2))
print ("RSquare Value for Simple Regresssion TRAIN data is-") 
print (np.round (LR.score(X_train,y_train)*100,2))

from sklearn import metrics  
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred))) 



from sklearn.linear_model import Lasso
from sklearn.linear_model import Ridge
from sklearn.linear_model import ElasticNet

lm_lasso = Lasso() 
lm_ridge =  Ridge() 
lm_elastic = ElasticNet() 


#Fit a model on the train data


lm_lasso.fit(X_train, y_train)
lm_ridge.fit(X_train, y_train)
lm_elastic.fit(X_train, y_train)



print ("RSquare Value for Lasso Regresssion TEST data is-")
print (np.round (lm_lasso.score(X_test,y_test)*100,2))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  

print ("RSquare Value for Ridge Regresssion TEST data is-")
print (np.round (lm_ridge.score(X_test,y_test)*100,2))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  

print ("RSquare Value for Elastic Net Regresssion TEST data is-")
print (np.round (lm_elastic.score(X_test,y_test)*100,2))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  

avg = np.mean(df['lpsa'])
df['lpsa']=df['lpsa'].apply(lambda x : 1 if x>avg else 0)



from sklearn.neighbors import KNeighborsClassifier
kNN = KNeighborsClassifier()
kNN.fit(X_train,y_train)

class_pred = kNN.predict(X_test)

from sklearn.metrics import classification_report
print(classification_report(y_test,class_pred))













































































































































































































































































































