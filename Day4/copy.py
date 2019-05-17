#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 14:44:32 2019

@author: hbagaria
"""

"""
Code Challenge
  Name: 
    copy command
  Filename: 
    copy.py
  Problem Statement:
    Make a program that create a copy of a file    
"""

file1 = open("hello.txt","w")
file1.write("hello")
file1 = open("hello.txt","r")
line = file1.read()


newFile = open("new.txt","w")
newFile.write(line)

file1.close
newFile.close

