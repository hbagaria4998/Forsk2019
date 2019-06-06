#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 17:07:57 2019

@author: hbagaria
"""
"""
Code Challenges 02: (House Data)
This is kings house society data.
In particular, we will: 
• Use Linear Regression and see the results
• Use Lasso (L1) and see the resuls
• Use Ridge and see the score
"""

import numpy as np
import pandas as pd

df = pd.read_csv('kc_house_data.csv')

df['date'] = df['date'].apply(lambda x : int(x[:4]))






