import sqlite3
connection = sqlite3.connect("chinook.db")

connection.execute(""" update customers set city ='Istanbul' where city='Berlin' """)

connection.commit()
connection.close()

