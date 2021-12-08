import tkinter as tk
from tkinter import ttk

#Create window
win = tk.Tk()
win.title("Membership Form")

# to resize the window, we use geometry method
win.geometry('700x700')

#create labels
id_label = ttk.Label(win, text = "Enter Your student/staff ID : ")
id_label.grid(row=0, column=0, pady=20, padx =20, sticky = tk.W)

name_label = ttk.Label(win, text = "Enter Your name : ")
name_label.grid(row=1, column=0, pady=20, padx =20, sticky = tk.W)

course_label = ttk.Label(win, text = "Enter Your course of study : ")
course_label.grid(row=2, column=0, pady=20, padx =20,sticky = tk.W)

mail_label = ttk.Label(win, text = "Enter Your email ID : ")
mail_label.grid(row=3, column=0, pady=20, padx =20, sticky = tk.W)

campus_label = ttk.Label(win, text = "Enter Your campus name : ")
campus_label.grid(row=4, column=0, pady=20, padx =20, sticky = tk.W)

nation_label = ttk.Label(win, text = "Enter Your nationality : ")
nation_label.grid(row=5, column=0, pady=20, padx =20, sticky = tk.W)

mob_label = ttk.Label(win, text = "Enter Your mobile number : ")
mob_label.grid(row=6, column=0, pady=20, padx =20, sticky = tk.W)

gender_label = ttk.Label(win, text = "Please select your gender: ")
gender_label.grid(row=7, column=0, pady=20, padx =20, sticky = tk.W)

acad_label = ttk.Label(win, text = "Please select your academic stage: ")
acad_label.grid(row=8, column=0, sticky = tk.W, padx = 20)

#create entrybox
id_var = tk.StringVar()
id_box = ttk.Entry(win, width = 30, textvariable = id_var)
id_box.grid(row =0, column=1, pady = 20, padx = 20)
id_box.focus()

name_var = tk.StringVar()
name_box = ttk.Entry(win, width = 30, textvariable = name_var)
name_box.grid(row =1, column=1, sticky = tk.W, pady = 20, padx = 20)

course_var = tk.StringVar()
course_box = ttk.Entry(win, width = 30, textvariable = course_var)
course_box.grid(row =2, column=1,sticky = tk.W, pady = 20, padx = 20)

email_var = tk.StringVar()
email_box = ttk.Entry(win, width = 30, textvariable = email_var)
email_box.grid(row =3, column=1,sticky = tk.W, pady = 20, padx = 20)

campus_var = tk.StringVar()
campus_box = ttk.Entry(win, width = 30, textvariable = campus_var)
campus_box.grid(row =4, column=1,sticky = tk.W, pady = 20, padx = 20)

nation_var = tk.StringVar()
nation_box = ttk.Entry(win, width = 30, textvariable = nation_var)
nation_box.grid(row =5, column=1,sticky = tk.W, pady = 20, padx = 20)

mob_var = tk.StringVar()
mob_box = ttk.Entry(win, width = 30, textvariable = email_var)
mob_box.grid(row =6, column=1,sticky = tk.W, pady = 20, padx = 20)

#create combobox/dropdown box
gender_var = tk.StringVar()
gender_drop = ttk.Combobox(win, width=30, textvariable = gender_var, state = "readonly")
gender_drop['values'] = ("Select Gender", "Male","Female", "Others", "Prefer not to say")
gender_drop.current(0)
gender_drop.grid(row=7, column = 1, sticky = tk.W, padx =20, pady = 20)

#create radiobutton - current status - hostler, day boarding
usertype = tk.StringVar()
radio_1 = ttk.Radiobutton(win, text = "Diploma", value = "Diploma", variable = usertype)
radio_1.grid(row=8, column = 1, sticky = tk.W)

radio_2 = ttk.Radiobutton(win, text = "Undergraduate - First year", value = "Undergraduate - First year", variable = usertype)
radio_2.grid(row=9, column = 1, sticky = tk.W)

radio_3 = ttk.Radiobutton(win, text = "Undergraduate - Second year", value = "Undergraduate - Second year", variable = usertype)
radio_3.grid(row=10, column = 1, sticky = tk.W)

radio_4 = ttk.Radiobutton(win, text = "Undergraduate - Third year", value = "Undergraduate - Third year", variable = usertype)
radio_4.grid(row=11, column = 1, sticky = tk.W)

radio_5 = ttk.Radiobutton(win, text = "Undergraduate - Final year", value = "Undergraduate - Final year", variable = usertype)
radio_5.grid(row=12, column = 1, sticky = tk.W)

radio_6 = ttk.Radiobutton(win, text = "Postgraduate", value = "Postgraduate", variable = usertype)
radio_6.grid(row=13, column = 1, sticky = tk.W)

radio_7 = ttk.Radiobutton(win, text = "PhD", value = "PhD", variable = usertype)
radio_7.grid(row=14, column =1, sticky = tk.W)

radio_8 = ttk.Radiobutton(win, text = "Other", value = "Other", variable = usertype)
radio_8.grid(row=15, column = 1, sticky = tk.W)



#start program
win.mainloop()