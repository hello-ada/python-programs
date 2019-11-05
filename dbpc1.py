





import sqlite3


db = sqlite3.connect('myusers.db')
cursor = db.cursor()
try :
                cursor.execute('''    CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT,
                                                                  phone TEXT, email TEXT unique, password TEXT) ''')
except  sqlite3.OperationalError :
            pass

db.commit()
cursor = db.cursor()
name1 = 'Andres'
phone1 = '3366858'
email1 = 'user@example.com'
# A very secure password
password1 = '12345'
 
name2 = 'John'
phone2 = '5557241'
email2 = 'johndoe@example.com'
password2 = 'abcdef'

name3='Anilvenktesh'
phone3='63999880'
email3='anilvenktesh@yahoo.com'
password3='ambur'

try :
# Insert user 1
       cursor.execute('''INSERT INTO users(name, phone, email, password) VALUES(?,?,?,?)''', (name1,phone1, email1, password1))
       print('First user inserted')
except  sqlite3.IntegrityError:
             pass
try:
       cursor.execute('''INSERT INTO users(name, phone, email, password) VALUES(?,?,?,?)''', (name2,phone2, email2, password2)) 
       print('Second user inserted')
except  sqlite3.IntegrityError:
             pass
            
try:
       cursor.execute('''INSERT INTO users(name, phone, email, password) VALUES(?,?,?,?)''', (name3,phone3, email3, password3)) 
       print('Third user inserted')
except  sqlite3.IntegrityError:
             pass
db.commit()


cursor.execute('''SELECT id,name, email, phone FROM users''')
user1 = cursor.fetchone()                                              #retrieve the first row
print(user1[1])                                                               #Print the first column retrieved(user's name)
all_rows = cursor.fetchall()
for row in all_rows:
                     # row[0] returns the first column in the query (name), row[1] returns email column.
                      print('{0} : {1}, {2},{3}'.format(row[0], row[1], row[2],row[3]))



newphone = '3113093165'
userid = 1
cursor.execute('''UPDATE users SET phone = ? WHERE id = ? ''', (newphone, userid))

delete_userid = 3
cursor.execute('''DELETE FROM users WHERE id = ? ''', (delete_userid,))
db.commit()

#row factory class sqlite3.Row is used to access the columns of a query by name instead of by index:

db.row_factory = sqlite3.Row
cursor = db.cursor()
cursor.execute('''SELECT id,name, email, phone FROM users''')
all_rows = cursor.fetchall()
for row in all_rows:
                     # row[0] returns the first column in the query (name), row[1] returns email column.
                      print('{0} : {1}, {2},{3}'.format(row['id'], row['email'], row['name'],row['phone']))

db.close()
