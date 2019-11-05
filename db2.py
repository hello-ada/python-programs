


import sqlite3
conn = sqlite3.connect ("Hand_tools1 . db" )
cursor = conn.cursor ( )
try :
             cursor.execute ("CREATE TABLE Foo ( id INTEGER   PRIMARY KEY, name TEXT) " )
except  sqlite3.OperationalError :
        pass

print("TableCreated Sucessfully")
try:
        cursor.execute("INSERT INTO Foo (id,name) VALUES(2,'Allen')")
        cursor.execute("INSERT INTO Foo (id,name) VALUES(3,' Border ')")
        cursor.execute("INSERT INTO Foo (id,name) VALUES(4, 'Mark')")
        cursor.execute("INSERT INTO Foo (id,name)  VALUES(5, 'Wesly')")
except  sqlite3.IntegrityError:
             pass
except sqlite3.OperationalError:
             pass
conn.commit()
print("Records Created Sucessfully")

#row factory class sqlite3.Row is used to access the columns of a query by name instead of by index:

conn.row_factory = sqlite3.Row
curs = conn.cursor()
curs.execute('''SELECT id,name FROM Foo''')
all_rows = curs.fetchall()
for row in all_rows:
                     # row[0] returns the first column in the query (id), row[1] returns name column.
                      print('{0} : {1}'.format(row['id'],  row['name']))

conn.close()
