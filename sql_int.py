import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user = "root",
    password = "root",
    database = "new"
)
cursor1 = conn.cursor()

# query1 = "CREATE DATABASE new"
# query2 = "show databases"
# query3 = "create table students(ID INT NOT NULL AUTO_INCREMENT, s_id INT NOT NULL, name VARCHAR(255), class INT, subject VARCHAR(255), PRIMARY KEY (ID))"
# query4 = "INSERT INTO students(s_id, name, class, subject) values(%s, %s, %s, %s)"
# values1 = [(1,"swati",11,"science"),
# (2,"kushal", 12, "maths"),
# (3, "palak", 11, "english"),
# (4, "lakshay", 9, "hindi")]
# query5 = "select*from students"
# query6 = "create table fees(ID INT NOT NULL AUTO_INCREMENT, s_id INT NOT NULL, name VARCHAR(255), month VARCHAR(255), status TINYINT NOT NULL, PRIMARY KEY(ID))"
# query7 = "INSERT INTO fees(s_id, name, month, status) values(%s, %s, %s, %s)"
# values2 = [(1,"swati","Jan",1),
# (1,"swati", "Feb", 0),
# (1,"swati", "Mar", 1),
# (2, "kushal", "Jan",1),
# (2, "kushal", "Feb",1),
# (2, "kushal", "Mar",1),
# (3, "palak", "Jan", 0),
# (3, "palak", "Feb", 1),
# (3, "palak", "Mar", 1),
# (4, "lakshay", "Jan", 1),
# (4, "lakshay", "Feb", 1),
# (4, "lakshay", "Mar", 1)]
# query8 = "select*from fees"
# query9 = "create table residence(ID INT NOT NULL AUTO_INCREMENT, s_id INT NOT NULL, name VARCHAR(255), residence VARCHAR(255), PRIMARY KEY(ID))"
# query10 = "INSERT INTO residence(s_id, name, residence) values(%s, %s, %s)"
# values3 = [(1,"swati", "hostel"),
# (2,"kushal","Day scholar"),
# (3, "palak","Day Boarding"),
# (4, "lakshay", "hostel"),
# (5, "lakshay", "day scholar")]
query11 = "select*from residence"

# cursor1.executemany(query10, values3)
cursor1.execute(query11)

for x in cursor1:
    print(x)


conn.commit()
conn.close() 

