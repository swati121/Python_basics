import tkinter as tk
from tkinter import ttk
import mysql.connector
form_win = tk.Tk()
form_win.title("SQL DB")

conn = mysql.connector.connect(host="localhost",
username = "root",
password = "root",
database = "db1")

my_cursor = conn.cursor()

#create labels - ID, name, age, city, state, country, school
labels = ["Enter your ID : ", "Enter your name : ", "Enter your class : ", "Please specify your email : "]

for x in range(len(labels)):
    cur_label = "label"+str(x)
    cur_label = ttk.Label(form_win, text = labels[x])
    cur_label.grid(row = x, column =0, sticky = tk.W, padx = 5, pady = 5)

#create entrybox
user_info = {
    "ID" : tk.IntVar(),
    "name" : tk.StringVar(),
    "class" : tk.IntVar(),
    "email" : tk.StringVar(),
}

counter = 0
for i in user_info:
    cur_box = "entry" + i #entryID, #entryname
    cur_box = ttk.Entry(form_win, width = 20, textvariable = user_info[i])
    cur_box.grid(row = counter, column=1, padx = 5, pady = 5)
    counter +=1


# create submit button
#write the data into SQL file

def sql_db():
    userid = user_info['ID'].get()
    username = user_info['name'].get()
    userclass= user_info['class'].get()
    usermail = user_info['email'].get()
    print(f"the details are : id is {userid}, name is {username}, class is {userclass} and email is {usermail}")
    query1 = "INSERT INTO students(id, name, class, email) VALUES(%s, %s, %s, %s)"
    values1 = (userid, username, userclass, usermail)
    my_cursor.execute(query1, values1)


    
# #to delete the data after the entry
#     # id_box.delete(0, tk.END)
#     # name_box.delete(0, tk.END)
#     # class_box.delete(0, tk.END)
#     # email_box.delete(0, tk.END)

submit_button = ttk.Button(form_win, text = "Submit", command = sql_db)
submit_button.grid(row = 7, column = 1,sticky = tk.W)


form_win.mainloop()
conn.commit()
conn.close()