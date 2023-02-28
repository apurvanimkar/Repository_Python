#Now we will insert data in previously created SQLite table
#called "Product" using python for that write the code.

import sqlite3

con = sqlite3.connect('hello.db')

cur = con.cursor()

cur.execute("INSERT INTO Product(p_name, price,quantity) VALUES ('AutoCAD',200,20)");

cur.execute("INSERT INTO Product(p_name, price,quantity) VALUES('Quick Hill',330,12)"); cur.execute("INSERT INTO Product(p_name, price,quantity) VALUES ('Keyboard',250,25)"); cur.execute("INSERT INTO Product(p_name, price,quantity) VALUES ('Mouse',150,34)");

print("Data Inserted!!!")

con.commit()

con.close()
