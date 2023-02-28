#Getting the values from the database-


import sqlite3

con = sqlite3.connect('hello.db')

cur = con.cursor()

cur.execute("CREATE TABLE Product (p_id INTEGER PRIMARY KEY AUTOINCREMENT,p_name TEXT NOT NULL, price REAL,quantity INTEGER)");

print("Table created!!!")

con.close()
 
