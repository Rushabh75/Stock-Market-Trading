import tkinter as tk
from tkinter import *
class Watchlist(tk.Frame):
    def __init__(self, window, obj):
        tk.Frame.__init__(self, window)
        menu = Frame(self)
        l = Label(menu,text="Menu: ").pack(side = LEFT)
        bb = Button(menu, text="Buy", command=lambda: obj.display_page(obj.Buy)).pack(side = LEFT)
        bs = Button(menu, text="Sell", command=lambda: obj.display_page(obj.Sell)).pack(side = LEFT)
        bd = Button(menu, text="Dashboard", command=lambda: obj.display_page(obj.DashBoard)).pack(side = LEFT)
        menu.pack()
        sel = Frame(self)
        l1 = Label(sel,text="Watch: ").pack(side = TOP)
        bu = Button(sel, text="User Stocks", command=lambda: obj.display_page(obj.UserWatch)).pack(side = LEFT)
        bm = Button(sel, text="Market", command=lambda: obj.display_page(obj.MarketWatch)).pack(side = LEFT)
        sel.pack()