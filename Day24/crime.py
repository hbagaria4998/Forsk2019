#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:29:13 2019

@author: hbagaria
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('crime_data.csv')
features = dataset.iloc[:,1:].values

from sklearn.decomposition import PCA
pca = PCA(n_components = 2)

features = pca.fit_transform(features)
explained_variance = pca.explained_variance_ratio_

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 3 ,init ='k-means++',random_state = 0)
y_kmeans = kmeans.fit_predict(features)

plt.scatter(features[y_kmeans ==0,0],features[y_kmeans == 0,1],s= 100,c = 'red',label = 'Cluster 1')
plt.scatter(features[y_kmeans ==1,0],features[y_kmeans == 1,1],s= 100,c = 'blue',label = 'Cluster 2')
plt.scatter(features[y_kmeans ==2,0],features[y_kmeans == 2,1],s= 100,c = 'green',label = 'Cluster 3')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s = 300,c = 'yellow',label = 'Centroids')
plt.legend()
plt.show()