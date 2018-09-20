#this page manages Addition of cash.
#focus on this page only basic addition to Account Balance. i.e from Balance column of the User table

from tkinter import *
import os
import sqlite3
from tkinter import messagebox as ms



#window declaration

add_money = Tk()
add_money.geometry("1360x1900")
add_money.title("Add Money")

bckground_label = Label(height=1000, width=1900)
image1 = PhotoImage(file="bank_home.gif")
bckground_label.config(image = image1)
bckground_label.image = image1
bckground_label.place(x=0, y=0)
bckground_label.pack()

conn = sqlite3.connect("Banking.db")
c = conn.cursor()
q="SELECT Phone_No FROM User WHERE Status='Y'"
a=c.execute(q)
for i in a:
    pass
no=i[0]


Amount1 = Label(text="Amount :", font=('Verdana', 20))
Amount1.place(x = 200, y = 200)


amount = Entry(fg='black', bg='white', font=('Verdana', 20))
amount.place(x = 400, y = 200)


def sign_out():
    id = c.execute("SELECT Phone_No FROM User WHERE Status = 'Y'")
    for i in id:
        pass
    j = i[0]
    q = "UPDATE User SET Status = 'N' where Phone_No = ?"
    c.execute(q,[j])
    conn.commit()
    conn.close()
    ms.showinfo(title="Status", message="Logged Out Successfully")
    add_money.destroy()
    os.system('python login.py')


def credit():
    q="SELECT Balance FROM User WHERE Phone_No=?"
    a=c.execute(q,[no])
    for i in a:
        pass
    balance=i[0]
    credit=amount.get()
    amt=(float)(credit)
    new_bal=balance+amt
    print(new_bal)
    q="UPDATE User Set Balance=? WHERE Phone_No=?"
    c.execute(q,[new_bal,no])
    ms.showinfo("Success","Money Added")
    id = c.execute("SELECT Phone_No FROM User WHERE Status = 'Y'")
    for i in id:
        pass
    j = i[0]
    q = "UPDATE User SET Status = 'N' where Phone_No = ?"
    c.execute(q,[j])
    conn.commit()
    conn.close()
    ms.showinfo(title="Status", message="Logged Out Successfully")
    add_money.destroy()
    os.system('python login.py')

sign_out = Button(text = "Cancel", font = ('Verdana', 45), fg = "BLUE",command=sign_out)
sign_out.place(x = 300, y = 500)

confirm = Button(text = "Confirm", font = ('Verdana', 45), fg = "BLUE",command=credit)
confirm.place(x = 600, y = 500)


add_money.mainloop()
