from tkinter import *
from tkinter import ttk
import tkinter

import mysql.connector as sql
from PIL import ImageTk,Image

from tkinter import messagebox

#for Student window

def student_win():
    top = tkinter.Toplevel()
    top.geometry("1930x1030")
    top.configure(bg='#B2EF6D')
    l = Label(top, text="Student Record Section", font=('Agency FB', 40),padx=20, fg='white', bg='#08C030', bd=12,
              relief=GROOVE)
    l.place(x=560, y=5)

    l1 = Label(top, text="Student Roll No.:", font=('arial', 30), fg='black', bg='#B2EF6D')
    l1.place(x=5, y=100)
    E1 = Entry(top, bd=10, width=50, font=10)
    E1.place(x=500, y=100)

    l2 = Label(top, text="Student Name:", font=('arial', 30), fg='black', bg='#B2EF6D')
    l2.place(x=5, y=160)
    E2 = Entry(top, bd=10, width=50, font=10)
    E2.place(x=500, y=160)

    l3 = Label(top, text="Student Gender:", font=('arial', 30), fg='black', bg='#B2EF6D')
    l3.place(x=5, y=220)
    E3 = ttk.Combobox(top, font=('arial', 15), width=50, state='readonly', )
    E3['values'] = ("Male", "Female")
    E3.place(x=500, y=220)

    l4 = Label(top, text="Student Email:", font=('arial', 30), fg='black', bg='#B2EF6D')
    l4.place(x=5, y=280)
    E4 = Entry(top, bd=10, width=50, font=10)
    E4.place(x=500, y=280)

    l5 = Label(top, text="Student Contact:", font=('arial', 30), fg='black', bg='#B2EF6D')
    l5.place(x=5, y=350)
    E5 = Entry(top, bd=10, width=50, font=10)
    E5.place(x=500, y=350)

    l6 = Label(top, text="Student DOB:", font=('arial', 30), fg='black', bg='#B2EF6D')
    l6.place(x=5, y=420)
    E6 = Entry(top, bd=10, width=50, font=10)
    E6.place(x=500, y=420)

    l7 = Label(top, text="Student Address:", font=('arial', 30), fg='black', bg='#B2EF6D')
    l7.place(x=5, y=480)
    E7 = Entry(top, bd=10, width=50, font=10)
    E7.place(x=500, y=480)

    l8 = Label(top, text="Student Branch:", font=('arial', 30), fg='black', bg='#B2EF6D')
    l8.place(x=5, y=540)
    E8 = ttk.Combobox(top, font=('arial', 15), width=50, state='readonly', )
    E8['values'] = ("Computer","IT","Electrical","ENTC","Mechanical","Civil")
    E8.place(x=500, y=540)

    l9 = Label(top, text="Search By:", font=('arial', 15), fg='black', bg='#B2EF6D')
    l9.place(x=5, y=620)
    E9 = ttk.Combobox(top, font=('arial', 15), width=10, state='readonly', )
    E9['values'] = ("Roll No", "Name", "Contact")
    E9.place(x=7, y=650)

    E10 = Entry(top, bd=10, width=10, font=10)
    E10.place(x=7, y=700)

    frm = Frame(top)
    table = ttk.Treeview(frm, column=(1, 2, 3, 4, 5, 6, 7, 8), show="headings", height="9", )
    yscrollbar = ttk.Scrollbar(frm, orient='vertical', command=table.yview())
    frm.place(x=150, y=600, width=1200, height=190)
    table.configure(yscroll=yscrollbar.set)
    table.grid(row=11, column=1, )
    yscrollbar.grid(row=11, column=2, sticky="ns")
    table.heading(1, text="Roll No")
    table.column(1, width=60)
    table.heading(2, text="Name")
    table.heading(3, text="Gender")
    table.column(3, width=60)
    table.heading(4, text="Email")
    table.heading(5, text="Contact")
    table.heading(6, text="DOB")
    table.heading(7, text="Address")
    table.heading(8, text="Branch")
    table.column(8, width=60)

    def buttonevent(selection):
        print("student Roll_No ", E1.get())
        print("student name ", E2.get())
        # print("student gender ", E3.get()) We will not print this because we are selecting it using combobox
        print("student email", E4.get())
        print("student contact ", E5.get())
        print("student DOB", E6.get())
        print("student address", E7.get())
        # print("student branch", E8.get())
        Roll_No = E1.get()
        name = E2.get()
        gender = E3.get()
        email = E4.get()
        contact = E5.get()
        DOB = E6.get()
        address = E7.get()
        branch = E8.get()
        searchby = E9.get()
        search = E10.get()
        if selection in ('INSERT'):
            mycon = sql.connect(host='localhost', user='root', password='root', database='My_University')
            cur = mycon.cursor()
            for record in table.get_children():
                table.delete(record)
            q = "select * from  student_record order by Roll_No"

            query = "create table if not exists student_record(Roll_No varchar(75) Not null,NAME varchar(20), GENDER varchar(30),EMAIL varchar(100),CONTACT varchar(30),DOB varchar(30),ADDRESS varchar(30),BRANCH varchar(30))"

            cur.execute(query)

            mycon.commit()
            messagebox.showinfo("Success", "Data Inserted Successfully!")
            print("table student_record created ")

            inquery = "insert into student_record (Roll_No,NAME,GENDER,EMAIL,CONTACT,DOB,ADDRESS,BRANCH) values ('%s','%s','%s','%s','%s','%s','%s','%s' )" % (
                Roll_No, name, gender, email, contact, DOB, address, branch)
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
            mycon.close()
        elif selection in ('UPDATE'):
            qshow = "SELECT * from student_record  where Roll_No ='%s'" % (Roll_No)
            for record in table.get_children():
                table.delete(record)
            qupdate = "update student_record set NAME='%s'" % (name) + ",GENDER='%s'" % (gender) + ",EMAIL='%s'" % (
                email) + ",CONTACT='%s'" % (contact) + ",DOB='%s'" % (DOB) + ",ADDRESS='%s'" % (
                          address) + ",BRANCH='%s'" % (branch) + "where Roll_No ='%s'" % (Roll_No)
            mycon = sql.connect(host='localhost', user='root', password='root', database='My_University')
            cur = mycon.cursor()
            for record in table.get_children():
                table.delete(record)

            cur.execute(qupdate)
            cur.execute(qshow)
            rows = cur.fetchall()

            for i in rows:
                table.insert('', 'end', values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
            E1.delete(0, END)
            E2.delete(0, END)
            E3.delete(0, END)
            E4.delete(0, END)
            E5.delete(0, END)
            E6.delete(0, END)
            E7.delete(0, END)
            E8.delete(0, END)

            mycon.commit()
            messagebox.showinfo("Success", "Data Updated Successfully!")
            mycon.close()
        elif selection in ('DELETE'):
            q = "select * from student_record order by Roll_No"
            qdelete = "delete from student_record  where Roll_No ='%s'" % (Roll_No)
            for record in table.get_children():
                table.delete(record)
            mycon = sql.connect(host='localhost', user='root', password='root', database='My_University')
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
            if(searchby == "Roll No"):
                qsearch = "SELECT * from student_record  where Roll_No = '%s' " % (search)
            elif(searchby == "Name"):
                qsearch = "SELECT * from student_record  where Name = '%s' " % (search)
            elif(searchby == "Contact"):
                qsearch = "SELECT * from student_record  where Contact = '%s' " % (search)
            for record in table.get_children():
                table.delete(record)
            mycon = sql.connect(host='localhost', user='root', password='root', database='My_University')
            cur = mycon.cursor()
            cur.execute(qsearch)
            rows = cur.fetchall()

            for i in rows:
                table.insert('', 'end', values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))

            mycon.close()
        elif selection in ('SHOWALL'):
            qshowall = "SELECT * from student_record order by Roll_No"
            for record in table.get_children():
                table.delete(record)
            mycon = sql.connect(host='localhost', user='root', password='root', database='My_University')
            cur = mycon.cursor()
            cur.execute(qshowall)
            rows = cur.fetchall()

            for i in rows:
                table.insert('', 'end', values=(i))

            mycon.close()

        elif selection in ('Back'):
            top.destroy()

    Binsert = tkinter.Button(top, text='INSERT', fg='white',background='#01BA11', font=('arial', 20), activebackground='#EDC6D2',
                             command=lambda: buttonevent('INSERT'))
    Binsert.place(x=1300, y=100)

    #Images used in the window

    img = Image.open("Images/Insertforstudent.jpg")
    img = img.resize((60, 50))  # Insert
    img = ImageTk.PhotoImage(img)
    tkinter.Label(top, image=img).place(x=1230, y=100)

    Bupdate = tkinter.Button(top, text='UPDATE', fg='white',background='#EDBF12', font=('arial', 20), activebackground='#EDC6D2',
                             command=lambda: buttonevent('UPDATE'))
    Bupdate.place(x=1300, y=170)

    img1 = Image.open("Images/Updateforstudent.jpg")
    img1 = img1.resize((60, 50))  # Update
    img1 = ImageTk.PhotoImage(img1)
    tkinter.Label(top, image=img1).place(x=1230, y=170)

    Bdelete = tkinter.Button(top, text='DELETE', fg='white',background='red', font=('arial', 20), activebackground='#EDC6D2',
                             command=lambda: buttonevent('DELETE'))
    Bdelete.place(x=1300, y=240)

    img2 = Image.open("Images/Deleteforstudent.jpg")
    img2 = img2.resize((60, 50))  # Delete
    img2 = ImageTk.PhotoImage(img2)
    tkinter.Label(top, image=img2).place(x=1230, y=240)

    Bsearch = tkinter.Button(top, text='SEARCH', fg='white',background='#F94BF2', font=('arial', 20), activebackground='#EDC6D2',
                             command=lambda: buttonevent('SEARCH'))
    Bsearch.place(x=1300, y=310)

    img3 = Image.open("Images/Searchforstudent.jpg")
    img3 = img3.resize((60, 50))  # Search
    img3 = ImageTk.PhotoImage(img3)
    tkinter.Label(top, image=img3).place(x=1230, y=310)

    Bshowall = tkinter.Button(top, text='SHOWALL', fg='white',background='#2EB2EE', font=('arial', 20), activebackground='#EDC6D2',
                              command=lambda: buttonevent('SHOWALL'))
    Bshowall.place(x=1300, y=380)

    img4 = Image.open("Images/showallforstudent.jpg")
    img4 = img4.resize((60, 50))  # Showall
    img4 = ImageTk.PhotoImage(img4)
    tkinter.Label(top, image=img4).place(x=1230, y=380)

    Bback = tkinter.Button(top, text='Back', fg='white',background='#FC5787', font=('arial', 20), activebackground='#EDC6D2',
                           command=lambda: buttonevent('Back'))
    Bback.place(x=1430, y=30)

    img5 = Image.open("Images/StudentforStudent.jpg")
    img5 = img5.resize((80, 80))  # Student
    img5 = ImageTk.PhotoImage(img5)
    tkinter.Label(top, image=img5).place(x=470, y=5)

    img6 = Image.open("Images/Backforstudent.jpg")
    img6 = img6.resize((55, 55))  # Exit
    img6 = ImageTk.PhotoImage(img6)
    tkinter.Label(top, image=img6).place(x=1360, y=30).pack() #pack() method prevents the image to be collected by garbage collector

    top.title("Student")

