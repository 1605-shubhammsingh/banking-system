#this page contains the buttons credit cash, debit cash and balance enquiry


from tkinter import *
import os
import sqlite3
from tkinter import messagebox as ms

conn = sqlite3.connect("Banking.db")
c = conn.cursor()
#c.execute("CREATE TABLE IF NOT EXISTS Account(Phone_No REAL NOT NULL PRIMARY KEY, UName TEXT NOT NULL, Password TEXT NOT NULL, UserId TEXT NOT NULL, Status TEXT DEFAULT 'N');")
#c.execute("SELECT * FROM User")

#window declaration

login1 = Tk()
login1.geometry("1360x1900")
login1.title("Login")

bckground_label = Label(height=1000, width=1900)
image1 = PhotoImage(file="bank_home.gif")
bckground_label.config(image = image1)
bckground_label.image = image1
bckground_label.place(x=0, y=0)
bckground_label.pack()

def sign_out() :
    pass

def widrawal() :
    pass

def add_money() :
    pass

def balance_enquiry() :
    pass

sign_out = Button(text = "Sign Out", font = ('Verdana', 45), fg = "BLUE", command=sign_out)
sign_out.place(x = 200, y = 200)

widrawal = Button(text = "Widrawal", font = ('Verdana', 45), fg = "BLUE", command=widrawal)
widrawal.place(x = 800, y = 200)

add_money = Button(text = "Add Money", font = ('Verdana', 45), fg = "BLUE", command=add_money)
add_money.place(x = 200, y = 500)

balance_enquiry = Button(text = "Balance", font = ('Verdana', 45), fg = "BLUE", command=balance_enquiry)
balance_enquiry.place(x = 800, y = 500)

login1.mainloop()
