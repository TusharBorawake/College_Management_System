from tkinter import *
from tkinter import ttk
import tkinter
from tkinter import messagebox

from PIL import ImageTk,Image
import mysql.connector as sql

top = tkinter.Tk()
top.geometry("1930x1030")
top.configure(bg='Sky blue')
l = Label(top, text="Student Record Management System", font=('Agency FB', 40), fg='white', bg='blue', bd=12, relief=GROOVE)
l.place(x=500,y=5)

l1 = Label(top,text="Student Roll No.:",font=('arial',30),fg='black',bg='sky blue')
l1.place(x=5,y=100)
E1 = Entry(top,bd=10,width=50,font=10)
E1.place(x=500,y=100)

l2 = Label(top,text ="Student Name:",font=('arial',30),fg='black',bg='sky blue')
l2.place(x=5,y=160)
E2 = Entry(top,bd=10,width=50,font=10)
E2.place(x=500,y=160)

l3 = Label(top,text ="Student Gender:",font=('arial',30),fg='black',bg='sky blue')
l3.place(x=5,y=220)
E3 =ttk.Combobox(top,font=('arial',15),width=50,state='readonly',)
E3['values']=("Male","Female")
E3.place(x=500,y=220)

l4 = Label(top,text ="Student Email:",font=('arial',30),fg='black',bg='sky blue')
l4.place(x=5,y=280)
E4 = Entry(top,bd=10,width=50,font=10)
E4.place(x=500,y=280)

l5 = Label(top,text ="Student Contact:",font=('arial',30),fg='black',bg='sky blue')
l5.place(x=5,y=350)
E5 = Entry(top,bd=10,width=50,font=10)
E5.place(x=500,y=350)

l6= Label(top,text ="Student DOB:",font=('arial',30),fg='black',bg='sky blue')
l6.place(x=5,y=420)
E6 = Entry(top,bd=10,width=50,font=10)
E6.place(x=500,y=420)

l7= Label(top,text ="Student Address:",font=('arial',30),fg='black',bg='sky blue')
l7.place(x=5,y=480)
E7 = Entry(top,bd=10,width=50,font=10)
E7.place(x=500,y=480)

ll8= Label(top,text ="Student Class:",font=('arial',30),fg='black',bg='sky blue')
ll8.place(x=5,y=540)
EE8=ttk.Combobox(top,font=('arial',15),width=25,state='readonly',)
EE8['values']=("FE","SE","TE","BE")
EE8.place(x=500,y=540)

l8= Label(top,text ="Student Branch:",font=('arial',30),fg='black',bg='sky blue')
l8.place(x=900,y=540)
E8=ttk.Combobox(top,font=('arial',15),width=25,state='readonly',)
E8['values']=("Computer","IT","Electrical","ENTC","Mechanical","Civil")
E8.place(x=1200,y=540)

l9= Label(top,text ="Search By:",font=('arial',15),fg='black',bg='sky blue')
l9.place(x=5,y=620)
E9=ttk.Combobox(top,font=('arial',15),width=10,state='readonly',)
E9['values']=("Roll_No","Name","Contact")
E9.place(x=7,y=650)

E10 = Entry(top, bd=10, width=10, font=10)
E10.place(x=7, y=700)




frm=Frame(top)
#frm.grid(row=11,column=1,)
table=ttk.Treeview(frm,column=(1,2,3,4,5,6,7,8,9),show="headings",height="9",)
yscrollbar=ttk.Scrollbar(frm,orient='vertical',command=table.yview())
frm.place(x=150,y=600,width=1260,height=190)     #frm.place(x=200,y=600,width=1160,height=190)
table.configure(yscroll=yscrollbar.set)
table.grid(row=11,column=1,)
yscrollbar.grid(row=11,column=2,sticky="ns")
table.heading(1,text="Roll No")
table.column(1, width=60)
table.heading(2,text="Name")
table.heading(3,text="Gender")
table.column(3, width=60)
table.heading(4,text="Email")
table.heading(5,text="Contact")
table.heading(6,text="DOB")
table.heading(7,text="Address")
table.heading(8,text="Class")
table.column(8, width=60)
table.heading(9,text="Branch")
table.column(9, width=60)


