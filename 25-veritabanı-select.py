import sqlite3 #sql kütüphanesi
connection = sqlite3.connect("chinook.db") #veritabanı bağlama

cursor = connection.execute("select FirstName,LastName from customers where City='Prague' or city='Paris'")
for row in cursor:

    print("First Name = "+row[0])
    print("Last Name = " +row[1])
    print("*************")

connection.close()

