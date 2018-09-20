from tkinter import *
import os

#with sqlite3.connect("Banking.db") as db:

#window declaration

root=Tk()
root.geometry("1360x1900")
root.title("Citizens Bank")

bckground_label = Label(height=1000, width=1900)
image1 = PhotoImage(file="bank_home.gif")
bckground_label.config(image = image1)
bckground_label.image = image1
bckground_label.place(x=0, y=0)
bckground_label.pack()

def quit_button() :
    root.destroy()

def signup():
    root.destroy()
    os.system('python register.py')

def login():
    root.destroy()
    os.system('python login.py')


quit_button = Button(text = "Quit", font = ('Verdana', 45), fg = "BLUE",command=quit_button)
quit_button.place(x = 600, y = 600)

signup = Button(text = "Sign Up", font = ('Verdana', 35), fg = "BLUE",command=signup)
signup.place(x = 100, y = 450)

login = Button(text = "Login", font = ('Verdana', 35), fg = "BLUE",command=login)
login.place(x = 1000, y = 450)


root.mainloop()
