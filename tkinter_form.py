#first import tkinter module
import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os #it will write header only if the file is empty
win = tk.Tk()
win.title("GUI Form")

#create labels
id_label= ttk.Label(win, text = "Enter Your id : ")
id_label.grid(row=0, column=0, sticky = tk.W)

name_label = ttk.Label(win, text = "Enter Your name : ")
name_label.grid(row=1, column=0, sticky = tk.W)

class_label = ttk.Label(win, text = "Enter Your class : ")
class_label.grid(row=2, column=0, sticky = tk.W)

email_label = ttk.Label(win, text = "Enter Your email id : ")
email_label.grid(row=3, column=0, sticky = tk.W)

gender_label = ttk.Label(win, text = "Select your gender : ")
gender_label.grid(row=4, column=0, sticky = tk.W)

res_label = ttk.Label(win, text = "Select your residency status : ")
res_label.grid(row=5, column=0, sticky = tk.W)


#create entry box
id_var = tk.IntVar()
id_box = ttk.Entry(win, width = 20, textvariable = id_var)
id_box.grid(row =0, column=1,sticky = tk.W)
id_box.focus()

name_var = tk.StringVar()
name_box = ttk.Entry(win, width = 20, textvariable = name_var)
name_box.grid(row =1, column=1, sticky = tk.W)

class_var = tk.IntVar()
class_box = ttk.Entry(win, width = 10, textvariable = class_var)
class_box.grid(row =2, column=1,sticky = tk.W)

email_var = tk.StringVar()
email_box = ttk.Entry(win, width = 20, textvariable = email_var)
email_box.grid(row =3, column=1,sticky = tk.W)

#create combobox/dropdown box
gender_var = tk.StringVar()
gender_drop = ttk.Combobox(win, width=16, textvariable = gender_var, state = "readonly")
gender_drop['values'] = ("Select Gender", "Male","Female", "Others")
gender_drop.current(0)
gender_drop.grid(row=4, column = 1, sticky = tk.W)

#create radiobutton - current status - hostler, day boarding
usertype = tk.StringVar()
radio_1 = ttk.Radiobutton(win, text = "Hostler", value = "Hostler", variable = usertype)
radio_1.grid(row=5, column = 1, sticky = tk.W)

radio_2 = ttk.Radiobutton(win, text = "Day Boarding", value = "Day Boarding", variable = usertype)
radio_2.grid(row=5, column = 2, sticky = tk.W)

#create checkbutton - need to get newsletter
check_var = tk.IntVar()
check1 = ttk.Checkbutton(win, text = "Subscribe to the weekly updates", variable=check_var)
check1.grid(row = 6, columnspan = 1)

#create button
# def act():
#     userid = id_var.get()
#     username = name_var.get()
#     userclass= class_var.get()
#     usermail = email_var.get()
#     print(f"the details are : id is {userid}, name is {username}, class is {userclass} and email is {usermail}")
#     usergender = gender_var.get()
#     user_res = usertype.get()
#     if check_var.get() == 0:
#         subscribed = "No"
#     else:
#         subscribed = "Yes"
#     print(f"user is {usergender}. User is a {user_res} and user has answered {subscribed} to the subscription.")

#     with open("file.txt","a") as f:
#         f.write(f"{userid},{username},{userclass},{usermail},{usergender},{user_res},{subscribed}\n")
#     #to delete the data after the entry
#     id_box.delete(0, tk.END)
#     name_box.delete(0, tk.END)
#     class_box.delete(0, tk.END)
#     email_box.delete(0, tk.END)

#write the data into csv file
def act():
    userid = id_var.get()
    username = name_var.get()
    userclass= class_var.get()
    usermail = email_var.get()
    usergender = gender_var.get()
    user_res = usertype.get()
    if check_var.get() == 0:
        subscribed = "No"
    else:
        subscribed = "Yes"
    with open("file.csv","a", newline="")as f:
        dict_writer = DictWriter(f, fieldnames = ["User ID", "User Name", "Class", "User Email ID", "Gender", 
        "Residence", "Subscription"])
        if os.stat('file.csv').st_size ==0:
            dict_writer.writeheader()
        
        dict_writer.writerow({
            'User ID' : userid,
            'User Name' : username,
            'Class' : userclass,
            'User Email ID' : usermail,
            'Gender' : usergender,
            'Residence' : user_res,
            'Subscription' : subscribed})
    
#to delete the data after the entry
    id_box.delete(0, tk.END)
    name_box.delete(0, tk.END)
    class_box.delete(0, tk.END)
    email_box.delete(0, tk.END)

submit_button = ttk.Button(win, text = "Submit", command = act)
submit_button.grid(row = 7, column = 1,sticky = tk.W)

win.mainloop() 
#mainloop defines that win object will run infinite times

