#!/usr/bin/env python
"""
_file name_ = Main.py
__python version = 3.11
_author_ = "Prathamesh Chaudhari - prathamc9221@gmail.com",
_status_ = "Development"
"""


# import modules

from os import name
from tkinter import *
from functools import partial
import os
from datetime import date
from datetime import time
from datetime import datetime
import _sqlite3
import sqlite3
import sys
# noinspection PyUnresolvedReferences
import pandas as pd

# Designing window for registration
global a, b,id
id=0


def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry


    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Forgot Password", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Enter New Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()

    password_lable = Label(register_screen, text="Enter New Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command=register_user).pack()


# Designing window for login

def login():

    main_screen.destroy()
    global login_screen
    login_screen = Tk()
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)

    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()


# Implementing event on register button

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w+")
    file = open(username_info, "a+")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()


# Implementing event on login button



def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()


# Designing popup for login success

def login_sucess():

    frame1 = Tk()
    frame1.title("Admin Section")
    frame1.geometry("500x500")
    frame1.configure(background="gray")

    def ad1():

        global addstud_screen
        addstud_screen = Tk()
        addstud_screen.title("ADD A STUDENT")
        addstud_screen.geometry("500x550")

        global name
        global add,mob_no,count,id
        global dat
        global name_entry,ID_entry,add_entry,mob_entry,date_entry

        global date_entry
        global today
        global days
        id=1

        name = StringVar()
        #id = StringVar()
        dat = StringVar()
        add = StringVar()
        mob_no = StringVar()
        days = StringVar()

        Label(addstud_screen, text="Please enter details below", bg="blue").pack()
        Label(addstud_screen, text="").pack()
        username_lable = Label(addstud_screen, text="Name of student* ")
        username_lable.pack()
        name_entry = Entry(addstud_screen, textvariable=name)
        name_entry.pack()



        id_lable = Label(addstud_screen, text="USER ID * ")
        id_lable.pack()
        ID_label = Label(addstud_screen, text=id)
        ID_label.pack()

        add_lable = Label(addstud_screen, text="ADDRESS * ")
        add_lable.pack()
        add_entry = Entry(addstud_screen, textvariable=add)
        add_entry.pack()

        mob_lable = Label(addstud_screen, text="MOBILE NUMBER * ")
        mob_lable.pack()
        mob_entry = Entry(addstud_screen, textvariable=mob_no)
        mob_entry.pack()

        today = date.today()

        mob_lable = Label(addstud_screen, text="Number Of Days * ")
        mob_lable.pack()
        mob_entry = Entry(addstud_screen, textvariable=days)
        mob_entry.pack()

        dat_lable = Label(addstud_screen, text="Date of Join * ")
        dat_lable.pack()
        dat_lable = Label(addstud_screen, text=today)
        dat_lable.pack()



        Label(addstud_screen, text="").pack()

        Label(addstud_screen, text="").pack()
        Button(addstud_screen, text="Register", width=10, height=1, bg="red", command=student_user).pack()
        id=id+1

    def student_user():
        global conn, cursor

        username_info = name.get()
        password_info = id
        dat_info = today

        file = open("guru99.txt", "a+")
        file.write(username_info + "\t")
        file.write(str(password_info) + "\t")
        file.write(str(dat_info) + "\t")
        file.write(str(days) + "\n")
        file.close()

        username_info = name.get()
        password_info = id
        date_info = today
        adderss_info = add.get()
        mobile_info = mob_no.get()
        endday_info = days.get()

        conn = sqlite3.connect("pythontut.db")
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS student ( username TEXT,id INTEGER,date REAL,address TEXT,mobile_no NUMERIC,end_day REAL)")
        cursor.execute("INSERT INTO student (username,id,date,address,mobile_no,end_day) VALUES(?,?,?,?,?,?)", (username_info, password_info,date_info,adderss_info,mobile_info,endday_info))
        # cursor.execute("SELECT * FROM `member` WHERE  `username` = ''")

        conn.commit()
        # Result.config(text="Result = %d")

        name_entry.delete(0, END)
        mob_entry.delete(0, END)
        add_entry.delete(0, END)
        #date_entry.delete(0, END)

        Label(addstud_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

    def disp1():
        frame1.destroy()
        global showstud_screen,scr

        showstud_screen = Tk()
        showstud_screen.title("ADD A STUDENT")
        showstud_screen.geometry("800x600")

        conn = sqlite3.connect("pythontut.db")
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM student")
        counter = cursor.fetchall()
        print(counter)

        count = counter[0]
        scr = count[0]
        print(scr)

        records = cursor.fetchall()



        #Button(showstud_screen, text="Exit", width=10, height=1, bg="red", command=exit).pack()
        i=0
        cursor.execute("SELECT * FROM `student` ")
        pint = cursor.fetchall()
        if scr >= 1:
            at = pint[0]

            Label(showstud_screen, text="NAME \t\t ID \t DATE \t ADDRESS \t\t MOBILE NUMBER  NO. OF DAYS", bg="red",
                  font=("bold, 20")).pack()
            label1 = Label(showstud_screen,
                           text=at[0] + "\t" + str(at[1]) + "\t" + str(at[2]) + "\t" + at[3] + "\t" + str(
                               at[4]) + "\t" + str(
                               at[5]) + "\n", font=("calibri", 20)).pack()
        if scr >= 2:
            at = pint[1]

            label2 = Label(showstud_screen,
                           text=str(at[0]) + "\t" + str(at[1]) + "\t" + str(at[2]) + "\t" + str(at[3]) + "\t" + str(
                               at[4]) + "\t" + str(
                               at[5]) + "\n", font=("calibri", 20)).pack()


        if scr >= 3:
            at = pint[2]

            label3 = Label(showstud_screen,
                           text=str(at[0]) + "\t" + str(at[1]) + "\t" + str(at[2]) + "\t" + str(at[3]) + "\t" + str(
                               at[4]) + "\t" + str(
                               at[5]) + "\n", font=("calibri", 20)).pack()


        if scr >= 4:
            at = pint[3]

            label4 = Label(showstud_screen,
                           text=str(at[0]) + "\t" + str(at[1]) + "\t" + str(at[2]) + "\t" + str(at[3]) + "\t" + str(
                               at[4]) + "\t" + str(
                               at[5]) + "\n", font=("calibri", 20)).pack()


        if scr >= 5:
            at = pint[4]

            label5 = Label(showstud_screen,
                           text=str(at[0]) + "\t" + str(at[1]) + "\t" + str(at[2]) + "\t" + str(at[3]) + "\t" + str(
                               at[4]) + "\t" + str(
                               at[5]) + "\n", font=("calibri", 20)).pack()



        if scr >= 6:
            at = pint[5]

            label6 = Label(showstud_screen,
                           text=str(at[0]) + "\t" + str(at[1]) + "\t" + str(at[2]) + "\t" + str(at[3]) + "\t" + str(
                               at[4]) + "\t" + str(
                               at[5]) + "\n", font=("calibri", 20)).pack()


        if scr >= 7:
            at = pint[6]

            label7 = Label(showstud_screen,
                           text=str(at[0]) + "\t" + str(at[1]) + "\t" + str(at[2]) + "\t" + str(at[3]) + "\t" + str(
                               at[4]) + "\t" + str(
                               at[5]) + "\n", font=("calibri", 20)).pack()


        if scr >= 8:
            at = pint[7]

            label8 = Label(showstud_screen,
                           text=str(at[0]) + "\t" + str(at[1]) + "\t" + str(at[2]) + "\t" + str(at[3]) + "\t" + str(
                               at[4]) + "\t" + str(
                               at[5]) + "\n", font=("calibri", 20)).pack()


        if scr >= 9:
            at = pint[8]

            label9 = Label(showstud_screen,
                           text=str(at[0]) + "\t" + str(at[1]) + "\t" + str(at[2]) + "\t" + str(at[3]) + "\t" + str(
                               at[4]) + "\t" + str(
                               at[5]) + "\n", font=("calibri", 20)).pack()


        if scr >= 9:
            at = pint[9]

            label10 = Label(showstud_screen,
                            text=str(at[0]) + "\t" + str(at[1]) + "\t" + str(at[2]) + "\t" + str(
                                at[3]) + "\t" + str(
                                at[4]) + "\t" + str(
                                at[5]) + "\n", font=("calibri", 20)).pack()


    def grc1():

        global grc_screen
        grc_screen = Tk()
        grc_screen.title("ADD A STUDENT")
        grc_screen.geometry("500x550")

        global name
        global add, mob_no, count, id
        global dat
        global name_entry, ID_entry, add_entry, mob_entry
        global l1,l2,l3,l4,l5,l6,l7,l8,l9,l10,l11,l12,l13,l14
        global date_entry
        global today
        global days
        global list1,list2,list3,list4,list5,list6,list7,list8,list9,list10,list11,list12,list13,list14
        id = 1


        # id = StringVar()
        dat = StringVar()
        add = StringVar()
       # mob_no = StringVar()
        days = StringVar()

        list1= StringVar()
        list2= StringVar()
        list3= StringVar()
        list4= StringVar()
        list5= StringVar()
        list6= StringVar()
        list7= StringVar()
        list8= StringVar()
        list9= StringVar()
        list10= StringVar()
        list11= StringVar()
        list12= StringVar()
        list13= StringVar()
        list14= StringVar()

        Label( grc_screen, text="Please enter details below", bg="blue").grid(row=0, column=1, sticky=W, pady=2)

        username_lable = Label(grc_screen, text="Name of Grocery* "+"USER ID * ",font=("calibri", 20))
        username_lable.grid(row=1, column=1, sticky=W, pady=2)



        l2 = Entry(grc_screen,  textvariable=list2).grid(row=2, column=1, sticky=W, pady=2)
        l3 = Entry(grc_screen, textvariable=list3).grid(row=3, column=1, sticky=W, pady=2)
        l4 = Entry(grc_screen, textvariable=list4).grid(row=4, column=1, sticky=W, pady=2)
        l5 = Entry(grc_screen,  textvariable=list5).grid(row=5, column=1, sticky=W, pady=2)
        l6 = Entry(grc_screen,  textvariable=list6).grid(row=6, column=1, sticky=W, pady=2)
        l7 = Entry(grc_screen, textvariable=list7).grid(row=7, column=1, sticky=W, pady=2)
        l1 = Entry(grc_screen, textvariable=list1).grid(row=8, column=1, sticky=W, pady=2)


        l9 = Entry(grc_screen, textvariable=list9).grid(row=2, column=2, sticky=W, pady=2)
        l10 = Entry(grc_screen, textvariable=list10).grid(row=3, column=2, sticky=W, pady=2)
        l11 = Entry(grc_screen, textvariable=list11).grid(row=4, column=2, sticky=W, pady=2)
        l12 = Entry(grc_screen, textvariable=list12).grid(row=5, column=2, sticky=W, pady=2)
        l13 = Entry(grc_screen, textvariable=list13).grid(row=6, column=2, sticky=W, pady=2)
        l14 = Entry(grc_screen, textvariable=list14).grid(row=7, column=2, sticky=W, pady=2)
        l8 = Entry(grc_screen, textvariable=list8).grid(row=8, column=2, sticky=W, pady=2)
        today = date.today()



        Label( grc_screen, text="").grid(row=9, column=1, sticky=W, pady=2)

        Label( grc_screen, text="").grid(row=10, column=1, sticky=W, pady=2)


        Button( grc_screen, text="Register", width=10, height=1, bg="red", command=grc2).grid(row=11, column=1, sticky=W, pady=2)
        id = id + 1

    def grc2():
        global conn, cursorm,lays

        username_info = list1.get()
        password_info = id
        dat_info = list8

        file = open("guru99.txt", "a+")
        file.write(username_info + "\t")
        file.write(str(password_info) + "\t")
        file.write(str(dat_info) + "\t")
        file.write(str(days) + "\n")
        file.close()

        username_info2 = list2.get()
        username_info3= list3.get()
        username_info4= list4.get()
        username_info5= list5.get()
        username_info6= list6.get()
        username_info7= list7.get()
        username_info1= list1.get()

        endday_info9 = list9.get()
        endday_info10= list10.get()
        endday_info11= list11.get()
        endday_info12= list12.get()
        endday_info13= list13.get()
        endday_info14= list14.get()
        endday_info8= list8.get()







        date_info = today

        endday_info = list9.get()


        conn = sqlite3.connect("pythontut.db")
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS groc (list TEXT,fair REAL)")
        cursor.execute("INSERT INTO groc (list,fair) VALUES(?,?)",
                       (username_info2, endday_info9))
        cursor.execute("INSERT INTO groc (list,fair) VALUES(?,?)",
                       (username_info3, endday_info10))
        cursor.execute("INSERT INTO groc (list,fair) VALUES(?,?)",
                       (username_info4, endday_info11))
        cursor.execute("INSERT INTO groc (list,fair) VALUES(?,?)",
                       (username_info5, endday_info12))
        cursor.execute("INSERT INTO groc (list,fair) VALUES(?,?)",
                       (username_info6, endday_info13))
        cursor.execute("INSERT INTO groc (list,fair) VALUES(?,?)",
                       (username_info7, endday_info14))
        cursor.execute("INSERT INTO groc (list,fair) VALUES(?,?)",
                       (username_info1, endday_info8))
        # cursor.execute("SELECT * FROM `member` WHERE  `username` = ''")

        conn.commit()
        # Result.config(text="Result = %d")





        Label(grc_screen, text="Registration Success", fg="green", font=("calibri", 11)).grid(row=12, column=1, sticky=W, pady=2)

        conn.commit()

    def delf():

        global login_screen
        login_screen = Tk()
        login_screen.title("Login")
        login_screen.geometry("300x250")
        Label(login_screen, text="Please enter details below to login").pack()
        Label(login_screen, text="").pack()

        global username_verify
        global password_verify


        password_verify = StringVar()

        global username_login_entry
        global password_login_entry

        Label(login_screen, text="Username * ").pack()
        username_login_entry = Entry(login_screen, textvariable=username_verify)

        username_login_entry.pack()
        Label(login_screen, text="").pack()

        Label(login_screen, text="").pack()
        Button(login_screen, text="Open", width=10, height=1, command=student_verify).pack()

    def student_verify():
        id_info= username_verify
        conn = sqlite3.connect("pythontut.db")
        cursor = conn.cursor()
        #cursor.execute(
           # "CREATE TABLE IF NOT EXISTS student (list TEXT,fair REAL)")
        cursor.execute("DELETE FROM student WHERE id= id_info ")
        a = cursor.fetchall()

    def emp1():
        global emp_screen
        emp_screen = Tk()
        emp_screen.title("Employee ")
        emp_screen.geometry("500x550")

        Add = Label(emp_screen , text="Add New Student: ", font=("calibri", 11)).grid(row=2, column=1, sticky=W, pady=2)
        Addb = Button(emp_screen , text="Add", command=ademp, font=("calibri", 11)).grid(row=2, column=2, sticky=W, pady=2)

        Disp = Label(emp_screen , text="Show List of Students: ", font=("calibri", 11)).grid(row=3, column=1, sticky=W,
                                                                                        pady=2)
        Dispb = Button(emp_screen , text="Show", command=emp2, font=("calibri", 11)).grid(row=3, column=2, sticky=W, pady=2)

    def ademp():
        global addstud_screen
        addstud_screen = Tk()
        addstud_screen.title("ADD A STUDENT")
        addstud_screen.geometry("500x550")

        global name
        global add, mob_no, count, id
        global dat
        global name_entry, ID_entry, add_entry, mob_entry, date_entry

        global date_entry
        global today
        global days
        id = 1

        name = StringVar()
        # id = StringVar()
        dat = StringVar()
        add = StringVar()
        mob_no = StringVar()
        days = StringVar()

        Label(addstud_screen, text="Please enter details below", bg="blue").pack()
        Label(addstud_screen, text="").pack()
        username_lable = Label(addstud_screen, text="Name of employee* ")
        username_lable.pack()
        name_entry = Entry(addstud_screen, textvariable=name)
        name_entry.pack()

        id_lable = Label(addstud_screen, text="USER ID * ")
        id_lable.pack()
        ID_label = Label(addstud_screen, text=id)
        ID_label.pack()

        add_lable = Label(addstud_screen, text="ADDRESS * ")
        add_lable.pack()
        add_entry = Entry(addstud_screen, textvariable=add)
        add_entry.pack()

        mob_lable = Label(addstud_screen, text="MOBILE NUMBER * ")
        mob_lable.pack()
        mob_entry = Entry(addstud_screen, textvariable=mob_no)
        mob_entry.pack()

        today = date.today()

        mob_lable = Label(addstud_screen, text="Salary * ")
        mob_lable.pack()
        mob_entry = Entry(addstud_screen, textvariable=days)
        mob_entry.pack()

        dat_lable = Label(addstud_screen, text="Date of Join * ")
        dat_lable.pack()
        dat_lable = Label(addstud_screen, text=today)
        dat_lable.pack()

        Label(addstud_screen, text="").pack()

        Label(addstud_screen, text="").pack()
        Button(addstud_screen, text="Register", width=10, height=1, bg="red", command=emp_user).pack()
        id = id + 1

    def emp_user():
        global conn, cursor

        username_info = name.get()
        password_info = id
        dat_info = today

        file = open("guru99.txt", "a+")
        file.write(username_info + "\t")
        file.write(str(password_info) + "\t")
        file.write(str(dat_info) + "\t")
        file.write(str(days) + "\n")
        file.close()

        username_info = name.get()
        password_info = id
        date_info = today
        adderss_info = add.get()
        mobile_info = mob_no.get()
        endday_info = days.get()

        conn = sqlite3.connect("pythontut.db")
        cursor = conn.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS employee ( username TEXT,id INTEGER,date REAL,address TEXT,mobile_no NUMERIC,end_day REAL)")
        cursor.execute("INSERT INTO student (username,id,date,address,mobile_no,end_day) VALUES(?,?,?,?,?,?)",
                       (username_info, password_info, date_info, adderss_info, mobile_info, endday_info))
        # cursor.execute("SELECT * FROM `member` WHERE  `username` = ''")

        conn.commit()
        # Result.config(text="Result = %d")

        name_entry.delete(0, END)
        mob_entry.delete(0, END)
        add_entry.delete(0, END)
        # date_entry.delete(0, END)

        Label(addstud_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

    def emp2():
        global showstud_screen, scr

        grc3_screen = Tk()
        grc3_screen.title("ADD A STUDENT")
        grc3_screen.geometry("800x600")

        conn = sqlite3.connect("pythontut.db")
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM student")
        counter = cursor.fetchall()
        print(counter)

        count = counter[0]
        scr = count[0]
        print(scr)

        records = cursor.fetchall()

        # Button(showstud_screen, text="Exit", width=10, height=1, bg="red", command=exit).pack()
        i = 0
        cursor.execute("SELECT * FROM `employee` ")
        pint = cursor.fetchall()
        if scr >= 1:
            at = pint[0]

            Label(showstud_screen, text="NAME \t\t ID \t DATE \t ADDRESS \t\t MOBILE NUMBER  SALARY", bg="red",
                  font=("bold, 20")).pack()
            label1 = Label( grc3_screen,
                           text=at[0] + "\t" + str(at[1]) + "\t" + str(at[2]) + "\t" + at[3] + "\t" + str(
                               at[4]) + "\t" + str(
                               at[5]) + "\n", font=("calibri", 20)).pack()
        if scr >= 2:
            at = pint[1]

            label2 = Label( grc3_screen,
                           text=str(at[0]) + "\t" + str(at[1]) + "\t" + str(at[2]) + "\t" + str(at[3]) + "\t" + str(
                               at[4]) + "\t" + str(
                               at[5]) + "\n", font=("calibri", 20)).pack()

        if scr >= 3:
            at = pint[2]

            label3 = Label( grc3_screen,
                           text=str(at[0]) + "\t" + str(at[1]) + "\t" + str(at[2]) + "\t" + str(at[3]) + "\t" + str(
                               at[4]) + "\t" + str(
                               at[5]) + "\n", font=("calibri", 20)).pack()

        if scr >= 4:
            at = pint[3]

            label4 = Label( grc3_screen,
                           text=str(at[0]) + "\t" + str(at[1]) + "\t" + str(at[2]) + "\t" + str(at[3]) + "\t" + str(
                               at[4]) + "\t" + str(
                               at[5]) + "\n", font=("calibri", 20)).pack()

        if scr >= 5:
            at = pint[4]

            label5 = Label(showstud_screen,
                           text=str(at[0]) + "\t" + str(at[1]) + "\t" + str(at[2]) + "\t" + str(at[3]) + "\t" + str(
                               at[4]) + "\t" + str(
                               at[5]) + "\n", font=("calibri", 20)).pack()

        if scr >= 6:
            at = pint[5]

            label6 = Label( grc3_screen,
                           text=str(at[0]) + "\t" + str(at[1]) + "\t" + str(at[2]) + "\t" + str(at[3]) + "\t" + str(
                               at[4]) + "\t" + str(
                               at[5]) + "\n", font=("calibri", 20)).pack()

        if scr >= 7:
            at = pint[6]

            label7 = Label( grc3_screen,
                           text=str(at[0]) + "\t" + str(at[1]) + "\t" + str(at[2]) + "\t" + str(at[3]) + "\t" + str(
                               at[4]) + "\t" + str(
                               at[5]) + "\n", font=("calibri", 20)).pack()

        if scr >= 8:
            at = pint[7]

            label8 = Label( grc3_screen,
                           text=str(at[0]) + "\t" + str(at[1]) + "\t" + str(at[2]) + "\t" + str(at[3]) + "\t" + str(
                               at[4]) + "\t" + str(
                               at[5]) + "\n", font=("calibri", 20)).pack()

        if scr >= 9:
            at = pint[8]

            label9 = Label( grc3_screen,
                           text=str(at[0]) + "\t" + str(at[1]) + "\t" + str(at[2]) + "\t" + str(at[3]) + "\t" + str(
                               at[4]) + "\t" + str(
                               at[5]) + "\n", font=("calibri", 20)).pack()

        if scr >= 9:
            at = pint[9]

            label10 = Label( grc3_screen,
                            text=str(at[0]) + "\t" + str(at[1]) + "\t" + str(at[2]) + "\t" + str(
                                at[3]) + "\t" + str(
                                at[4]) + "\t" + str(
                                at[5]) + "\n", font=("calibri", 20)).pack()


    Add = Label(frame1, text="Add New Student: ",font=("calibri", 11)).grid(row=2, column=1, sticky=W, pady=2)
    Addb = Button(frame1, text="Add", command=ad1,font=("calibri", 11)).grid(row=2, column=2, sticky=W, pady=2)

    Disp = Label(frame1, text="Show List of Students: ",font=("calibri", 11)).grid(row=3, column=1, sticky=W, pady=2)
    Dispb = Button(frame1, text="Show", command=disp1,font=("calibri", 11)).grid(row=3, column=2, sticky=W, pady=2)

    Grc = Label(frame1, text="Grocery Section",font=("calibri", 11)).grid(row=4, column=1, sticky=W, pady=2)
    Grcb = Button(frame1, text="Grocery", command=grc1,font=("calibri", 11)).grid(row=4, column=2, sticky=W, pady=2)

    Dele = Label(frame1, text="Remove Student ", font=("calibri", 11)).grid(row=5, column=1, sticky=W, pady=2)
    Deleb = Button(frame1, text="Remove", command=delf, font=("calibri", 11)).grid(row=5, column=2, sticky=W, pady=2)

    Emp = Label(frame1, text="Employee Management ", font=("calibri", 11)).grid(row=6, column=1, sticky=W, pady=2)
    Empb = Button(frame1, text="Emp", command=emp1, font=("calibri", 11)).grid(row=6, column=2, sticky=W, pady=2)

    login_screen.destroy()


# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()


# Designing popup for user not found

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()


# Deleting popups

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()


# Designing Main(first) window

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")

    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()

    result_ = cursor.fetchall()
    count = cursor.rowcount

    Label(text="Select Your Choice", bg="red", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login for admin", height="2",bg="gray", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Change Password", height="2",bg="gray", width="30", command=register).pack()

    main_screen.mainloop()


main_account_screen()
