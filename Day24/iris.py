#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:14:14 2019

@author: hbagaria
"""
"""

Q2. (Create a program that fulfills the following specification.)

The iris data set consists of 50 samples from each of three species of Iris flower (Iris setosa, Iris virginica and Iris versicolor).



    Four features were measured from each sample: the length and the width of the sepals and petals, in centimetres (iris.data).
    Import the iris dataset already in sklearn module using the following command:\


from sklearn.datasets import load_iris
iris = load_iris()
iris=iris.data


Reduce dimension from 4-d to 2-d and perform clustering to distinguish the 3 species.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
iris_data = load_iris()
features=iris_data.data
labels = iris_data.target

features = pd.DataFrame(features)
labels = pd.DataFrame(labels)


from sklearn.decomposition import PCA
pca = PCA(n_components = 2)
features = pca.fit_transform(features)

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 3 ,init ='k-means++',random_state = 0)
y_kmeans = kmeans.fit_predict(features)


plt.scatter(features[y_kmeans ==0,0],features[y_kmeans == 0,1],s= 100,c = 'red',label = 'Cluster 1')
plt.scatter(features[y_kmeans ==1,0],features[y_kmeans == 1,1],s= 100,c = 'blue',label = 'Cluster 2')
plt.scatter(features[y_kmeans ==2,0],features[y_kmeans == 2,1],s= 100,c = 'green',label = 'Cluster 3')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s = 300,c = 'yellow',label = 'Centroids')
plt.legend()
plt.show()





