from optparse import check_builtin
from tkinter import *
from tkinter import ttk
from venv import create
import mysql.connector as mysql

window = Tk()
window.title("Login form")
label = Label(window,text="Login form",font=('arial',20,'bold'),bg="black",fg="white")
label.pack(side=TOP,fill=X)
label = Label(window,text="",font=('arial',15,'bold'),bg="black",fg="white")
label.pack(side=BOTTOM,fill=X)



label_name = Label(window,text="Name",font=('arial',13,'bold'))
label_name.place(x=30,y=60)

name_entry=StringVar()
name_entry=ttk.Entry(window,textvariable=name_entry)
name_entry.place(x=170,y=60)

label_pwd = Label(window,text="Password",font=('airal',13,'bold'))
label_pwd.place(x=30,y=100)

pwd_entry=StringVar()
pwd_entry = ttk.Entry(window,textvariable=pwd_entry,show='*')
pwd_entry.place(x=170,y=100)

def show_password():
    if pwd_entry.cget('show')=='*':
        pwd_entry.config(show='')
    else:
        pwd_entry.config(show='*')

check_btn=Checkbutton(window,text="show password", command=show_password)
check_btn.place(x=168,y=122)

def search():
    db=mysql.connect(
    host="localhost",
    user="bunny",
    passwd="bunny",
    database="bunnydb"
    )
    cur=db.cursor()
    cur.execute('select * from users')
    data=cur.fetchall()
    name=name_entry.get()
    pwd=pwd_entry.get()
    if (name,pwd) in data:
        print(name,pwd)
    else:
        print('wrong credentials')
        db.close()

btn = ttk.Button(window,text="Login",command=search)
btn.place(x=170,y=160,width=125,height=30)

window.geometry('400x400')
window.resizable(False,False)
window.mainloop()