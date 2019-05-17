#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 14:43:19 2019

@author: hbagaria
"""

"""

Code Challenge
  Name: 
    Student and Faculty JSON
  Filename: 
    student.json
    faculty.json
  Problem Statement:
    Create a student and Faculty JSON object and get it verified using jsonlint.com
    Write a JSON for faculty profile. 
    The JSON should have profile of minimum 2 faculty members. 
    The profile for each faculty should include below information atleast:

        First Name
        Last Name
        Photo (Just a random url)
        Department 
        Research Areas (can be multiple)
        Contact Details (should include phone number and email id and can have multiple )
   Hint:
       www.jsonlint.com
       
"""
import json
student = """[{
 "firstName" : "Himanshu",
 "lastName" : "Bagaria",
 "photo" : "hello.com/hb",
 "contactDetail" : {
         "phone": "1234567789",
         "email": "bagaria.hb@gmail.com"}
},
{
 "firstName" : "Narayan",
 "lastName" : "Sitapura",
 "photo" : "hello.com/abc",
 "contactDetail" : {
         "phone": "12345674455",
         "email": "sitapura@gmail.com"}
}]"""
    
faculty = """[{
 "firstName" : "sunil",
 "lastName" : "jangir",
 "photo" : "hello.com/456",
 "contactDetail" : {
         "phone": "45645646456",
         "email": "sunil@gmail.com"},
 "Department" = "IT",
 "Research Areas" = ["ML","DL"]
},
{
 "firstName" : "piyush",
 "lastName" : "srivastav",
 "photo" : "hello.com/456",
 "contactDetail" : {
         "phone": "1237894565",
         "email": "piyush@gmail.com"},
 "Department" = "CSE",
 "Research Areas" = ["ML"]
}]"""
    
with open("student.json", "w") as write_file:
    json.dump(student, write_file)
    
with open("faculty.json", "w") as faculty_file:
    json.dump(faculty, faculty_file)
    
