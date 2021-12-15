import mysql.connector as msql
import pandas as pd

conn = msql.connect(host='localhost',
    username='root', 
    password='root',
    database = 'sqlnew')

cur = conn.cursor()

# from tabulate import tabulate

query1 = pd.read_sql_query("select*from student",conn)
# cur.execute(query1)

# print(type(my_cursor))

d = (pd.DataFrame(query1, columns=['ID', 'name', 'CLASS', 'Email', 'gender', 'residence', 'subs']))
print(d)

conn.commit()
conn.close()