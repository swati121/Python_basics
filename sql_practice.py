# lets integrate MySQL with python
# initially install package mysql and then import mysql.connector as msql

import mysql.connector as msql #we use msql in further codes

# create connection
# give a name to connection
conn = msql.connect(host='localhost',
    username='root', 
    password='root',
    database = 'sqlnew')

# next is create cursor :
my_cursor = conn.cursor()

# we want to connect csv file with SQL and edit using python
# firstly, install csv file. we use employees.csv file he

import pandas as pd
import csv

data=pd.read_csv("file.csv")
df1=pd.DataFrame(data)

# print(type(data))

# to connect csv file in sql, we create a query as create table
# query1 = "CREATE TABLE  emp(first_name VARCHAR(255), last_name VARCHAR(255), salary INT, employee_type VARCHAR(255))"

# query to add data into table
# query2 = "INSERT INTO emp(first_name, last_name, salary, employee_type) VALUES(%s, %s, %s, %s)"

# create new database
# query3 = "CREATE DATABASE sqlnew"


# run create table query
# my_cursor.execute(query1)

# insert data from csv to table, we use for loop with itertuple function
# for row in df.itertuples():
#     query2 = "INSERT INTO emp(first_name, last_name, salary, employee_type) VALUES(%s, %s, %s, %s)"
#     val = (row.first_name,row.last_name,row.salary,row.employee_type)
#     my_cursor.execute(query2,val)

# create new database
# query3 = "CREATE DATABASE sqlnew"

# create new table
# query4 = "CREATE TABLE student(ID INT, name VARCHAR(255), CLASS INT, Email VARCHAR(255), gender VARCHAR(255), residence VARCHAR(255), subs VARCHAR(255))"
# my_cursor.execute(query4)

# print(df1)

# insert data using for loop
for row in df1.itertuples():
    query5 = "INSERT INTO student(ID, name, CLASS, Email, gender, residence, subs) VALUES(%s, %s, %s, %s, %s, %s, %s)"
    val1 = (row.User_ID,row.User_Name,row.Class,row.User_Email_ID,row.Gender,row.Residence,row.Subscription)
    my_cursor.execute(query5,val1)


conn.commit()
conn.close()


