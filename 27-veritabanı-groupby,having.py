import sqlite3
connection = sqlite3.connect("chinook.db")

cursor = connection.execute("""select city,count(*) from customers 
                            group by city having count(*)>1 
                            order by city """)#sayısı 1 den fazla olanları ver
for row in cursor:

    print("City = "+row[0])
    print("Count = " +str(row[1]))
    print("*************")

connection.close()

