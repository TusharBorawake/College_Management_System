import tkinter
from tkinter import *
from tkinter import ttk

topresult = tkinter.Tk()
topresult.geometry("1920x1030+0+0")
topresult.configure(bg='pink')
lr= Label(topresult,text ="Student Result Section",font=('arial',30),padx=10,fg='White',bg='violet',bd=10,relief=SUNKEN)
lr.place(x=500,y=5)

lrseatno= Label(topresult,text ="Seat Number :-",font=('arial',25),fg='black',bg='pink')
lrseatno.place(x=160,y=90)
Erseatno = Entry(topresult,bd=10,width=20,font=8)
Erseatno.place(x=400,y=90)


lrrollno= Label(topresult,text ="Roll Number :-",font=('arial',25),fg='black',bg='pink')
lrrollno.place(x=850,y=90)
Errollno = Entry(topresult,bd=10,width=20,font=8)
Errollno.place(x=1080,y=90)

lclass= Label(topresult,text ="Class :-",font=('arial',25),fg='black',bg='pink')
lclass.place(x=160,y=150)
Eclass = ttk.Combobox(topresult,font=('arial',15),width=20,state='readonly',)
Eclass['values']=("FE","SE","TE","BE")
Eclass.place(x=400,y=160)


lbranch= Label(topresult,text ="Branch :-",font=('arial',25),fg='black',bg='pink')
lbranch.place(x=850,y=150)
Ebranch = ttk.Combobox(topresult,font=('arial',15),width=20,state='readonly',)
Ebranch['values']=("Computer","IT","Mechanical","Electrical","ENTC","Civil")
Ebranch.place(x=1080,y=160)

lr1= Label(topresult,text ="Subject Name :-",font=('arial',25),fg='black',bg='pink')
lr1.place(x=20,y=210)
Er1 = Entry(topresult,bd=10,width=30,font=8)
Er1.place(x=500,y=210)

lrm1= Label(topresult,text ="Subject Marks:",font=('arial',25),fg='black',bg='pink')
lrm1.place(x=20,y=260)
Erm1 = Entry(topresult,bd=10,width=10,font=8)
Erm1.place(x=500,y=260)


lr2= Label(topresult,text ="Subject Name:",font=('arial',25),fg='black',bg='pink')
lr2.place(x=20,y=310)
Er2 = Entry(topresult,bd=10,width=30,font=8)
Er2.place(x=500,y=310)

lrm2= Label(topresult,text ="Subject Marks:",font=('arial',25),fg='black',bg='pink')
lrm2.place(x=20,y=360)
Erm2 = Entry(topresult,bd=10,width=10,font=8)
Erm2.place(x=500,y=360)


lr3= Label(topresult,text ="Subject Name:",font=('arial',25),fg='black',bg='pink')
lr3.place(x=20,y=410)
Er3 = Entry(topresult,bd=10,width=30,font=8)
Er3.place(x=500,y=410)

lrm3= Label(topresult,text ="Subject Marks:",font=('arial',25),fg='black',bg='pink')
lrm3.place(x=20,y=460)
Erm3 = Entry(topresult,bd=10,width=10,font=8)
Erm3.place(x=500,y=460)


lr4= Label(topresult,text ="Subject Name:",font=('arial',25),fg='black',bg='pink')
lr4.place(x=20,y=510)
Er4 = Entry(topresult,bd=10,width=30,font=8)
Er4.place(x=500,y=510)

lrm4= Label(topresult,text ="Subject Marks:",font=('arial',25),fg='black',bg='pink')
lrm4.place(x=20,y=560)
Erm4 = Entry(topresult,bd=10,width=10,font=8)
Erm4.place(x=500,y=560)

lr5= Label(topresult,text ="Subject Name:",font=('arial',25),fg='black',bg='pink')
lr5.place(x=20,y=610)
Er5 = Entry(topresult,bd=8,width=30,font=8)
Er5.place(x=500,y=610)

lr5= Label(topresult,text ="Subject Marks:",font=('arial',25),fg='black',bg='pink')
lr5.place(x=20,y=660)
Er5 = Entry(topresult,bd=8,width=10,font=8)
Er5.place(x=500,y=660)

rwgenerateresult=tkinter.Button(topresult,text='Generate Result',fg='white',font=('arial',20),bg='green')
rwgenerateresult.place(x=650 , y=710)



def buttonevent(selection):
    if selection in ('Exit'):
         quit()




Bexit =tkinter.Button(topresult,text='Exit',fg='white',font=('arial',20),back='Red',command=lambda: buttonevent('Exit'))
Bexit.place(x=1450,y=30)

topresult.title("Student Result Section")

topresult.mainloop()
