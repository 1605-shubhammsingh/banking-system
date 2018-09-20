#this page contains the buttons credit cash, debit cash and balance enquiry


from tkinter import *
import os
import sqlite3
from tkinter import messagebox as ms



#window declaration

login1 = Tk()
login1.geometry("1360x1900")
login1.title("Welcome")

bckground_label = Label(height=1000, width=1900)
image1 = PhotoImage(file="bank_home.gif")
bckground_label.config(image = image1)
bckground_label.image = image1
bckground_label.place(x=0, y=0)
bckground_label.pack()

def sign_out() :
    conn = sqlite3.connect("Banking.db")
    c = conn.cursor()
    c.execute("SELECT * FROM User")
    id = conn.execute("SELECT Phone_No FROM User WHERE Status = 'Y'")
    for row in id:
        pass
    j = row[0]
    q = "UPDATE User SET Status = 'N' where Phone_No = ?"
    c.execute(q,[j])
    conn.commit()
    conn.close()
    ms.showinfo(title="Status", message="Logged Out Successfully")
    login1.destroy()
    os.system('python home.py')

def widrawal() :
    login1.destroy()
    os.system('python widrawal.py')

def add_money() :
    login1.destroy()
    os.system('python add_money.py')

def balance_enquiry() :
    conn = sqlite3.connect("Banking.db")
    c = conn.cursor()
    id = c.execute("SELECT Balance FROM User WHERE STATUS = 'Y'")
    balance = c.fetchone()
    conn.commit()
    conn.close()
    ms.showinfo(title="Balance", message="Account Balance is:- " + str(balance))
    login1.destroy()
    os.system('python login.py')

sign_out = Button(text = "Sign Out", font = ('Verdana', 45), fg = "BLUE", command=sign_out)
sign_out.place(x = 200, y = 200)

widrawal = Button(text = "Withdrawal", font = ('Verdana', 45), fg = "BLUE", command=widrawal)
widrawal.place(x = 800, y = 200)

add_money = Button(text = "Add Money", font = ('Verdana', 45), fg = "BLUE", command=add_money)
add_money.place(x = 200, y = 500)

balance_enquiry = Button(text = "Balance", font = ('Verdana', 45), fg = "BLUE", command=balance_enquiry)
balance_enquiry.place(x = 800, y = 500)

login1.mainloop()
