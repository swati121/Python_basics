import mysql.connector

conn = mysql.connector.connect(host="localhost",
user = "root",
password = "root",
database = "classicmodels")

cur = conn.cursor()

# query1 = "show tables"
# query2 = "select*from customers"
# query3 = "desc payments"
# query4 = "INSERT INTO payments(customerNumber, checkNumber, paymentDate, amount) VALUES(%s,%s,%s,%s)"
# values1 = (497,"UN349867", "2005-2-5", 53192.89)
# query5 = "select count(distinct country) from customers"
# query6 = "select * from customers where country = 'Canada'"
# query7 = "select count(country) from customers where country = 'Germany'"
# query8 = "select distinct customerNumber from payments"
# query9 = "select sum(amount) from payments where customerNumber='298' or customerNumber ='489'"
# query10 = "select * from payments where customerNumber = '447'"
# query11 = "select distinct productCode from orderdetails"
# query12 = "select sum(quantityOrdered) from orderDetails where productCode='S700_3505'"
# query13 = "SELECT * FROM Customers ORDER BY Country, CustomerName"
query14 = "SELECT * FROM customers ORDER BY country ASC, customerName DESC"

cur.execute(query14)

for x in cur:
    print(x)

conn.commit()
conn.close()