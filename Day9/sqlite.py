#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 14:43:19 2019

@author: hbagaria
"""

"""

Code Challenge 1
Write a python code to insert records to a mongo/sqlite/MySQL database 
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.
"""



import sqlite3
from pandas import DataFrame

#os.chdir('/Users/sylvester/Desktop/Database and Python/Python/')

# File based database ( connects if exits or creates a new one if it does not exists ) 
conn = sqlite3.connect ( 'db_University.db' )


# creating cursor
c = conn.cursor()


# STEP 1
# www.sqlite.org/datatype3.html
c.execute ("""CREATE TABLE students(
          Student_Name TEXT,
          Student_Age INTEGER ,
          Student_Roll_no INTEGER,
          Student_Branch TEXT
          )""")


# STEP 2
c.execute("INSERT INTO students VALUES ('Himanshu',20, 001, 'IT')")
c.execute("INSERT INTO students VALUES ('Narayan',20, 002, 'IT')")
c.execute("INSERT INTO students VALUES ('HimanshuS',22, 003, 'CSE')")
c.execute("INSERT INTO students VALUES ('Himansh',22, 004, 'ME')")
c.execute("INSERT INTO students VALUES ('Him',45, 005, 'CE')")


# STEP 3
c.execute("SELECT * FROM students")
# "SELECT * FROM employees WHERE last = 'Fernandes' "



# STEP 4
# returns one or otherwise None as a tuple
print ( c.fetchone()) 

# returns one or otherwise None as a tuple
print ( c.fetchmany(2)) 

# returns a list of tuples
print ( c.fetchall() )


# Since now the cursor has read all the rows and we are at End
# So again fetching the records from the database
c.execute("SELECT * FROM students")


# STEP 5
df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["Student_Name","Student_Age","Student_Roll_no","Student_Branch"]


# STEP 6
# commits the current transaction 
conn.commit()

# STEP 7
# closing the connection 
conn.close()