# For Faculty Window
def faculty_win():
    top = tkinter.Toplevel()
    top.geometry("1930x1030")
    top.configure(bg='#FFDF43')

    s = Label(top, text="Faculty Record Section", font=('Agency FB', 40), padx=20, fg='white', bg='#FFC100', bd=12, relief=GROOVE)
    s.place(x=600, y=5)

    s1 = Label(top, text="Faculty ID:", font=('arial', 25), fg='black', bg='#FFDF43')
    s1.place(x=8, y=113)
    F1 = Entry(top, bd=10, width=50, font=10)
    F1.place(x=500, y=110)

    s2 = Label(top, text="Faculty Name:", font=('arial', 25), fg='black', bg='#FFDF43')
    s2.place(x=8, y=168)
    F2 = Entry(top, bd=10, width=50, font=10)
    F2.place(x=500, y=165)

    s3 = Label(top, text="Faculty Gender:", font=('arial', 25), fg='black', bg='#FFDF43')
    s3.place(x=8, y=223)

    F3 = ttk.Combobox(top, font=('arial', 15), width=41, state='readonly', )
    F3['values'] = ("Male", "Female")
    F3.place(x=500, y=228)

    s4 = Label(top, text="Faculty Email:", font=('arial', 25), fg='black', bg='#FFDF43')
    s4.place(x=5, y=278)
    F4 = Entry(top, bd=10, width=50, font=10)
    F4.place(x=500, y=275)

    s5 = Label(top, text="Faculty Contact:", font=('arial', 25), fg='black', bg='#FFDF43')
    s5.place(x=5, y=333)
    F5 = Entry(top, bd=10, width=50, font=10)
    F5.place(x=500, y=332)

    s6 = Label(top, text="Faculty Qualification:", font=('arial', 25), fg='black', bg='#FFDF43')
    s6.place(x=5, y=388)
    F6 = Entry(top, bd=10, width=50, font=10)
    F6.place(x=500, y=389)

    s7 = Label(top, text="Faculty Department:", font=('arial', 25), fg='black', bg='#FFDF43')
    s7.place(x=5, y=443)
    F7 = ttk.Combobox(top, font=('arial', 15), width=50, state='readonly', )
    F7['values'] = ("Computer", "IT", "ENTC", "MECH.", "ELECTRICAL", "CIVIL", "AI")
    F7.place(x=500, y=453)

    s8 = Label(top, text="Search By:", font=('Agency FB', 30), fg='Red', bg='#FFDF43')
    s8.place(x=350, y=515)
    F8 = ttk.Combobox(top, font=('arial', 15), width=10, state='readonly', )
    F8['values'] = ("Faculty ID", "Name", "Contact")
    F8.place(x=520, y=530)

    F9 = Entry(top, bd=10, width=10, font=10)
    F9.place(x=700, y=520)

    frm = Frame(top)
    table = ttk.Treeview(frm, column=(1, 2, 3, 4, 5, 6, 7), show="headings", height="9", )
    yscrollbar = ttk.Scrollbar(frm, orient='vertical', command=table.yview())
    frm.place(x=190, y=600, width=1145, height=190)
    table.configure(yscroll=yscrollbar.set)
    table.grid(row=11, column=1, )
    yscrollbar.grid(row=11, column=2, sticky="ns")
    table.heading(1, text="ID")
    table.column(1, width=60)
    table.heading(2, text="Name")
    table.heading(3, text="Gender")
    table.column(3, width=60)
    table.heading(4, text="Email")
    table.heading(5, text="Contact")
    table.heading(6, text="Qualification")

    table.heading(7, text="Branch")

    def buttonevent(selection):
        print("Faculty ID ", F1.get())
        print("Faculty Name ", F2.get())
        # print("Faculty Gender ", F3.get()) We will not print this because we are selecting it using combobox
        print("Faculty email", F4.get())
        print("Faculty Contact ", F5.get())
        print("Faculty Qualification", F6.get())
        print("Faculty Branch", F7.get())

        faculty_ID = F1.get()
        name = F2.get()
        gender = F3.get()
        email = F4.get()
        contact = F5.get()
        qualification = F6.get()
        branch = F7.get()
        searchby=F8.get()
        search=F9.get()

        if selection in ('INSERT'):
            mycon = sql.connect(host='localhost', user='root', password='root', database='my_university')
            cur = mycon.cursor()
            for record in table.get_children():
                table.delete(record)
            q = "select * from  faculty_record order by Faculty_ID"

            queryf = "create table if not exists faculty_record(Faculty_ID varchar(75) Not null,Faculty_Name varchar(20), Faculty_Gender varchar(30),Faculty_email varchar(100),Faculty_Contact varchar(30),Faculty_Qualification varchar(30), Faculty_Branch varchar(30))"

            cur.execute(queryf)

            mycon.commit()
            messagebox.showinfo("Success", "Data Inserted Successfully!")
            print("table faculty_record created ")

            inquery = "insert into faculty_record (Faculty_ID,Faculty_Name, Faculty_Gender,Faculty_email,Faculty_Contact,Faculty_Qualification,Faculty_Branch) values ('%s','%s','%s','%s','%s','%s','%s')" % (
                faculty_ID, name, gender, email, contact, qualification, branch)
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
            qshowf = "SELECT * from Faculty_record where faculty_ID ='%s'" % (faculty_ID)
            for record in table.get_children():
                table.delete(record)
            qupdatef = "update Faculty_record set Faculty_Name='%s'" % (name) + ",Faculty_Gender='%s'" % (gender) + ",Faculty_email='%s'" % (
                email) + ",Faculty_Contact='%s'" % (contact) + ",Faculty_Qualification='%s'" % (qualification) + ",Faculty_Branch='%s'" % (
                           branch) + "where faculty_ID ='%s'" % (faculty_ID)
            mycon = sql.connect(host='localhost', user='root', password='root', database='my_university')
            cur = mycon.cursor()
            for record in table.get_children():
                table.delete(record)

            cur.execute(qupdatef)
            cur.execute(qshowf)
            rows = cur.fetchall()

            for i in rows:
                table.insert('', 'end', values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6],))
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

        elif selection in ('DELETE'):
            q = "select * from faculty_record order by faculty_ID"
            qdelete = "delete from faculty_record  where faculty_ID ='%s'" % (faculty_ID)
            for record in table.get_children():
                table.delete(record)
            mycon = sql.connect(host='localhost', user='root', password='root', database='My_University')
            cur = mycon.cursor()
            cur.execute(qdelete)
            cur.execute(q)
            rows = cur.fetchall()

            for i in rows:
                table.insert('', 'end', values=(i))
            mycon.commit()
            messagebox.showinfo("Success", "Faculty Data Deleted Successfully!")
            mycon.close()

        elif selection in ('SEARCH'):
            if(searchby == "Faculty ID"):
                qsearch = "SELECT * from faculty_record where faculty_ID = '%s' " % (search)
            elif(searchby == "Name"):
                qsearch = "SELECT * from faculty_record where Faculty_Name = '%s' " % (search)
            elif(searchby == "Contact"):
                qsearch = "SELECT * from faculty_record where Faculty_Contact = '%s' " % (search)
            for record in table.get_children():
                table.delete(record)
            mycon = sql.connect(host='localhost', user='root', password='root', database='My_University')
            cur = mycon.cursor()
            cur.execute(qsearch)
            rows = cur.fetchall()

            for i in rows:
                table.insert('', 'end', values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6],))

            mycon.close()

        elif selection in ('SHOWALL'):
            qshowall = "SELECT * from faculty_record order by faculty_ID"
            for record in table.get_children():
                table.delete(record)
            mycon = sql.connect(host='localhost', user='root', password='root', database='My_University')
            cur = mycon.cursor()
            cur.execute(qshowall)
            rows = cur.fetchall()

            for i in rows:
                table.insert('', 'end', values=(i))

            mycon.close()

        elif selection in ('Back'):
            top.destroy()

    Finsert = tkinter.Button(top, text='INSERT',background='#01BA11',fg='black', font=('arial', 20), activebackground='Red',
                             command=lambda: buttonevent('INSERT'))
    Finsert.place(x=1300, y=100)

    img = Image.open("Images/Insertforfaculty.jpg")
    img = img.resize((60, 50))  # Insert
    img = ImageTk.PhotoImage(img)
    tkinter.Label(top, image=img).place(x=1230, y=100)

    Fupdate = tkinter.Button(top, text='UPDATE', background='#EDBF12',fg='black', font=('arial', 20), activebackground='Red',
                             command=lambda: buttonevent('UPDATE'))
    Fupdate.place(x=1300, y=170)

    img1 = Image.open("Images/Updateforfaculty.jpg")
    img1 = img1.resize((60, 50))  # Update
    img1 = ImageTk.PhotoImage(img1)
    tkinter.Label(top, image=img1).place(x=1230, y=170)

    Fdelete = tkinter.Button(top, text='DELETE', background='red', fg='black', font=('arial', 20), activebackground='Red',
                             command=lambda: buttonevent('DELETE'))
    Fdelete.place(x=1300, y=240)

    img2 = Image.open("Images/Deleteforfaculty.jpg")
    img2 = img2.resize((60, 50))  # Delete
    img2 = ImageTk.PhotoImage(img2)
    tkinter.Label(top, image=img2).place(x=1230, y=240)

    Fsearch = tkinter.Button(top, text='SEARCH',background='#F94BF2', fg='black', font=('arial', 20), activebackground='Red',
                             command=lambda: buttonevent('SEARCH'))
    Fsearch.place(x=1300, y=310)

    img3 = Image.open("Images/Searchforfaculty.jpg")
    img3 = img3.resize((60, 50))  # Search
    img3 = ImageTk.PhotoImage(img3)
    tkinter.Label(top, image=img3).place(x=1230, y=310)

    Fshowall = tkinter.Button(top, text='SHOWALL', fg='black',background='#2EB2EE', font=('arial', 20), activebackground='Red',
                              command=lambda: buttonevent('SHOWALL'))
    Fshowall.place(x=1300, y=380)

    img4 = Image.open("Images/showallforfaculty.jpg")
    img4 = img4.resize((60, 50))  # Showall
    img4 = ImageTk.PhotoImage(img4)
    tkinter.Label(top, image=img4).place(x=1230, y=380)

    Fback = tkinter.Button(top, text='Back', fg='black',background='#FC5787', font=('arial', 20), activebackground='Red',
                           command=lambda: buttonevent('Back'))
    Fback.place(x=1430, y=30)

    img6 = Image.open("Images/Backforfaculty.jpg")
    img6 = img6.resize((55, 55))  # Faculty
    img6 = ImageTk.PhotoImage(img6)
    tkinter.Label(top, image=img6).place(x=1365, y=30)

    img5 = Image.open("Images/Faculty.jpg")
    img5 = img5.resize((82, 82))  # Faculty
    img5 = ImageTk.PhotoImage(img5)
    tkinter.Label(top, image=img5).place(x=500, y=5).pack()

    top.title("Faculty")

