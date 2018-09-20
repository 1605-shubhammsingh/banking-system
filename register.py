from tkinter import *
import os
import sqlite3
from tkinter import messagebox as ms
import math

#connect the database

conn = sqlite3.connect("Banking.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS User(Phone_No REAL NOT NULL PRIMARY KEY, UName TEXT NOT NULL, Password TEXT NOT NULL, UserId TEXT NOT NULL, Balance REAL NOT NULL, Status TEXT DEFAULT 'N');")
c.execute("SELECT * FROM User")

#window declaration

register = Tk()
register.geometry("1360x1900")
register.title("Join with us")

bckground_label = Label(height=1000, width=1900)
image1 = PhotoImage(file="bank_home.gif")
bckground_label.config(image = image1)
bckground_label.image = image1
bckground_label.place(x=0, y=0)
bckground_label.pack()

#window declaration over

#Enter the details for Registration which includes Phone Number, User Name, Password, User ID

#Phone_No, UName, Password, UserId

introduction = Label(text = "Note:Your Phone Number is your Account Number", font = ('Times', 20))
introduction.place(x = 350, y = 20)

name = Label(text = "User Name", font = ('Verdana', 20))
name.place(x = 200, y = 100)
UName = Entry(width = 100, font = ('Verdana', 20))
UName.place(x = 470, y = 100)

userid = Label(text = "User ID", font = ('Verdana', 20))
userid.place(x = 200, y = 200)
UserId = Entry(width = 100, font = ('Verdana', 20))
UserId.place(x = 470, y = 200)

phone = Label(text = "Phone No.", font = ('Verdana', 20))
phone.place(x = 200, y = 300)
Phone_No = Entry(width = 100, font = ('Verdana', 20))
Phone_No.place(x = 470, y = 300)

passw = Label(text = "Password", font = ('Verdana', 20))
passw.place(x = 200, y = 400)
Password = Entry(width = 100, font = ('Verdana', 20), show="*")
Password.place(x = 470, y = 400)

cpass = Label(text = "Confirm Password", font = ('Verdana', 20))
cpass.place(x = 200, y = 500)
CPassword = Entry(width = 100, font = ('Verdana', 20), show="*")
CPassword.place(x = 470, y = 500)

#Declaration is Done

#Add all the buttons

#Previous buttons
def back_button() :
    register.destroy()
    os.system('python home.py')


#for confirmation of Password
def reg_button() :
    if Password.get() != CPassword.get() :
        ms.showerror(title="Error", message="Password Do Not Match")

    else :
        query=("INSERT INTO User(Phone_No,UName,Password,UserId,Balance)Values(?,?,?,?,5000)")
        c.execute(query,[Phone_No.get(),UName.get(),Password.get(),UserId.get()])
        ms.showinfo(title="Welcome",message="Congratulations you are registered")
        conn.commit()
        conn.close()
        register.destroy()
        os.system('python after_register.py')

#set the buttons
back_button = Button(text = "Back", font=('Verdana', 20), command=back_button)
back_button.place(x = 300, y = 600)

register = Button(text = "Register", font=('Verdana', 20), command=reg_button)
register.place(x = 500, y = 600)

register.mainloop()
