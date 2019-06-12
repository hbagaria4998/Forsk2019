#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 11:20:54 2019

@author: hbagaria
"""
import pandas as pd
from sqlalchemy import create_engine

# Create your engine.
engine = create_engine('mysql+mysqldb://hbagaria:12345678@db4free.net/hbagariadb')

with engine.connect() as conn, conn.begin():
    data = pd.read_sql_table('online_marketing', conn)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    