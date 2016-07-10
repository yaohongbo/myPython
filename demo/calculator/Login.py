# -- coding: utf-8 --
from calculator import *
from Tkinter import *
import sqlite3


class LoginFrame(Tk):
    def __init__(self):
        def Login():
            cursor.execute("SELECT * FROM USERDATA where NAME=?", (name_display.get(),))
            res = cursor.fetchall()
            for row in res:
                print row[2]
                if (row[2] == pwd_display.get()):
                    self.destroy()
                    Calculator().mainloop()
                else:
                    print "username or password is not correct"

        def Exit():
            self.destroy()
        Tk.__init__(self)
        self.title("Login Frame")
        self.geometry('300x100')
        self.resizable(width=False, height=False)
        name_display = StringVar()
        pwd_display = StringVar()
        name_display.set('')
        pwd_display.set('')
        # two label
        Label(self, text='UserName:').grid(row=0)
        Label(self, text='PassWord:').grid(row=1)
        # two entry
        e1 = Entry(self, textvariable=name_display).grid(row=0, column=1)
        e2 = Entry(self, textvariable=pwd_display, show='*').grid(row=1, column=1)
        # two button
        Button(self, text='login', comman=Login).grid(row=2, column=1)
        Button(self, text='exit', comman=Exit).grid(row=2, column=2)

def createTable(conn):
    sql = '''CREATE TABLE USERDATA (ID INT PRIMARY KEY,NAME TEXT,PASSWORD TEXT,LEVEL INT)'''
    conn.execute(sql)
def insertUser(cursor, id, name, pwd, level):
    cursor.execute("SELECT * FROM USERDATA where NAME =(?)", (name,))
    res = cursor.fetchall()
    count = 0
    for i in res:
        count += 1
        res = cursor.fetchall()
    if count > 0:
        print 'data exists'
    else:
        cursor.execute("INSERT INTO USERDATA VALUES(?,?,?,?)", (id, name, pwd, level))


conn = sqlite3.connect('mydatabase')
#createTable(conn)
cursor = conn.cursor()
insertUser(cursor, 1, 'yaohongbo', '123456', 1)
insertUser(cursor, 2, 'xiangxiaodong', '123456', 1)
insertUser(cursor, 3, 'wangzheng', '123456', 1)
conn.commit()

login = LoginFrame()
login.mainloop()



