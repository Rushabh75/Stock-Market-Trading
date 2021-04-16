import tkinter as tk
from tkinter import *
from db_connect import mysql as ms
class MarketWatch(tk.Frame):
    def __init__(self, window, obj):
        tk.Frame.__init__(self, window)
        menu = Frame(self)
        self.sql = ms()
        self.mycursor = self.sql.mycursor
        self.db = self.sql.mydb
        l = Label(menu, text="Menu: ").pack(side=LEFT)
        bb = Button(menu, text="Buy", command=lambda: obj.display_page(obj.Buy)).pack(side=LEFT)
        bd = Button(menu, text="Dashboard", command=lambda: obj.display_page(obj.DashBoard)).pack(side=LEFT)
        bs = Button(menu, text="Sell", command=lambda: obj.display_page(obj.Sell)).pack(side=LEFT)
        bw = Button(menu, text="Watchlist", command=lambda: obj.display_page(obj.Watchlist)).pack(side=LEFT)
        menu.pack()
        self.mycursor.execute("select user_id from users where user_name = \"{}\"".format(obj.uname))
        stock_list = []
        uid = self.mycursor.fetchone()[0]
        #print(uid)
        self.mycursor.execute("select sector_id,sector_name from sector")
        secid = []
        sec_name = []
        dict1 = {}
        c = 0
        for i in self.mycursor.fetchall():
            secid.append(i[0])
            sec_name.append(i[1])
            dict1[sec_name[c]]= secid[c]
            c+=1
        #print(sec_name[0],secid[0])
        sector_frame = Frame(self)
        l2 = Label(sector_frame, text="Select Sector you want to Watch: ").pack(side=LEFT)
        sec_sel = StringVar()
        sel_sec_id = 0
        global cont
        cont = 0
        def sel_sector(sec_sel_id):
            global cont
            global sel_sec_id
            sel_sec_id = sec_sel_id
            #print(sel_sec_id)
            if sel_sec_id != 0:
                #print("couounter",cont)
                if cont != 0:
                    self.table.destroy()
                putin(sel_sec_id)
                cont += 1

        sel1 = ttk.Combobox(sector_frame, values=sec_name, textvariable=sec_sel).pack(side=LEFT)
        #print(sec_sel)
        selb = Button(sector_frame, text="Select", command=lambda : sel_sector(dict1[sec_sel.get()])).pack(side=LEFT)
        #print("lol", sel_sec_id)
        sector_frame.pack()
        sql = "select stock_id,stock_name,pps,quantity from Stocks where sector_id = {} "
        def putin(sel_sec_id):
            global row
            self.table = Frame(self)
            sql = "select stock_id,stock_name,pps,quantity from Stocks where sector_id = {} "
            self.mycursor.execute(sql.format(sel_sec_id))
            #print("look",sel_sec_id)
            stock_id = []
            stock_name=[]
            pps=[]
            quantity=[]
            for row in self.mycursor.fetchall():
                stock_id.append(row[0])
                stock_name.append(row[1])
                pps.append(row[2])
                quantity.append(row[3])
            #print(stock_id,stock_name,pps,quantity)
            head = Frame(self.table)
            idl = Text(head, height=2, width=15)
            idl.insert(END, "Stock ID")
            idl.pack(side=LEFT)
            namel = Text(head, height=2, width=25)
            namel.insert(END, "Stock Name")
            namel.pack(side=LEFT)
            pricel = Text(head, height=2, width=15)
            pricel.insert(END, "Stock Price")
            pricel.pack(side=LEFT)
            qtyl = Text(head, height=2, width=15)
            qtyl.insert(END, "Stock Quantity")
            qtyl.pack(side=LEFT)
            head.pack()
            for i in range(0,len(stock_id)):
                row = Frame(self.table)
                idl = Text(row, height=2, width=15)
                idl.insert(END, stock_id[i])
                idl.pack(side=LEFT)
                namel = Text(row, height=2, width=25)
                namel.insert(END, stock_name[i])
                namel.pack(side=LEFT)
                pricel = Text(row, height=2, width=15)
                pricel.insert(END, pps[i])
                pricel.pack(side=LEFT)
                qtyl = Text(row, height=2, width=15)
                qtyl.insert(END, quantity[i])
                qtyl.pack(side=LEFT)
                row.pack()
            self.table.pack()