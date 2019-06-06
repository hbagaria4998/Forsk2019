#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:32:57 2019

@author: hbagaria
"""
"""
Code Challenge:
dataset: BreadBasket_DMS.csv

Q1. In this code challenge, you are given a dataset which has data and time wise transaction on a bakery retail store.
1. Draw the pie chart of top 15 selling items.
2. Find the associations of items where min support should be 0.0025, min_confidence=0.2, min_lift=3.
3. Out of given results sets, show only names of the associated item from given result row wise.
"""

import pandas as pd
from apyori import apriori
import matplotlib.pyplot as plt
from apyori import apriori

dataset = pd.read_csv('BreadBasket_DMS.csv')

list1 = dataset.index[dataset['Item'] == 'NONE'].tolist()
dataset.drop(list1,axis = 0,inplace = True)

x = dataset['Item'].value_counts()
print("Top 15 selling items are : ")
counts = x[:15].values.tolist()
names = x[:15].index.tolist()

plt.pie(counts,labels = names,autopct="%2.2f%%",radius = 3)

item = dataset.groupby('Transaction')['Item'].unique()
item_list = [x.tolist() for x in item]


rules = apriori(item_list, min_support = 0.0025, min_confidence = 0.2, min_lift = 3)

results = list(rules)

for item in results:

    # first index of the inner list
    # Contains base item and add item
    pair = item[0] 
    items = [x for x in pair]
    print("Rule: " + items[0] + " -> " + items[1])

    #second index of the inner list
    print("Support: " + str(item[1]))

    #third index of the list located at 0th
    #of the third index of the inner list

    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")
