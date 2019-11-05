

import sqlite3 
conn = sqlite3.connect('demo.db') 
print ("Opened database successfully")

cursor=conn.cursor()
try :
       conn.execute("""Create Table Emp ( id INT primary key,name Text NOT NULL, size Text, price REAL)""")
except  sqlite3.OperationalError :
              pass
            
print (" database created successfully")

ch=input("You want enter the details\n")
if ch=='y':
          n=int(input("Enter the number of employees\n"))
          for i in range(0,n):
                      print("")
                      id=int(input("Enter EmpId of an Emp\n"))
                      print("")
                      name=input("Enter name of an Emp\n")
                      print("")
                      size=int(input("Enter size of an Emp\n"))
                      print("")
                      price=float(input("Enter Basic Salary of an Emp\n"))
                      
cursor.execute("INSERT INTO Emp (id,name,size,price) VALUES (?,?,?,?)",(id,name,size,price));
conn.commit()