def buttonevent(selection):
    print("student Roll_No ",E1.get())
    print("student name ", E2.get())
   # print("student gender ", E3.get()) We will not print this because we are selecting it using combobox
    print("student email",E4.get())
    print("student contact ", E5.get())
    print("student DOB", E6.get())
    print("student address", E7.get())
   # print("student class", EE8.get())
   # print("student branch", E8.get())
    Roll_No= E1.get()
    name = E2.get()
    gender = E3.get()
    email = E4.get()
    contact = E5.get()
    DOB = E6.get()
    address = E7.get()
    stud_class=EE8.get()
    branch = E8.get()
    searchby = E9.get()
    search = E10.get()




    # # get_cursor method starts here
    # def get_cursor(self,ev):
    #     cursor_row = self.table.focus()
    #     contents = self.table.item(cursor_row)
    #     row = contents['values']
    #     self.Roll_No.set(row[0])
    #     self.name.set(row[1])
    #     self.gender.set(row[2])
    #     self.email.set(row[3])
    #     self.contact.set(row[4])
    #     self.DOB.set(row[5])
    #     self.address.set(row[6])
    #     self.stud_class.set(row[7])
    #     self.branch.set(row[8])



    if selection in ('INSERT'):
        mycon = sql.connect(host='localhost', user='root', password='root', database='project')
        cur = mycon.cursor()
        for record in table.get_children():
            table.delete(record)
        q = "select * from  record order by Roll_No"

        query = "create table if not exists record(Roll_No varchar(75) Not null,NAME varchar(20), GENDER varchar(30),EMAIL varchar(100),CONTACT varchar(30),DOB varchar(30),ADDRESS varchar(30),stud_class varchar(15),BRANCH varchar(30))"

        cur.execute(query)
        print("table record created ")

        # inquery = "insert into record (Roll_No,NAME,GENDER,EMAIL,CONTACT,DOB,ADDRESS,stud_class,BRANCH) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s' )" % (
        # Roll_No, name, gender, email, contact, DOB, address, stud_class, branch)
        # cur.execute(inquery)
        # cur.execute(q)
        # rows = cur.fetchall()
        # for i in rows:
        #     table.insert('', 'end', values=i)
        #
        # E1.delete(0, END)
        # E2.delete(0, END)
        # E3.delete(0, END)
        # E4.delete(0, END)
        # E5.delete(0, END)
        # E6.delete(0, END)
        # E7.delete(0, END)
        # E8.delete(0, END)
        # mycon.commit()
        # messagebox.showinfo("Success", "Data Inserted Successfully!")
        # mycon.close()

        if Roll_No=="" or name=="" or gender=="" or email=="" or contact=="" or DOB=="" or address=="" or stud_class=="" or branch=="":
            messagebox.showerror("Error","All Fields are compulsory")
        else:
            inquery = "insert into record (Roll_No,NAME,GENDER,EMAIL,CONTACT,DOB,ADDRESS,stud_class,BRANCH) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s' )" % (
            Roll_No, name, gender, email, contact, DOB, address, stud_class, branch)
            cur.execute(inquery)
            cur.execute(q)
            rows = cur.fetchall()
            for i in rows:
                table.insert('', 'end', values=i)

            E1.delete(0, END)
            E2.delete(0, END)
            E3.delete(0, END)
            E4.delete(0, END)
            E5.delete(0, END)
            E6.delete(0, END)
            E7.delete(0, END)
            E8.delete(0, END)
            mycon.commit()
            messagebox.showinfo("Success", "Data Inserted Successfully!")
            mycon.close()
    elif selection in ('UPDATE'):
        qshow = "SELECT * from record  where Roll_No ='%s'" % (Roll_No)
        for record in table.get_children():
            table.delete(record)
        #new
        if Roll_No=="" or name=="" or gender=="" or email=="" or contact=="" or DOB=="" or address=="" or stud_class=="" or branch=="":
            messagebox.showerror("Error","All Fields are compulsory")
        else:
            qupdate = "update record set NAME='%s'" % (name) + ",GENDER='%s'" % (gender) + ",EMAIL='%s'" % (
                email) + ",CONTACT='%s'" % (contact) + ",DOB='%s'" % (DOB) + ",ADDRESS='%s'" % (
                          address) +",stud_class='%s'" % (stud_class) + ",BRANCH='%s'" % (branch) + "where Roll_No ='%s'" % (Roll_No)
            mycon = sql.connect(host='localhost', user='root', password='root', database='project')
            cur = mycon.cursor()
            for record in table.get_children():
                table.delete(record)

            cur.execute(qupdate)
            cur.execute(qshow)
            rows = cur.fetchall()

            for i in rows:
                table.insert('', 'end', values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6],i[7],i[8]))
            E1.delete(0, END)
            E2.delete(0, END)
            E3.delete(0, END)
            E4.delete(0, END)
            E5.delete(0, END)
            E6.delete(0, END)
            E7.delete(0, END)
            EE8.delete(0, END)
            E8.delete(0, END)

            mycon.commit()
            messagebox.showinfo("Success", "Data Updated Successfully!")
            mycon.close()
    elif selection in ('DELETE'):
        q = "select * from record order by Roll_No"
        qdelete = "delete from record  where Roll_No ='%s'" % (Roll_No)
        for record in table.get_children():
            table.delete(record)
        mycon = sql.connect(host='localhost', user='root', password='root', database='project')
        cur = mycon.cursor()
        cur.execute(qdelete)
        cur.execute(q)
        rows = cur.fetchall()

        for i in rows:
            table.insert('', 'end', values=(i))
        mycon.commit()
        messagebox.showinfo("Success", "Data Deleted Successfully!")
        mycon.close()

    elif selection in ('SEARCH'):
        if (searchby == "Roll_No") :
            qsearch = "SELECT * from record  where Roll_No ='%s'" % (search)

        elif (searchby == "Name") :
            qsearch = "SELECT * from record  where Name ='%s'" % (search)

        elif (searchby == "Contact") :
            qsearch = "SELECT * from record  where Contact ='%s'" % (search)

        for record in table.get_children():
            table.delete(record)
        mycon = sql.connect(host='localhost', user='root', password='root', database='project')
        cur = mycon.cursor()
        cur.execute(qsearch)
        rows = cur.fetchall()

        for i in rows:
            table.insert('', 'end', values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7],i[8]))

        mycon.close()
    elif selection in ('SHOWALL'):
        qshowall = "SELECT * from record order by Roll_No"
        for record in table.get_children():
            table.delete(record)
        mycon = sql.connect(host='localhost', user='root', password='root', database='project')
        cur = mycon.cursor()
        cur.execute(qshowall)
        rows = cur.fetchall()

        for i in rows:
            table.insert('', 'end', values=(i))

        mycon.close()

    elif selection in ('About Us'):
        def hellocallback():
            messagebox.showinfo("About Us","Project Name:- Student Record Management System\nProject By:-\n1)Borawake Tushar Prashant\n2)Khomane Pratik Balaso\n3)Chaudhari Rahul Deepak\n4)Kokare Ganesh Dhananjay\n      --- Thank You ---")

        hellocallback()

    elif selection in ('Exit'):
         quit()

Binsert=tkinter.Button(top,text='INSERT',fg='black',font=('arial',20),activebackground='Red',command=lambda:buttonevent('INSERT'))
Binsert.place(x=1300,y=100)

Bupdate=tkinter.Button(top,text='UPDATE',fg='black',font=('arial',20),activebackground='Red',command=lambda: buttonevent('UPDATE') )
Bupdate.place(x=1300,y=170)

Bdelete=tkinter.Button(top,text='DELETE',fg='black',font=('arial',20),activebackground='Red',command=lambda: buttonevent('DELETE'))
Bdelete.place(x=1300,y=240)

Bsearch=tkinter.Button(top,text='SEARCH',fg='black',font=('arial',20),activebackground='Red',command=lambda: buttonevent('SEARCH'))
Bsearch.place(x=1300,y=310)

Bshowall=tkinter.Button(top,text='SHOWALL',fg='black',font=('arial',20),activebackground='Red',command=lambda: buttonevent('SHOWALL'))
Bshowall.place(x=1300,y=380)

Bexit =tkinter.Button(top,text='Exit',fg='black',font=('arial',20),activebackground='Red',command=lambda: buttonevent('Exit'))
Bexit.place(x=1450,y=30)

top.title("Student Record Management System")

top.mainloop()
