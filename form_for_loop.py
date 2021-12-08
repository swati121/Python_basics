#create a form using for loop
import tkinter as tk
from tkinter import ttk
form_win = tk.Tk()
form_win.title("Loop Form")

#create labels - ID, name, age, city, state, country, school
labels = ["Enter your ID : ", "Enter your name : ", "What is your age : ", "Please specify your city : ", 
"Please mention your state : ", "Your country : ", "Name of your school : "]

for x in range(len(labels)):
    cur_label = "label"+str(x)
    cur_label = ttk.Label(form_win, text = labels[x])
    cur_label.grid(row = x, column =0, sticky = tk.W)

#create entrybox
# name_var = tk.StringVar()
user_info = {
    "ID" : tk.IntVar(),
    "name" : tk.StringVar(),
    "age" : tk.StringVar(),
    "city" : tk.StringVar(),
    "state" : tk.StringVar(),
    "country" : tk.StringVar(),
    "school" : tk.StringVar()
}

counter = 0
for i in user_info:
    cur_box = "entry" + i #entryID, #entryname
    cur_box = ttk.Entry(form_win, width = 20, textvariable = user_info[i])
    cur_box.grid(row = counter, column=1)
    counter +=1


form_win.mainloop()