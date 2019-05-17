#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:30:50 2019

@author: hbagaria
"""
"""
Code Challenge
  Name: 
    JSON Parser
  Filename: 
    json.py
  Problem Statement:
    Get me the other details about the city
        Latitude and Longitude
        Weather Condition
        Wind Speed
        Sunset Rise and Set timing
"""

import requests

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Jaipur"
url3 = "&appid=e9185b28e9969fb7a300801eb026de9c"

url = url1 + url2 + url3
print (url)


response = requests.get(url)

jsondata = response.json()

print("Latitude : " + str(jsondata['coord']['lat']))
print("Longitude : " + str(jsondata['coord']['lon']))
print("Whether Condition : " + str(jsondata['weather'][0]['main']))
print("Wind Speed : " + str(jsondata['wind']['speed']))
print("Sunrise : " + str(jsondata['sys']['sunrise']))
print("Sunset : " + str(jsondata['sys']['sunset']))