#for Department window

def department_win():
    top = tkinter.Toplevel()
    top.geometry("1930x1030")
    top.configure(bg='#14D5FF')
    l = Label(top, text="Department Record Section", font=('Agency FB', 40),padx=20, fg='white', bg='#11B6DA', bd=12,
              relief=GROOVE)
    l.place(x=560, y=30)

    l1 = Label(top, text="Department ID:", font=('arial', 30), fg='black', bg='#14D5FF')
    l1.place(x=5, y=150)
    D1 = Entry(top, bd=10, width=50, font=10)
    D1.place(x=500, y=150)

    l2 = Label(top, text="Department Name:", font=('arial', 30), fg='black', bg='#14D5FF')
    l2.place(x=5, y=210)
    D2 = Entry(top, bd=10, width=50, font=10)
    D2.place(x=500, y=210)

    # Table
    frame = Frame(top)
    frame.pack(pady=20)

    tv = ttk.Treeview(frame, columns=(1, 2), show='headings', height=5)
    tv.pack(side=LEFT)

    tv.heading(1, text="Department ID")
    tv.column(1, width=150)
    tv.heading(2, text="Department Name")
    tv.column(2, width=250)

    sb = Scrollbar(frame, orient=VERTICAL)
    sb.pack(side=RIGHT, fill=Y)

    tv.config(yscrollcommand=sb.set)
    sb.config(command=tv.yview)
    frame.place(x=600, y=500)

    def buttonevent(selection):
        print("Department ID", D1.get())
        print("Department Name", D2.get())

        Did = D1.get()
        Dname = D2.get()
        if selection in ('ADD'):
            mycon = sql.connect(host='localhost', user='root', password='root', database='My_University')
            cur = mycon.cursor()
            for record in tv.get_children():
                tv.delete(record)
            q = "select * from department_record order by Did"

            queryd = "create table if not exists department_record(Did varchar(20) Not null, Dname varchar(20))"

            cur.execute(queryd)

            mycon.commit()
            messagebox.showinfo("Success", "Department Added Successfully!")
            print("table department_record created ")

            inquery = "insert into department_record(Did,Dname) values ('%s','%s')" % (Did, Dname)
            cur.execute(inquery)
            cur.execute(q)
            rows = cur.fetchall()
            for i in rows:
                tv.insert('', 'end', values=i)

            D1.delete(0, END)
            D2.delete(0, END)
            mycon.commit()
            mycon.close()

        elif selection in ('UPDATE'):
            qshowd = "SELECT * from department_record  where Did ='%s'" % (Did)
            for record in tv.get_children():
                tv.delete(record)
            qupdated = "update department_record set Dname='%s'" % (Dname) + "where Did ='%s'" % (Did)

            mycon = sql.connect(host='localhost', user='root', password='root', database='my_university')
            cur = mycon.cursor()
            for record in tv.get_children():
                tv.delete(record)

            cur.execute(qupdated)
            cur.execute(qshowd)
            rows = cur.fetchall()

            for i in rows:
                tv.insert('', 'end', values=(i[0], i[1]))
            D1.delete(0, END)
            D2.delete(0, END)

            mycon.commit()
            messagebox.showinfo("Success", "Department Updated Successfully!")
            mycon.close()

        elif selection in ('DELETE'):
            q = "select * from department_record order by Did"
            qdelete = "delete from department_record where Did ='%s'" % (Did)
            for record in tv.get_children():
                tv.delete(record)
            mycon = sql.connect(host='localhost', user='root', password='root', database='My_University')
            cur = mycon.cursor()
            cur.execute(qdelete)
            cur.execute(q)
            rows = cur.fetchall()

            for i in rows:
                tv.insert('', 'end', values=(i))
            mycon.commit()
            messagebox.showinfo("Success", "Department Deleted Successfully!")
            mycon.close()

        elif selection in ('SHOWALL'):
            qshowalld = "SELECT * from department_record order by Did"
            for record in tv.get_children():
                tv.delete(record)
            mycon = sql.connect(host='localhost', user='root', password='root', database='My_University')
            cur = mycon.cursor()
            cur.execute(qshowalld)
            rows = cur.fetchall()

            for i in rows:
                tv.insert('', 'end', values=(i))

            mycon.close()

        elif selection in ('Back'):
            top.destroy()

    # Buttons
    Dadd = tkinter.Button(top, text='ADD', fg='white', background='#01BA11', font=('arial', 20),
                             activebackground='#EDC6D2',command=lambda: buttonevent('ADD'))
    Dadd.place(x=1300, y=100)

    # Images used in the window
    img = Image.open("Images/Addfordepartment.jpg")
    img = img.resize((60, 50))  # Add
    img = ImageTk.PhotoImage(img)
    tkinter.Label(top, image=img).place(x=1230, y=100)

    Dupdate = tkinter.Button(top, text='UPDATE', fg='white', background='#EDBF12', font=('arial', 20),
                             activebackground='#EDC6D2',command=lambda: buttonevent('UPDATE'))
    Dupdate.place(x=1300, y=170)

    img1 = Image.open("Images/Updatefordepartment.jpg")
    img1 = img1.resize((60, 50))  # Update
    img1 = ImageTk.PhotoImage(img1)
    tkinter.Label(top, image=img1).place(x=1230, y=170)

    Ddelete = tkinter.Button(top, text='DELETE', fg='white', background='red', font=('arial', 20),
                             activebackground='#EDC6D2',command=lambda: buttonevent('DELETE'))
    Ddelete.place(x=1300, y=240)

    img2 = Image.open("Images/Deletefordepartment.jpg")
    img2 = img2.resize((60, 50))  # Delete
    img2 = ImageTk.PhotoImage(img2)
    tkinter.Label(top, image=img2).place(x=1230, y=240)

    Dshowall = tkinter.Button(top, text='SHOWALL', fg='white', background='#2EB2EE', font=('arial', 20),
                              activebackground='#EDC6D2',command=lambda: buttonevent('SHOWALL'))
    Dshowall.place(x=1300, y=310)

    img4 = Image.open("Images/showallfordepartment.jpg")
    img4 = img4.resize((60, 50))  # Showall
    img4 = ImageTk.PhotoImage(img4)
    tkinter.Label(top, image=img4).place(x=1230, y=310)

    Dback = tkinter.Button(top, text='Back', fg='black', background='#FC5787', font=('arial', 20), activebackground='Red',
                           command=lambda: buttonevent('Back'))
    Dback.place(x=1430, y=30)

    img6 = Image.open("Images/Backfordepartment.jpg")
    img6 = img6.resize((55, 55))  # Exit
    img6 = ImageTk.PhotoImage(img6)
    tkinter.Label(top, image=img6).place(x=1360, y=30)

    img5 = Image.open("Images/Department.jpg")
    img5 = img5.resize((80, 80))  # Department
    img5 = ImageTk.PhotoImage(img5)
    tkinter.Label(top, image=img5).place(x=470, y=30).pack()

    top.title("Department")

