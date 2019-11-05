import sqlite3
import time

try:
      conn=sqlite3.connect('tutorial1.db')
      c=conn.cursor()
except sqlite3.OperationalErrror:
       pass

def create_table():
              c.execute('create table if not exists Employee(empid INT,empname TEXT,email  TEXT,salary REAL)')

def data_entry():
              c.execute("insert into Employee values(121,'Ashoka','ashokchakra@gmail.com',8000.0)")
              conn.commit()
              

def dynamic_data_entry():
                empid=input("enter the empid")
                empname=input("enter the empname")
                email=input("enter the emailid")
                salary=input("enter the salary")
                c.execute("insert into Employee(empid,empname,email,salary) values(?,?,?,?)",(empid,empname,email,salary))
                conn.commit()
                

create_table()
data_entry()

for var in range(2):
                 dynamic_data_entry()
                 time.sleep(1)
c.close()
conn.close()
