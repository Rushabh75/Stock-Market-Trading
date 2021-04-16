import tkinter as tk
from tkinter import *
from Buy import Buy
from Sell import Sell
from Watchlist import Watchlist
from UserWatch import UserWatch
from MarketWatch import MarketWatch

class dashboard(tk.Tk):
    def __init__(self,uname):
        tk.Tk.__init__(self)
        window = Frame(self,height = 500,width = 500)
        window.pack(side="top",fill="both", expand=True)
        window.grid_rowconfigure(0, weight=1)
        window.grid_columnconfigure(0, weight=1)
        #print(uname)
        self.window = window
        self.uname = uname
        self.Buy = Buy
        self.Sell = Sell
        self.Watchlist = Watchlist
        self.UserWatch = UserWatch
        self.MarketWatch = MarketWatch
        self.DashBoard = DashBoard
        self.pages = {}
        #for F in (DashBoard, Buy, Sell, Watchlist, UserWatch, MarketWatch):
            #page = F(window, self)
            #self.pages[F] = page
            #page.grid(row=1, column=1, sticky="nsew")
        self.display_page(DashBoard)

    def display_page(self, sel):
        page = sel(self.window,self)
        page.grid(row=1, column=1, sticky="nsew")


class DashBoard(tk.Frame):

    def __init__(self,window,obj):
        tk.Frame.__init__(self,window)
        l = Label(self, text=" DASHBOARD  ").pack(side=TOP)
        bb = Button(self,text="Buy", command=lambda: obj.display_page(Buy)).pack()
        bs = Button(self, text="Sell", command=lambda: obj.display_page(Sell)).pack()
        bw = Button(self, text="Watchlist", command=lambda: obj.display_page(Watchlist)).pack()


class dash():
    def __init__(self,uname):
        dashb = dashboard(uname)
        dashb.title("lol")
        dashb.mainloop()