import sqlite3
connection = sqlite3.connect("chinook.db")

connection.execute(""" insert into customers (firstName,lastName,city,email)
                values('Senol','Kumas','Trabzon','senol@hotmail.com') """)
connection.commit()
connection.close()

