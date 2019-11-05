


import sqlite3 
conn = sqlite3.connect('test1.db')
curs = conn.cursor()
print ("Opened database successfully")
try :
        curs.execute("""CREATE TABLE COMPANY  (ID INT PRIMARY KEY NOT NULL, 
                            NAME TEXT NOT NULL, AGE INT NOT NULL, ADDRESS CHAR(50), SALARY REAL)""")
except  sqlite3.OperationalError :
              pass
print ("Table created successfully")
#conn.close()
try:
        curs.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES(2,'Allen',25,'Texas',15000.00)")
        curs.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES(3,' Border ',35,'Boston',18000.00)")
        curs.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY)  VALUES(4, 'Mark', 25, 'Rich-Mond', 65000.00)")
        curs.execute("INSERT INTO COMPANY(ID,NAME,AGE,ADDRESS,SALARY)  VALUES(5, 'Wesly', 45, 'Houston', 70000.00)")
except  sqlite3.IntegrityError:
             pass
except sqlite3.OperationalError:
             pass
conn.commit()
print("Records Created Sucessfully")

#row factory class sqlite3.Row is used to access the columns of a query by name instead of by index:

conn.row_factory = sqlite3.Row
curs = conn.cursor()
curs.execute('''SELECT id,name, age, address,salary FROM COMPANY''')
all_rows = curs.fetchall()
for row in all_rows:
                     # row[0] returns the first column in the query (name), row[1] returns email column.
                      print('{0} : {1}, {2},{3},{4}'.format(row['id'], row['age'], row['name'],row['salary'],row['address']))

conn.close()











