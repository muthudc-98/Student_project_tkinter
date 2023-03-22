from tkinter import *
import tkinter.font as f
from tkinter import messagebox as m
import mysql.connector

'''mydb=mysql.connector.connect(host='localhost',user='root',password='',database='collegenew')
mycursor=mydb.cursor()'''

a=Tk()
a.title('STUDENT RECORD')
a.resizable(0,0)
a.config(bg='dark green')
a.geometry('900x600')
t=Text(a,width=35,height=50,border=3,bg='light gray',fg='black',font=('consolas',15,'bold'))
t.pack(side='right')
f_1=f.Font(family='arial',size=26,weight='bold')
f_2=f.Font(family='arial',size=16,weight='bold')
lbl_head=Label(a,text='Students Record: ',fg='white',bg='dark green',font=('rockwell',22,'bold'))
lbl_head.place(x=125,y=15)
#lbl_head['font']=f_1
lbl_1=Label(a,text='Roll No.',fg='white',bg='dark green',font=('Times new roman',17,'bold')).place(x=50,y=100)
lbl_2=Label(a,text='Name',fg='white',bg='dark green',font=('times new roman',17,'bold')).place(x=50,y=150)
lbl_3=Label(a,text='Age',fg='white',bg='dark green',font=('times new roman',17,'bold')).place(x=50,y=200)
lbl_4=Label(a,text='City',fg='white',bg='dark green',font=('times new roman',17,'bold')).place(x=50,y=250)
en_1=Entry(a,font=('arial',13),width=12,bg='dark green',fg='white',border=0)
en_2=Entry(a,font=('arial',13),width=12,bg='dark green',fg='white',border=0)
en_3=Entry(a,font=('arial',13),width=12,bg='dark green',fg='white',border=0)
en_4=Entry(a,font=('arial',13),width=12,bg='dark green',fg='white',border=0)
en_1.place(x=150,y=105)
Frame(a,width=140,height=2,bg='black').place(x=150,y=128)
en_2.place(x=150,y=155)
Frame(a,width=140,height=2,bg='black').place(x=150,y=178)
en_3.place(x=150,y=205)
Frame(a,width=140,height=2,bg='black').place(x=150,y=228)
en_4.place(x=150,y=255)
Frame(a,width=140,height=2,bg='black').place(x=150,y=278)

global stu
stu=[]

def find():
    global stu
    try:
        le=len(stu)
        idno=Entry.get(en_1)
        '''mycursor.execute('select * from student where no={}'.format(idno))
        for i in mycursor:
            t.insert(INSERT,i)
        clear()'''
    except:
        m.showerror('Error','Fill the Roll No...!')
def delete():
    global stu
    try:
        idno=Entry.get(en_1)
        '''mycursor.execute('delete from student where no ={}'.format(idno))
        mydb.commit()
        li=len(stu)
        for i in range(li):
            if stu[i][0]==idno:
                stu.pop(i)
                m.showinfo('Deleted',f'{rollno} Deleted')
                break
        clear()'''
    except:
        m.showerror('Error','Fill the Roll No...!')
        
def show():
    '''mycursor.execute('select * from student ')
    res=mycursor.fetchall()
    for i in res:
        #print(i)
        t.insert(INSERT, i)
        t.insert(INSERT, '\n')
    clear()'''
def clear():
    en_1.delete(0,END)
    en_2.delete(0,END)
    en_3.delete(0,END)
    en_4.delete(0,END)

def process():
    if en_1==True and en_2==True and en_3==True and en_4==True:
        idno=Entry.get(en_1)
        name=Entry.get(en_2)
        age=Entry.get(en_3)
        city=Entry.get(en_4)
        rec=[idno,name,age,city]
        stu.append(rec)
        print(stu)
        print('\n')
        t.insert(INSERT, stu)
        '''sql='INSERT INTO student(no,name,age,city) values(%s,%s,%s,%s)'
        val=(idno,name,age,city)
        mycursor.execute(sql,val)
        mydb.commit()
        clear()'''
    else:
        m.showerror('Error','Fill the Empty Fields...')
    
btn_sub=Button(a,text='Submit',font=('Times new roman',15,'bold'),border='5',activeforeground='white',activebackground='green',bg='dark blue',fg='white',command=process)
btn_sub.place(x=25,y=330)
#btn_sub['font']=f_2

btn_sub=Button(a,text='Find',font=('Times new roman',15,'bold'),border='5',activeforeground='white',activebackground='green',bg='dark blue',fg='white',command=find,width=6)
btn_sub.place(x=112,y=330)
#btn_sub['font']=f_2

btn_sub=Button(a,text='Delete',font=('Times new roman',15,'bold'),border='5',activeforeground='white',activebackground='green',bg='dark blue',fg='white',command=delete,width=6)
btn_sub.place(x=205,y=330)
#btn_sub['font']=f_2

btn_sub=Button(a,text='Show',font=('Times new roman',15,'bold'),border='5',activeforeground='white',activebackground='green',bg='dark blue',fg='white',command=show,width=6)
btn_sub.place(x=297,y=330)
#btn_sub['font']=f_2

def clr():
    t.delete('1.0','end')
    
btn_sub=Button(a,text='clear',font=('Times new roman',15,'bold'),border='5',activeforeground='white',activebackground='green',bg='dark blue',fg='white',command=clr,width=6)
btn_sub.place(x=390,y=330)
#btn_sub['font']=f_2
a.mainloop
