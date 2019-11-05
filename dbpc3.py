import sqlite3

conn=sqlite3.connect('tutorial.db')
c=conn.cursor()

def create_table():
              c.execute('create table if not exists stuffplot(unix REAL ,datestamp TEXT,keyword TEXT,value REAL)')

def data_entry():
              c.execute("insert into stuffplot values(145123543,'2016-02-01','Python',9)")
              conn.commit()
              c.close()
              conn.close()





create_table()
data_entry()

     
