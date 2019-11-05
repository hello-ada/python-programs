import sqlite3 
conn1 = sqlite3.connect('test.db') 
print("Opened database successfully")
conn1.execute("UPDATE COMPANY set SALARY = 35000.00 where id = 2") 
conn1.commit 
print ("Total number of rows updated :", conn1.total_changes )
cur = conn1.execute("SELECT id, name, address, salary from COMPANY") 
for row in cur: 
	print ("ID = ", row[0] )
	print ("NAME = ", row[1] )
	print ("ADDRESS = ", row[2] )
	print ("SALARY = ", row[3], "\n" )
print("Operation done successfully")
conn1.close()
