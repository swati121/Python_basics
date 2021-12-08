import mysql.connector
import crud_code

conn = mysql.connector.connect(host="localhost",
username = "root",
password = "root",
database = "db1")

my_cursor = conn.cursor()

#we want to add/update/delete the values from a MySQL table using python. we will give a user menu to opt for a choice.
print("user menu options:")
print("1. Classname")
print("2. Section")
print("3. Students")
print("4. Exit the application")
choice = int(input("Enter the table number you want to edit : "))
if choice == 1:
    print("user menu options:")
    print("1. Add Data")
    print("2. Update Data")
    print("3. Delete Data")
    print("4. Search Data")
    print("5. Go to previous menu")
    choice1 = int(input("Enter the option you want to perform : "))
    if choice1 ==1:
        name = input("Enter your class name : ")
        crud_code.insert_data(name)
    elif choice1 ==2:
        ID = int(input("Enter your ID: "))
        crud_code.update_data(ID)
    elif choice1 ==3:
        pass
    elif choice1 ==4:
        pass
    elif choice1 ==5:
        print("go back")
elif choice == 2:
    pass
elif choice == 3:
    pass
else:
    print("exit")

conn.commit()
conn.close()