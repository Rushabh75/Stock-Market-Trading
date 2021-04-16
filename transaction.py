from tkinter import *
from datetime import datetime
from db_connect import mysql as ms
transql = ms()
tranmycursor = transql.mycursor
trandb = transql.mydb
class Transaction():
    def __init__(self,tran):
        #pass
        if (tran.type == 'B'):
            tranmycursor.execute("select quantity from stocks where stock_id = {}".format(tran.stock_id))
        else:
            tranmycursor.execute("select quantity from user_has where stock_id = {}".format(tran.stock_id))
        qtymax = tranmycursor.fetchone()[0]
        if (tran.qty>qtymax):
            warning = Tk()
            l1 = Label(warning, text = "Please Enter a suitable quantity")
            l1.pack()
            warning.mainloop()
        else:
            if (tran.type == 'B'):
                tranmycursor.execute("update stocks set quantity = quantity - {} where stock_id = {}".format(tran.qty,tran.stock_id))
                tranmycursor.execute("insert into user_has(user_id,stock_id,quantity) values({},{},{}) on duplicate key update quantity = quantity + {} ".format(tran.uid ,tran.stock_id,tran.qty,tran.qty))
            else:
                tranmycursor.execute("update stocks set quantity = quantity + {} where stock_id = {}".format(tran.qty,tran.stock_id))
                tranmycursor.execute("update user_has set quantity = quantity - {} where stock_id = {}".format(tran.qty, tran.stock_id))
            now = datetime.now()
            date_ins = now.strftime('%Y-%m-%d %H:%M:%S')
            print(date_ins)
            sql = "insert into transactions(tran_time,trans_price,stock_id,user_id,type,trans_qty) values(\"{}\",{},{},{},\"{}\",{})"
            tranmycursor.execute(sql.format(date_ins,tran.pps,tran.stock_id,tran.uid,tran.type,tran.qty))
            trandb.commit()
        #print(qtymax)
        #print(tran.pps,tran.sname,tran.qty,tran.type,tran.uid,tran.stock_id)
        #print(tran.)