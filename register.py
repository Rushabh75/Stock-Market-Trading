#import mysql.connector
from db_connect import  mysql as ms
from tkinter import *
def log():
    r.destroy()
    userx = l.login()
    userx.log(uname.get(),password.get())
regsql = ms()
rmydb = regsql.mydb
rmycursor = regsql.mycursor
#mydb = mysql.connector.connect(
    #host="localhost",
    #user="root",
    #password="Soham123",
    #auth_plugin='mysql_native_password',
    #db = 'project'
#)
#mycursor = mydb.cursor()
class register():

    def reg(self):
        r = Tk()
        self.uev=StringVar()
        self.pwdev=StringVar()
        self.c1ev=IntVar()
        self.c2ev=IntVar()
        self.addev=StringVar()
        self.panev=StringVar()
        self.emailev=StringVar()
        top = Label(r,text = 'Registeration').grid(row = 0,column = 0, columnspan = 2)
        ul = Label(r,text = 'enter username: ').grid(row = 1, column = 0)
        ue = Entry(r, textvariable=self.uev).grid(row = 1, column = 1)
        pwdl = Label(r, text='enter Password: ').grid(row = 2, column = 0)
        pwde = Entry(r, textvariable=self.pwdev).grid(row = 2, column = 1)
        c1l = Label(r, text='enter contact number 1: ').grid(row = 3, column = 0)
        c1e = Entry(r, textvariable=self.c1ev).grid(row = 3, column = 1)
        c2l = Label(r, text='enter contact numebr 2: ').grid(row = 4, column = 0)
        c2e = Entry(r, textvariable=self.c2ev).grid(row = 4, column = 1)
        addl = Label(r, text='enter address: ').grid(row = 5, column = 0)
        adde = Entry(r, textvariable=self.addev).grid(row = 5, column = 1)
        panl = Label(r, text='enter pan number: ').grid(row = 6, column = 0)
        pane = Entry(r, textvariable=self.panev).grid(row = 6, column = 1)
        emaill = Label(r, text='enter email id: ').grid(row = 7, column = 0)
        emaile = Entry(r, textvariable=self.emailev).grid(row = 7, column = 1)
        def mid():
            self.check()
            success = Label(r, text="registration successful!! Login now").grid(row=9, column=0)
            ok = Button(r, text='ok', command=r.destroy).grid(row=9, column=1)
        che = Button(r,text = 'Register', command = mid).grid(row = 8,column = 0, columnspan = 2)

        r.mainloop()
    def check(self):
        try:
            sql = "insert into users(user_name,password,contact_no1,contact_no2,address,pan_no,email_id) values(\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\",\"{}\")"

            rmycursor.execute(sql.format(str(self.uev.get()), self.pwdev.get(), self.c1ev.get(), self.c2ev.get(), self.addev.get(), self.panev.get(), self.emailev.get()))
            rmydb.commit()

        except Exception as e:
            print("enter unique username and pan number",e)