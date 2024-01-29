# from tkinter import *
# from tkinter import ttk
# import tkinter
# from tkinter import messagebox
#
# import mysql.connector as sql
#
# topf = tkinter.Tk()
# topf.geometry("1000x720")
# topf.configure(bg='Yellow')
# fl = Label(topf, text=" Faculty ", font=('Agency FB', 40), fg='white', bg='blue', bd=12, relief=GROOVE,padx=50,pady=5)
# fl.place(x=700,y=5)
#
# def buttonevent(selection):
#
#     if selection in ('Exit'):
#           topf.destroy()
#
#
#
# Bexit =tkinter.Button(topf,text='Exit',fg='black',font=('arial',20),activebackground='Red',command=lambda: buttonevent('Exit'))
# #Bexit.grid(row=2 ,column=2)
# Bexit.place(x=1450,y=30)
#
#
# topf.mainloop()

import tkinter
from tkinter import ttk
from tkinter import *
from tkinter import messagebox

import mysql.connector as sql
top = tkinter.Tk()

top.geometry("1920x1030+0+0")
top.configure(bg='#FFE360')
s = Label(top, text="Faculty", font=('Agency FB', 15), fg='white', bg='blue', bd=12, relief=GROOVE)
s.place(x=450,y=5)


s1 = Label(top,text="Faculty ID:",font=('arial',25),fg='black',bg='#FFE360')
s1.place(x=8,y=64)
F1 = Entry(top,bd=10,width=50,font=10)
F1.place(x=500,y=64)

s2 = Label(top,text ="Faculty Name:",font=('arial',25),fg='black',bg='#FFE360')
s2.place(x=8,y=114)
F2 = Entry(top,bd=10,width=50,font=10)
F2.place(x=500,y=114)

s3 = Label(top,text ="Faculty Gender:",font=('arial',25),fg='black',bg='#FFE360')
s3.place(x=8,y=164)

F3 =ttk.Combobox(top,font=('arial',15),width=41,state='readonly',)
F3['values']=("Male","Female")
F3.place(x=500,y=164)

s4 = Label(top,text ="Faculty Email:",font=('arial',25),fg='black',bg='#FFE360')
s4.place(x=5,y=214)
F4 = Entry(top,bd=10,width=50,font=10)
F4.place(x=500,y=214)

s5 = Label(top,text ="Faculty Contact:",font=('arial',25),fg='black',bg='#FFE360')
s5.place(x=5,y=264)
F5 = Entry(top,bd=10,width=50,font=10)
F5.place(x=500,y=264)


s6= Label(top,text ="Faculty Qualification:",font=('arial',25),fg='black',bg='#FFE360')
s6.place(x=5,y=314)
F6 = Entry(top,bd=10,width=50,font=10)
F6.place(x=500,y=314)

s7= Label(top,text ="Faculty Department:",font=('arial',25),fg='black',bg='#FFE360')
s7.place(x=5,y=364)
F7=ttk.Combobox(top,font=('arial',12),width=50,state='readonly',)
F7['values']=("Computer","IT","ENTC","MECH.","ELECTRICAL","CIVIL","AI")
F7.place(x=500,y=364)

frm=Frame(top)
#frm.grid(row=11,column=1,)
table=ttk.Treeview(frm,column=(1,2,3,4,5,6,7),show="headings",height="9",)
yscrollbar=ttk.Scrollbar(frm,orient='vertical',command=table.yview())
frm.place(x=150,y=500,width=1145,height=190)     #frm.place(x=200,y=600,width=1160,height=190)
table.configure(yscroll=yscrollbar.set)
table.grid(row=11,column=1,)
yscrollbar.grid(row=11,column=2,sticky="ns")
table.heading(1,text="ID")
table.column(1, width=60)
table.heading(2,text="Name")
table.heading(3,text="Gender")
table.column(3, width=60)
table.heading(4,text="Email")
table.heading(5,text="Contact")
table.heading(6,text="Qualification")

table.heading(7,text="Branch")

