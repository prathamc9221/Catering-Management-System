from tkinter import *
import sqlite3
import time
import datetime

def commit_to_database():
    conn = sqlite3.connect("SGAF_Application_Database.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS StatusTable(ID BLOB, Status BLOB, Timestamp TEXT)")
    #table format
    unix = time.time()
    time_data = str(datetime.datetime.fromtimestamp(unix).strftime("%m-%d-%Y %H:%M:%S"))
    #timestamp generation
    c.execute("INSERT INTO StatusTable(ID, Status, Timestamp) VALUES (?, ?, ?)", (d1.get(), d2.get(), time_data))
    conn.commit()
    b1 = Button(master, text="Quit", font="bold", fg="black", bg="white", width=15, command=master.quit)
    b1.grid(column=3, row=22)

master = Tk()
master.wm_title("Form")
Label(master, text="Cage ID", width=25).grid(column=1, row=1)
d1 = Entry(master)
d1.grid(column=2, row=1)
Label(master, text="Status", width=25).grid(column=1, row=2)
d2 = Entry(master)
d2.grid(column=2, row=2)
b2 = Button(master, text="Commit", font="bold", fg="black", bg="white", width=15, command=commit_to_database())
b2.grid(column=6, row=22)


mainloop()