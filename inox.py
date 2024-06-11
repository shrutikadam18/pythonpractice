import mysql.connector
mydb=mysql.connector.connect(host="localhost",
                             username="root",
                             password="root",
                             database="inox")
c=mydb.cursor()
#c.execute("CREATE DATABASE inox")
#c.execute("CREATE TABLE Movies (id int,name varchar(255),language varchar(255),rating int,Ticket_Price int,Category varchar(255),YearOfRelease int)")


sqlFormula="INSERT INTO Movies (id,name,language,rating,Ticket_Price,Category,YearOfRelease) values (%s,%s,%s,%s,%s,%s,%s)"
first_item=[(1,"Sita Ramam","Telugu",9.8,300,"Romantic Drama",2022),(2,"Shershaah","Hindi",9.0,250,"Biographic war",2021),(3,"Pawankhind","marathi",9.5,260,"Historical Action",2022),(4,"Laapataa Ladies","Hindi",8,220,"Comedy Drama",2024),(5,"KGF-Chapter 1","Kannada",9.6,260,"Action",2018)]
c.executemany(sqlFormula,first_item)
mydb.commit()