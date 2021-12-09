# lets integrate MySQL with python
# initially install package mysql and then import mysql.connector as msql

import mysql.connector as msql #we use msql in further codes

# create connection
# give a name to connection
conn = msql.connect(host='localhost', username='root', password='root')

# next is create cursor :
my_cursor = conn.cursor()

# we want to connect csv file with SQL and edit using python
# firstly, install csv file. we use employees.csv file he

import pandas as pd
import csv

data=pd.read_csv("employees.csv")

print(data)



conn.commit()
conn.close()


