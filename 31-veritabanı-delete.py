import sqlite3
connection = sqlite3.connect("chinook.db")

connection.execute(""" delete from customers where customerid=62 """)

connection.commit()
connection.close()