#For Course Window

def Course_win():
    top = tkinter.Toplevel()
    top.geometry("1930x1030")
    top.configure(bg='#DA97F8')
    l = Label(top, text="Course Record Section", font=('Agency FB', 40),padx=20, fg='white', bg='#C14CF5', bd=12,
              relief=GROOVE)
    l.place(x=560, y=30)

    l1 = Label(top, text="Course ID:", font=('arial', 30), fg='black', bg='#DA97F8')
    l1.place(x=5, y=150)
    D1 = Entry(top, bd=10, width=50, font=10)
    D1.place(x=500, y=150)

    l2 = Label(top, text="Course Name:", font=('arial', 30), fg='black', bg='#DA97F8')
    l2.place(x=5, y=210)
    D2 = Entry(top, bd=10, width=50, font=10)
    D2.place(x=500, y=210)

    l3 = Label(top, text="Course Year:", font=('arial', 30), fg='black', bg='#DA97F8')
    l3.place(x=5, y=270)
    D3 = Entry(top, bd=10, width=50, font=10)
    D3.place(x=500, y=270)

    # Table
    frame = Frame(top)
    frame.pack(pady=20)

    tv = ttk.Treeview(frame, columns=(1, 2,3), show='headings', height=5)
    tv.pack(side=LEFT)

    tv.heading(1, text="Course ID")
    tv.column(1, width=150)
    tv.heading(2, text="Course Name")
    tv.column(2, width=250)
    tv.heading(3, text="Course Year")
    tv.column(3, width=150)

    sb = Scrollbar(frame, orient=VERTICAL)
    sb.pack(side=RIGHT, fill=Y)

    tv.config(yscrollcommand=sb.set)
    sb.config(command=tv.yview)
    frame.place(x=500, y=500)

    def buttonevent(selection):
        print("Course ID", D1.get())
        print("Course Name", D2.get())
        print("Course Year", D3.get())

        Cid = D1.get()
        Cname = D2.get()
        Cyear = D3.get()
        if selection in ('ADD'):
            mycon = sql.connect(host='localhost', user='root', password='root', database='My_University')
            cur = mycon.cursor()
            for record in tv.get_children():
                tv.delete(record)
            q = "select * from course_record order by Cid"

            queryc = "create table if not exists course_record(Cid varchar(20) Not null, Cname varchar(20),Cyear varchar(20))"

            cur.execute(queryc)

            mycon.commit()
            messagebox.showinfo("Success", "Course Added Successfully!")
            print("table course_record created ")

            inquery = "insert into Course_record(Cid,Cname,Cyear) values ('%s','%s','%s')" % (Cid, Cname,Cyear)
            cur.execute(inquery)
            cur.execute(q)
            rows = cur.fetchall()
            for i in rows:
                tv.insert('', 'end', values=i)

            D1.delete(0, END)
            D2.delete(0, END)
            D3.delete(0, END)
            mycon.commit()
            mycon.close()

        elif selection in ('UPDATE'):
            qshowd = "SELECT * from Course_record  where Cid ='%s'" % (Cid)
            for record in tv.get_children():
                tv.delete(record)
            qupdated = "update Course_record set Cname='%s'" % (Cname) + ",Cyear='%s'" % (Cyear) + "where Cid ='%s'" % (Cid)

            mycon = sql.connect(host='localhost', user='root', password='root', database='my_university')
            cur = mycon.cursor()
            for record in tv.get_children():
                tv.delete(record)

            cur.execute(qupdated)
            cur.execute(qshowd)
            rows = cur.fetchall()

            for i in rows:
                tv.insert('', 'end', values=(i[0], i[1]))
            D1.delete(0, END)
            D2.delete(0, END)
            D3.delete(0, END)

            mycon.commit()
            messagebox.showinfo("Success", "Course Updated Successfully!")
            mycon.close()

        elif selection in ('DELETE'):
            q = "select * from Course_record order by Cid"
            qdelete = "delete from Course_record where Cid ='%s'" % (Cid)
            for record in tv.get_children():
                tv.delete(record)
            mycon = sql.connect(host='localhost', user='root', password='root', database='My_University')
            cur = mycon.cursor()
            cur.execute(qdelete)
            cur.execute(q)
            rows = cur.fetchall()

            for i in rows:
                tv.insert('', 'end', values=(i))
            mycon.commit()
            messagebox.showinfo("Success", "Course Deleted Successfully!")
            mycon.close()

        elif selection in ('SHOWALL'):
            qshowalld = "SELECT * from Course_record order by Cid"
            for record in tv.get_children():
                tv.delete(record)
            mycon = sql.connect(host='localhost', user='root', password='root', database='My_University')
            cur = mycon.cursor()
            cur.execute(qshowalld)
            rows = cur.fetchall()

            for i in rows:
                tv.insert('', 'end', values=(i))

            mycon.close()

        elif selection in ('Back'):
            top.destroy()

    # Buttons
    Dadd = tkinter.Button(top, text='ADD', fg='white', background='#01BA11', font=('arial', 20),
                             activebackground='#EDC6D2',command=lambda: buttonevent('ADD'))
    Dadd.place(x=1300, y=100)

    # Images used in the window
    img = Image.open("Images/Addforcourse.jpg")
    img = img.resize((60, 50))  # Add
    img = ImageTk.PhotoImage(img)
    tkinter.Label(top, image=img).place(x=1230, y=100)

    Dupdate = tkinter.Button(top, text='UPDATE', fg='white', background='#EDBF12', font=('arial', 20),
                             activebackground='#EDC6D2',command=lambda: buttonevent('UPDATE'))
    Dupdate.place(x=1300, y=170)

    img1 = Image.open("Images/Updateforcourse.jpg")
    img1 = img1.resize((60, 50))  # Update
    img1 = ImageTk.PhotoImage(img1)
    tkinter.Label(top, image=img1).place(x=1230, y=170)

    Ddelete = tkinter.Button(top, text='DELETE', fg='white', background='red', font=('arial', 20),
                             activebackground='#EDC6D2',command=lambda: buttonevent('DELETE'))
    Ddelete.place(x=1300, y=240)

    img2 = Image.open("Images/Deleteforcourse.jpg")
    img2 = img2.resize((60, 50))  # Delete
    img2 = ImageTk.PhotoImage(img2)
    tkinter.Label(top, image=img2).place(x=1230, y=240)

    Dshowall = tkinter.Button(top, text='SHOWALL', fg='white', background='#2EB2EE', font=('arial', 20),
                              activebackground='#EDC6D2',command=lambda: buttonevent('SHOWALL'))
    Dshowall.place(x=1300, y=310)

    img4 = Image.open("Images/Showallforcourse.jpg")
    img4 = img4.resize((60, 50))  # Showall
    img4 = ImageTk.PhotoImage(img4)
    tkinter.Label(top, image=img4).place(x=1230, y=310)

    Dback = tkinter.Button(top, text='Back', fg='black', background='#FC5787', font=('arial', 20), activebackground='Red',
                           command=lambda: buttonevent('Back'))
    Dback.place(x=1430, y=30)

    img6 = Image.open("Images/Backforcourse.jpg")
    img6 = img6.resize((58, 55))  # Exit
    img6 = ImageTk.PhotoImage(img6)
    tkinter.Label(top, image=img6).place(x=1360, y=30)

    img5 = Image.open("Images/Course.jpg")
    img5 = img5.resize((80, 80))  # Department
    img5 = ImageTk.PhotoImage(img5)
    tkinter.Label(top, image=img5).place(x=470, y=30).pack()

    top.title("Course")

