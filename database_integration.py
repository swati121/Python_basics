import mysql.connector

# to use previously created databases:
conn = mysql.connector.connect(host="localhost",username = "root", password = "root",
database = "db1")

#we want a cursor to execute
my_cursor = conn.cursor()

#we want to create a database and give the query
# query = "create database db1"
# query = "show databases"
# query = "create table student(name VARCHAR(255), age INT)"
# query = "insert into student(name,age) VALUES (%s, %s)"
#here %s is the placeholder.
values = [("swati", 27),
("kushal",28),
("megha",25)
]

query = "select*from student"

my_cursor.execute(query)

# for x in my_cursor:
    # print(x)


# to create a list of all databases name. use fetchall function.
print(my_cursor.fetchall())
conn.commit()
conn.close()

