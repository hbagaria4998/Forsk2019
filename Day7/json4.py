#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 17:36:03 2019

@author: hbagaria
"""

endpoint = "https://requestinspector.com/inspect/01dav68mjap7myfs67963g81xs"

import json
import requests

Host = "http://httpbin.org/post"

data = {"firstname":"dev","language":"English"}

headers = {"Content-Type":"application/json","Content-Length":len(data),"data":json.dumps(data)}

def post_method():
    res1 = requests.post(endpoint,data,headers)
    return res1

print ( post_method().text )

def get_method():
    res2 = requests.get("https://en2vck2hokujx.x.pipedream.net/?firstname=Dev")
    return res2.content

print (get_method())



