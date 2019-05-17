#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:35:56 2019

@author: hbagaria
"""

"""
Code Challenge
  Name: 
    Zoo Management
  Filename: 
    zoo.py
  Problem Statement:
    Create different functions to :
    read the zoo.csv file using readlines and print them
    Print in list of animals in groups (elephant / tiger / lion / zebra / kangaroo)
    print the total number of water need by elephant / tiger / lion / zebra / kangaroo
    print the total number of water needed by all the animals    
"""
import csv
def readandprint():
    with open("zoo.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        # row has the list of all columns
        for row in csv_reader:
            print (row)
    
def printanimal():
    with open("zoo.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        # row has the list of all columns
        set1 = set()
        for row in csv_reader:
            if row[0] =="elephant":
                set1.add("elephant")
            elif row[0] =="tiger":
                set1.add("tiger")
            elif row[0] =="lion":
                set1.add("lion")
            elif row[0] =="zebra":
                set1.add("zebra")
            elif row[0] =="kangaroo":
                set1.add("kangaroo")
        print(set1)
            
            
             
                 
            
def totalwater():
      with open("zoo.csv") as csv_file:
          csv_reader = csv.reader(csv_file, delimiter=",")
          # row has the list of all columns
          next(csv_reader)
          num = 0
          for row in csv_reader:
              num =int(row[-1]) +num
          print(num)
            
def seperatewaterneed():
       with open("zoo.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            next(csv_reader)
            # row has the list of all columns
            enum = 0
            tnum = 0
            lnum = 0
            znum = 0
            knum = 0
            for row in csv_reader:
                if row[0] =="elephant":
                    enum += int(row[-1])
                    
                elif row[0] =="tiger":
                    tnum += int(row[-1])
                elif row[0] =="lion":
                    lnum += int(row[-1])
                elif row[0] =="zebra":
                    znum += int(row[-1])
                elif row[0] =="kangaroo":
                    knum += int(row[-1])
                else:
                    break
            print("Water needed by elephant is "+str(enum))
            print("Water needed by tiger is "+str(tnum))
            print("Water needed by lion is "+str(lnum))
            print("Water needed by zebra is "+str(znum))
            print("Water needed by kangroo is "+str(knum))
             
    
    
    
    
