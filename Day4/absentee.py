#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:57:02 2019

@author: hbagaria
"""

"""
Code Challenge
  Name: 
    Create a list of absentee
  Filename: 
    absentee.py
  Problem Statement:
    Make a program that create a file absentee.txt
    The program should take max 25 students name one by one
    When the user enter a blank line, it should terminate the input
    Store all the name of students in the file    
    Once all the students names have been entered, it should display the list
    
"""

absentee = open("absentee.txt","w")
num  = 1
while num <=25:
    name = input("enter a name : ")
    if name != "":
        absentee.write(name)
        absentee.write("\n")
        num +=1
    else:
        break
absentee.close()   
    
     
    
absenteeOpen = open("absentee.txt","r")   
print(absenteeOpen.read())
    
absentee.close()