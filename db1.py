





import sqlite3
connection = sqlite3.connect ("Hand_tools . db" )
cursor = connection.cursor ( )
try :
           cursor.execute ( """CREATE TABLE Toolsm( id INTEGER PRIMARY KEY,name TEXT,size TEXT,
                                   price INTEGER) """ )
except  sqlite3.OperationalError :
            pass
        
for item in (
               (None , "Knife" , "Small" , 15) , 
               (None , "Machete", "Medium", 35) ,
               (None , "Axe" , "Large", 55),
               (None , "Hatchet" , "Small", 25) ,
               (None , "Hammer", "Small", 25),
               (None , "Prybar", "Large", 60) ,
               ) :
          cursor .execute ("INSERT INTO Toolsm VALUES (? ,? , ? , ?)" , item)

connection .commit ()
#cursor.close()


cursor.execute ("SELECT name,size, price FROM Toolsm")
toolsTuple = cursor.fetchall()
for tuple in toolsTuple:
                   name , size , price = tuple                                                              
                   item = ( "%s , %s , %d" % (name , size , price ) )
                   print (item)

cursor . execute ("SELECT * FROM Toolsm " )
for row in cursor :
              print("−"  * 10)
              print("ID: " , row [0])
              print("Name : " , row [1])
              print(" Size : " , row [2])
              print("Price : " , row [3])
              print("−"  * 10)
