#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:21:52 2019

@author: hbagaria
"""

"""Code Challenge -
Data: "data.csv"

This data is provided by The Metropolitan Museum of Art Open Access
1. Visualize the various countries from where the artworks are coming.
2. Visualize the top 2 classification for the artworks
3. Visualize the artist interested in the artworks
4. Visualize the top 2 culture for the artworks
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("data.csv")

ser = dataset['Country'].value_counts()

country_list = list(ser.keys())
values = list(ser.values)

pie = plt.pie(values,autopct='%1.1f%%')
plt.legend(pie[0],country_list,loc = "upper corner",bbox_to_anchor = (1,1))


