from tkinter import *
import os
import sqlite3
from tkinter import messagebox as ms

conn = sqlite3.connect("Banking.db")
c = conn.cursor()

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

def back_button():
    login1.destroy()
    os.system('python home.py')

back_button = Button(text = "Back", font = ('Verdana', 45), fg = "BLUE", command=back_button)
back_button.place(x = 600, y = 600)

id = Label(text="User ID", font=('Verdana', 20))
id.place(x = 300, y = 200)
passw = Label(text="Password", font=('Verdana', 20))
passw.place(x = 300, y = 300)

UserId = Entry(fg='black', bg='white', font=('Verdana', 20))
UserId.place(x = 500, y = 200)
Password = Entry(fg='black', bg='white', font=('Verdana', 20), show="*")
Password.place(x = 500, y = 300)


def login_butto():
    query="SELECT * FROM User WHERE UserId=? AND Password=?"
    c.execute(query,[UserId.get(), Password.get()])
    results=c.fetchall()

    if results:
        q = "UPDATE  User SET Status = 'Y' where UserId=?"
        c.execute(q,[UserId.get()])
        conn.commit()
        conn.close()
        ms.showinfo(title="STATUS", message="You are Successfully Logged in")
        login1.destroy()
        os.system('python bank_main.py')

    else:
        ms.showerror(title="LOGIN ERROR", message="Invalid User ID or Password")



login = Button(text = "Login", font = ('Verdana', 45), fg = "BLUE", command=login_butto)
login.place(x = 300, y = 600)


login1.mainloop()
