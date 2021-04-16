import tkinter as tk
from tkinter import *
from tkinter import ttk
from db_connect import mysql as ms
from transaction import Transaction
class Sell(tk.Frame):
    def __init__(self, window, obj):
        tk.Frame.__init__(self, window)
        menu = Frame(self)
        self.sql = ms()
        self.mycursor = self.sql.mycursor
        self.db = self.sql.mydb
        l = Label(menu, text="Menu: ").pack(side=LEFT)
        bb = Button(menu,text="Buy",command = lambda: obj.display_page(obj.Buy)).pack(side = LEFT)
        bd = Button(menu, text="Dashboard", command=lambda: obj.display_page(obj.DashBoard)).pack(side = LEFT)
        bw = Button(menu, text="Watchlist", command=lambda: obj.display_page(obj.Watchlist)).pack(side = LEFT)
        menu.pack()

        self.mycursor.execute("select user_id from users where user_name = \"{}\"".format(obj.uname))
        stock_list = []
        uid = self.mycursor.fetchone()[0]
        self.uid = uid
        #print(type(uid))
        self.mycursor.execute("select stock_id from user_has where user_id = {}".format(uid))
        sid = []
        for i in self.mycursor.fetchall():
            sid.append(i[0])
        #print(sid, type(sid))
        stock_list = []
        for i in sid:
            self.mycursor.execute("select stock_name from stocks where stock_id = {}".format(i))
            stock_list.append(self.mycursor.fetchone()[0])
        stock_frame = Frame(self)
        l2 = Label(stock_frame, text="Select stock you want to Sell: ").pack(side=LEFT)
        stock_sel = StringVar()
        p = 0
        def set_price(stock_sel):
            x = stock_sel.get()
            sql1 = "select pps,stock_id from Stocks where stock_name = \"{}\" "
            self.mycursor.execute(sql1.format(x))
            global price
            global stock_id
            y = self.mycursor.fetchall()[0]

            price =y[0]
            stock_id = y[1]
            sql2 = "select quantity from user_has where stock_id = (select stock_id from stocks where stock_name = \"{}\") and user_id = {}"
            self.mycursor.execute(sql2.format(x,self.uid))
            qty1 = self.mycursor.fetchall()[0]
            #print()
            out1.delete(1.0, END)
            out1.insert(END, price)
            out2.delete(1.0, END)
            out2.insert(END, qty1)
        sel1 = ttk.Combobox(stock_frame, values=stock_list, textvariable=stock_sel).pack(side=LEFT)
        price_frame = Frame(self)
        selb = Button(stock_frame, text="Select", command=lambda: set_price(stock_sel)).pack(side=LEFT)
        l3 = Label(price_frame, text="Price of the stock: ").pack(side=LEFT)
        out1 = Text(price_frame, height=2, width=15)
        out1.pack(side=LEFT)
        stock_frame.pack()
        price_frame.pack()
        qty_avail_frame = Frame(self)
        l3 = Label(qty_avail_frame, text="Quantity of the stock available: ").pack(side=LEFT)
        out2 = Text(qty_avail_frame, height=2, width=15)
        out2.pack(side=LEFT)
        qty_avail_frame.pack()
        buy_frame = Frame(self)
        l4 = Label(buy_frame, text="How many stocks do you want to Sell: ").pack(side=LEFT)
        quant = IntVar()
        qty = Entry(buy_frame, textvariable=quant).pack(side=LEFT)
        buy_frame.pack()
        confirm_frame = Frame(self)
        l5 = Label(confirm_frame, text="Total ammount: ").pack(side=LEFT)
        out3 = Text(confirm_frame, height=2, width=15)
        out3.pack(side=LEFT)
        def x():
            out3.delete(1.0, END)
            out3.insert(END, ((price)* quant.get()))
            self.sname = stock_sel.get()
            self.pps = price
            self.qty = quant.get()
            self.stock_id = stock_id
        conbut = Button(confirm_frame, text="Total ammount",command=lambda:x()).pack()
        confirm_frame.pack()
        self.type = "S"
        sell_button = Button(self, text=" SELL ", command=lambda: Transaction(self)).pack()
        #print(obj.uname)