#For Welcome Page

root = Tk()
root.title("Welcome")
canvas= Canvas(root,width=1920,height=1030)
canvas.pack()

menubar=Menu(root)
Student=Menu(menubar,tearoff=0)
root.config(menu=menubar)
Student.add_command(label="Open Student", command=lambda:student_win())
menubar.add_cascade(label="Student",menu=Student)

Faculty=Menu(menubar,tearoff=0)
root.config(menu=menubar)
Faculty.add_command(label="Open Faculty",command=lambda:faculty_win())
menubar.add_cascade(label="Faculty",menu=Faculty)

Department=Menu(menubar,tearoff=0)
root.config(menu=menubar)
Department.add_command(label="Open Department",command=lambda:department_win())
menubar.add_cascade(label="Department",menu=Department)

Course=Menu(menubar,tearoff=0)
root.config(menu=menubar)
Course.add_command(label="Open Course",command=lambda:Course_win())
menubar.add_cascade(label="Course",menu=Course)

def hellocallback():
    messagebox.showinfo("About Us",
                        "Project Name:- University Database Management System\nProject By:-\n1)Borawake Tushar Prashant\n2)Khomane Pratik Balaso\n3)Chaudhari Rahul Deepak\n"
                        "4)Kokare Ganesh Dhananjay\n      --- Thank You ---")

menubar.add_cascade(label="About Us",command=lambda:hellocallback())
menubar.add_cascade(label="Exit",command=root.quit)

img7=Image.open("Images/University Wallpaper.jpeg")
img7=img7.resize((1550,800)) #Here we have resized the image to fit it in full screen
img7=ImageTk.PhotoImage(img7)
canvas.create_image(0,0,anchor=NW,image=img7)
root.mainloop()


