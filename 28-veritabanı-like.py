import sqlite3 #sql kütüphanesi
connection = sqlite3.connect("chinook.db") #veritabanı bağlama

cursor = connection.execute("select FirstName,LastName from customers where FirstName like '%a' ")
for row in cursor:

    print("First Name = "+row[0])
    print("Last Name = " +row[1])
    print("*************")
# %a% içinde a harfi geçenler
# a% a ile başlayanlar
# %a a ile bitenler
connection.close()

