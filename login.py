import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from PIL import ImageTk,Image
import mysql.connector as sql

top = tkinter.Tk()
top.geometry("1000x2000")
top.configure(bg='#B2EF6D')
l = Label(top, text="Login", font=('Agency FB', 40), fg='white', bg='blue', bd=12, relief=GROOVE)
l.place(x=700,y=100)

l1 = Label(top,text="User Name:",font=('arial',30),fg='black',bg='#B2EF6D')
l1.place(x=400,y=400)
E1 = Entry(top,bd=10,width=20,font=20)
E1.place(x=650,y=400)

l2 = Label(top,text ="Password:",font=('arial',30),fg='black',bg='#B2EF6D')
l2.place(x=400,y=500)
E2 = Entry(top,bd=10,width=20,font=20)
E2.place(x=650,y=500)

l4 = Label(top,text ="New User? Click On Sign In",font=('arial',20),fg='Red',bg='#B2EF6D')
l4.place(x=925,y=110)

Login=tkinter.Button(top,text='Login',fg='black',font=('arial',20),activebackground='Red',)
Login.place(x=800,y=600)

Sign_in=tkinter.Button(top,text='Sign In',fg='black',font=('arial',20),activebackground='Red',)
Sign_in.place(x=1300,y=100)

top.title("Login")

top.mainloop()