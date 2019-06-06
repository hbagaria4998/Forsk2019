#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 14:46:39 2018

@author: hbagaria
"""
"""
Q1. (Create a program that fulfills the following specification.)
deliveryfleet.csv


Import deliveryfleet.csv file

Here we need Two driver features: mean distance driven per day (Distance_feature) and the mean percentage of time a driver was >5 mph over the speed limit (speeding_feature).

    Perform K-means clustering to distinguish urban drivers and rural drivers.
    Perform K-means clustering again to further distinguish speeding drivers from those who follow speed limits, in addition to the rural vs. urban division.
    Label accordingly for the 4 groups.

"""

import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('deliveryfleet.csv')
features = dataset.iloc[:,-2:].values


from sklearn.cluster import KMeans
wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters = i,init = 'k-means++',random_state = 0)
    kmeans.fit(features)
    wcss.append(kmeans.inertia_)
    



plt.plot(range(1,11),wcss)
plt.title('The Elbow Method')
plt.xlabel('Numbers of Clusters')
plt.ylabel('wcss')
    

kmeans = KMeans(n_clusters = 2 ,init ='k-means++',random_state = 0)
y_kmeans = kmeans.fit_predict(features)

plt.scatter(features[y_kmeans ==0,0],features[y_kmeans == 0,1],s= 100,c = 'red',label = 'Cluster 1')
plt.scatter(features[y_kmeans ==1,0],features[y_kmeans == 1,1],s= 100,c = 'blue',label = 'Cluster 2')
plt.scatter(features[y_kmeans ==2,0],features[y_kmeans == 2,1],s= 100,c = 'green',label = 'Cluster 3')
plt.scatter(features[y_kmeans ==3,0],features[y_kmeans == 3,1],s= 100,c = 'violet',label = 'Cluster 4')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s = 300,c = 'yellow',label = 'Centroids')
plt.legend()
plt.show()

5558