def buttonevent(selection):
    print("Faculty ID ",F1.get())
    print("Faculty Name ", F2.get())
   # print("Faculty Gender ", F3.get()) We will not print this because we are selecting it using combobox
    print("Faculty email",F4.get())
    print("Faculty Contact ", F5.get())
    print("Faculty Qualification", F6.get())
    print("Faculty Branch", F7.get())
   # print("student branch", F8.get())
    faculty_ID= F1.get()
    name = F2.get()
    gender = F3.get()
    email = F4.get()
    contact = F5.get()
    qualification = F6.get()
    branch = F7.get()
    #branch = F8.get()
    #searchby=E9.get()
    #search=E10.get()

    if selection in ('INSERT'):
        mycon = sql.connect(host='localhost', user='root', password='root', database='project')
        cur = mycon.cursor()
        for record in table.get_children():
            table.delete(record)
        q = "select * from  faculty_record order by Faculty_ID"

        queryf= "create table if not exists faculty_record(Faculty_ID varchar(75) Not null,Faculty_Name varchar(20), Faculty_Gender varchar(30),Faculty_email varchar(100),Faculty_Contact varchar(30),Faculty_Qualification varchar(30), Faculty_Branch varchar(30))"

        cur.execute(queryf)

        mycon.commit()
        messagebox.showinfo("Success","Data Inserted Successfully!")
        print("table record created ")

        inquery = "insert into faculty_record (Faculty_ID,Faculty_Name, Faculty_Gender,Faculty_email,Faculty_Contact,Faculty_Qualification,Faculty_Branch) values ('%s','%s','%s','%s','%s','%s','%s')" % (
            faculty_ID,name,gender,email,contact,qualification,branch)
        cur.execute(inquery)
        cur.execute(q)
        rows = cur.fetchall()
        for i in rows:
            table.insert('', 'end', values=i)

        F1.delete(0, END)
        F2.delete(0, END)
        F3.delete(0, END)
        F4.delete(0, END)
        F5.delete(0, END)
        F6.delete(0, END)
        F7.delete(0, END)

        mycon.commit()
        mycon.close()
    elif selection in ('UPDATE'):
        qshowf = "SELECT * from Faculty_record  where faculty_ID ='%s'" % (faculty_ID)
        for record in table.get_children():
            table.delete(record)
        qupdatef = "update Faculty_record set NAME='%s'" % (name) + ",GENDER='%s'" % (gender) + ",EMAIL='%s'" % (
            email) + ",CONTACT='%s'" % (contact) + ",QUALIFICATION='%s'" % (qualification) +",BRANCH='%s'"%(branch)+"where faculty_ID ='%s'" % (faculty_ID)
        mycon = sql.connect(host='localhost', user='root', password='root', database='project')
        cur = mycon.cursor()
        for record in table.get_children():
            table.delete(record)

        cur.execute(qupdatef)
        cur.execute(qshowf)
        rows = cur.fetchall()

        for i in rows:
            table.insert('', 'end', values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
        F1.delete(0, END)
        F2.delete(0, END)
        F3.delete(0, END)
        F4.delete(0, END)
        F5.delete(0, END)
        F6.delete(0, END)
        F7.delete(0, END)


        mycon.commit()
        messagebox.showinfo("Success", "Data Updated Successfully!")
        mycon.close()




Finsert=tkinter.Button(top,text='INSERT',fg='black',font=('arial',20),activebackground='Red',command=lambda:buttonevent('INSERT'))
Finsert.place(x=1200,y=100)

Fupdate=tkinter.Button(top,text='UPDATE',fg='black',font=('arial',20),activebackground='Red',command=lambda: buttonevent('UPDATE') )
Fupdate.place(x=1200,y=170)

Fdelete=tkinter.Button(top,text='DELETE',fg='black',font=('arial',20),activebackground='Red',command=lambda: buttonevent('DELETE'))
Fdelete.place(x=1200,y=240)

Fsearch=tkinter.Button(top,text='SEARCH',fg='black',font=('arial',20),activebackground='Red',command=lambda: buttonevent('SEARCH'))
Fsearch.place(x=1200,y=310)

Fshowall=tkinter.Button(top,text='SHOWALL',fg='black',font=('arial',20),activebackground='Red',command=lambda: buttonevent('SHOWALL'))
Fshowall.place(x=1200,y=380)

Fexit =tkinter.Button(top,text='Exit',fg='black',font=('arial',20),activebackground='Red',command=lambda: buttonevent('Exit'))
Fexit.place(x=1200,y=30)

top.mainloop()