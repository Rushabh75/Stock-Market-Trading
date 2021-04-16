import tkinter as tk
from tkinter import *
from db_connect import mysql as ms
class UserWatch(tk.Frame):
    def __init__(self, window, obj):
        tk.Frame.__init__(self, window)
        menu = Frame(self)
        self.sql = ms()
        self.mycursor = self.sql.mycursor
        self.db = self.sql.mydb
        l = Label(menu, text="Menu: ").grid(row = 0, column = 0 )
        bb = Button(menu, text="Buy", command=lambda: obj.display_page(obj.Buy)).grid(row = 0, column = 1 )
        bd = Button(menu, text="Dashboard", command=lambda: obj.display_page(obj.DashBoard)).grid(row = 0, column = 2 )
        bs = Button(menu, text="Sell", command=lambda: obj.display_page(obj.Sell)).grid(row = 0, column = 3 )
        bw = Button(menu, text="Watchlist", command=lambda: obj.display_page(obj.Watchlist)).grid(row = 0, column = 4 )
        menu.pack()
        self.mycursor.execute("select user_id from users where user_name = \"{}\"".format(obj.uname))
        stock_list = []
        uid = self.mycursor.fetchone()[0]
        #print(uid)
        qry = """select s.stock_id,s.stock_name,s.pps,uh.quantity from stocks s  Inner join user_has uh on uh.stock_id = s.stock_id
                where (s.stock_id, uh.user_id) in 
                (select stock_id,user_id from user_has where user_id = {});"""
        self.mycursor.execute(qry.format(uid))
        sid = []
        sqty = []
        sname = []
        pps = []
        for i in self.mycursor.fetchall():
            sid.append(i[0])
            sname.append(i[1])
            pps.append(i[2])
            sqty.append(i[3])
        #print(sid, sqty,sname,pps)
        table = Frame(self)
        row = Frame(table)
        idl = Text(row, height=2, width=15)
        idl.insert(END, "Stock ID")
        idl.pack(side=LEFT)
        namel = Text(row, height=2, width=25)
        namel.insert(END, "Stock Name")
        namel.pack(side=LEFT)
        pricel = Text(row, height=2, width=15)
        pricel.insert(END, "Stock Price")
        pricel.pack(side=LEFT)
        qtyl = Text(row, height=2, width=15)
        qtyl.insert(END, "Stock Quantity")
        qtyl.pack(side=LEFT)
        row.pack()
        for i in range (0,len(sid)):
            row = Frame(table)
            idl = Text(row, height=2, width=15)
            idl.insert(END,sid[i])
            idl.pack(side = LEFT)
            namel= Text(row, height=2, width=25)
            namel.insert(END,sname[i])
            namel.pack(side = LEFT)
            pricel= Text(row, height=2, width=15)
            pricel.insert(END,pps[i])
            pricel.pack(side = LEFT)
            qtyl= Text(row, height=2, width=15)
            qtyl.insert(END,sqty[i])
            qtyl.pack(side = LEFT)
            row.pack()
        table.pack()