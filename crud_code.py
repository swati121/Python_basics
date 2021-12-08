import mysql.connector

#function to add data in classname table
def insert_data(name):
    myconn = mysql.connector.connect(host="localhost", username = "root", password = "root", database = "db1")
    mycursor = myconn.cursor()
    query1 = "INSERT INTO classname(name) VALUES(%s)"
    mycursor.execute(query1,(name,))
    myconn.commit()
    myconn.close()

#function to update data in classname table
def update_data(ID):
    myconn = mysql.connector.connect(host="localhost", username = "root", password = "root", database = "db1")
    mycursor = myconn.cursor()
    name = input("Enter your new class name : ")
    query2 = "UPDATE classname SET name = %s WHERE ID = %s"
    mycursor.execute(query2, (name, ID,))
    myconn.commit()
    myconn.close()

#function to delete data in classname table
# def delete_data(ID):
#     myconn = mysql.connector.connect(host="localhost", username = "root", password = "root", database = "db1")
#     mycursor = myconn.cursor()
#     query3 = "UPDATE classname SET name = %s WHERE ID = %s"
#     mycursor.execute(query2, (name, ID,))
#     myconn.commit()
#     myconn.close()


