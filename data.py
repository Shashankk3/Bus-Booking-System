from tkinter import*
import sqlite3
from tkinter.messagebox import *
from datetime import date
con=sqlite3.connect('project_db')
cur=con.cursor()
cur.execute('select * from route')
res=cur.fetchall()
print(res)
cur.execute('select * from operator')
res=cur.fetchall()
print(res)
cur.execute('select * from running')
res=cur.fetchall()
print(res)
cur.execute('select * from booking_history')
res=cur.fetchall()
print(res)
