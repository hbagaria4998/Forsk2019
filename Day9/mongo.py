#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 17:31:43 2019

@author: hbagaria
"""


import pymongo



client = pymongo.MongoClient("mongodb://hbagaria:hello1234@clusterhb-shard-00-00-kzgrq.mongodb.net:27017,clusterhb-shard-00-01-kzgrq.mongodb.net:27017,clusterhb-shard-00-02-kzgrq.mongodb.net:27017/test?ssl=true&replicaSet=Clusterhb-shard-0&authSource=admin&retryWrites=true")










mydb = client.hbdb

def add_employee(idd, first, last, pay):
    #unique_employee = mydb.employees.find_one({"id":idd})
    #if unique_employee:
    #    return "Employee already exists"
    #else:
    mydb.hello.insert_one(
            {
            "id" : idd,
            "first" : first,
            "last" : last,
            "pay" : pay
            })
    return "Employee added successfully"


def fetch_all_employee():
    user = mydb.hello.find()
    for i in user:
        print (i)




add_employee(1,'Sylvester', 'Fernandes', 50000)
add_employee(2,'Yogendra', 'Singh', 70000)
add_employee(3,'Rohit', 'Mishra', 30000)
add_employee(4,'Kunal', 'Vaid', 30000)
add_employee(5,'Devendra', 'Shekhawat', 30000)

fetch_all_employee()

h!manshu1998