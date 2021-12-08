import mysql.connector

conn = mysql.connector.connect(host="localhost",
username = "root",
password = "root",
database = "mydatabase")
#we can print the connection and it will give an object as a result.

my_cursor = conn.cursor()

#we will give a query to create database
# query1 = "create database mydatabase"
# query2 = "show databases"
# query3 = "CREATE TABLE  customer(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))"
# query4 = "show tables"
# query5 = "ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY"
# query6 = "DROP TABLE customer"
# query7 = "INSERT INTO customers(name, address) VALUES(%s, %s)"
# values = [("Swati", "Ambala"),("kushal", "ambala"),("megha","YNR")]
query8 = "select*from customers"

#(if we want to add one row in the last and want the id number, use the following query)
# query9= "INSERT INTO customers(name, address) VALUES(%s, %s)"
# values = ("tiya", "yamunanagar")


# my_cursor.execute(query4)
my_cursor.execute(query8)

# print("1 record inserted, ID:", my_cursor.lastrowid)

for x in my_cursor:
    print(x)

# print(my_cursor.fetchall())
conn.commit()
conn.close()
