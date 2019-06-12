#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 16:11:29 2019

@author: hbagaria
"""
"""
Q1. 

(Click Here To Download Training data File): 
http://openedx.forsk.in/c4x/Forsk_Labs/ST101/asset/Advertisement_training_data.json

(Click Here To Download Test data File):
http://openedx.forsk.in/c4x/Forsk_Labs/ST101/asset/Advertisement_test_data.json


This is the data for local classified advertisements. It has 9 prominent sections: jobs, resumes, gigs, personals, housing, community, services, for-sale and discussion forums. Each of these sections is divided into subsections called categories. For example, the services section has the following categories under it:
beauty, automotive, computer, household, etc.

For a set of sixteen different cities (such as newyork, Mumbai, etc.), we provide to you data from four sections

        for-sale
        housing
        community
        services

and we have selected a total of 16 categories from the above sections.

        activities
        appliances
        artists
        automotive
        cell-phones
        childcare
        general
        household-services
        housing
        photography
        real-estate
        shared
        temporary
        therapeutic
        video-games
        wanted-housing

Each category belongs to only 1 section.

About Data:

        city (string) : The city for which this Craigslist post was made.
        section (string) : for-sale/housing/etc.
        heading (string) : The heading of the post.

each of the fields have no more than 1000 characters. The input for the program has all the fields but category which you have to predict as the answer.

A total of approximately 20,000 records have been provided to you, proportionally represented across these sections, categories and cities. The format of training data is the same as input format but with an additional field "category", the category in which the post was made.

Task:

    Given the city, section and heading of an advertisement, can you predict the category under which it was posted?
    Also Show top 5 categories which has highest number of posts
"""

import pandas as pd
import numpy as np
import requests

url1 = "http://openedx.forsk.in/c4x/Forsk_Labs/ST101/asset/Advertisement_training_data.json"
url2 = "http://openedx.forsk.in/c4x/Forsk_Labs/ST101/asset/Advertisement_test_data.json"

train = requests.get(url1)
test =  requests.get(url2)

train = train.text
test = test.text

train = pd.read_json(train,lines = True)
test = pd.read_json(test,lines = True)


features_train = train.iloc[:,1:].values
labels_train = train.iloc[:,0].values

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
labels_train = le.fit_transform(labels_train)


features_train = pd.DataFrame(features_train)

le2 = LabelEncoder()
features_train.iloc[:,0] = le2.fit_transform(features_train.iloc[:,0])
test.iloc[:,0] = le2.transform(test.iloc[:,0])

le3 = LabelEncoder()
features_train.iloc[:,2] = le3.fit_transform(features_train.iloc[:,2])
test.iloc[:,2] = le3.transform(test.iloc[:,2])

df = features_train.iloc[:,[0,2]]
df2 = test.iloc[:,[0,2]]

from sklearn.preprocessing import OneHotEncoder
ohe1 = OneHotEncoder(categorical_features=[0,1])
df= ohe1.fit_transform(df).toarray()
df2= ohe1.fit_transform(df2).toarray()

df =df[:,1:-1]
df2 =df2[:,1:-1]


import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

corpus = []
for i in range(0, 20217):
    review = re.sub('[^a-zA-Z]', ' ', features_train[1][i])
    review = review.lower()
    review = review.split()
    review = [word for word in review if not word in set(stopwords.words('english'))]
    
    #lem = WordNetLemmatizer() #Another way of finding root word
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review]
    #review = [lem.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)
    
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
features = cv.fit_transform(corpus).toarray()

X = np.concatenate((features,df),axis=1)

corpus1 = []
for i in range(0, 15370):
    review = re.sub('[^a-zA-Z]', ' ', test['heading'][i])
    review = review.lower()
    review = review.split()
    review = [word for word in review if not word in set(stopwords.words('english'))]
    
    #lem = WordNetLemmatizer() #Another way of finding root word
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review]
    #review = [lem.lemmatize(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus1.append(review)
    

features1 = cv.transform(corpus1).toarray()

Y = np.concatenate((features1,df2),axis=1)

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier()
classifier.fit(X, labels_train)
labels_pred = classifier.predict(Y)

le.inverse_transform(labels_pred)





































