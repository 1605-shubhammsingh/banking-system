from tkinter import *
import os

#Window Declaration
after_register=Tk()
after_register.geometry("1360x1900")
after_register.title("Welcome")

#setting of the background wallpaper

bckground_label = Label(height=1000, width=1900)
image1 = PhotoImage(file="bank_home.gif")
bckground_label.config(image = image1)
bckground_label.image = image1
bckground_label.place(x=0, y=0)
bckground_label.pack()

#login button for further continuation
def login_button():
    after_register.destroy()
    os.system('python login.py')

#Displaying some text regarding first login
id = Label(text="Hello Dear User, Thank You for Trusting us. \n You are being rewarded 5000 rs for \n joining with us. Press the Continue button \n for proceeding. \n Happy Banking! :)", font=('Verdana', 20))
id.place(x = 400, y = 100)

#setting up the login button

login = Button(text = "Continue", font=('Verdana', 30), fg = "BLUE", command=login_button)
login.place(x = 600, y = 600)


after_register.mainloop()
