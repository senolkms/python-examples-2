import sqlite3
connection = sqlite3.connect("chinook.db")

cursor = connection.execute("select FirstName,LastName from customers order by FirstName ")#desc tersten
for row in cursor:

    print("First Name = "+row[0])
    print("Last Name = " +row[1])
    print("*************")

connection.close()

