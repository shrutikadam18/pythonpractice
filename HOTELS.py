import mysql.connector
db_connection = mysql.connector.connect(host="localhost",user="root", password="root", database = "hotel")
cursor=db_connection.cursor()

#create_database_query = "CREATE DATABASE HOTEl"

#cursor.execute(create_database_query)

#db_connection.commit()

#create_table_query = """CREATE TABLE Staff( id int,fullname varchar(255),position varchar(255),salary int)"""
#cursor.execute(create_table_query)
#db_connection.commit()
#insert_data_query = """
#INSERT INTO Staff (id,fullname,position,salary) VALUES (%s, %s , %s ,%s)
#"""
#data_to_insert1 = (1,"shruti kadam","manager",40000 )
#data_to_insert= (2,"sakshi gurav","accountant",37000)
#cursor.execute(insert_data_query)
#db_connection.commit()

#create_table_query="""CREATE TABLE BOOKING(booking_id int ,guest_id int,room_no int ,room_price int)"""
#cursor.execute(create_table_query )
#db_connection.commit()

insert_data_query=""" INSERT INTO BOOKING (Booking_id,guest_id,room_no,room_price) VALUES (%s, %s, %s ,%s)"""
data1=[(1,3,78,900),(2,4,23,1200),(3,7,34,2000)]
cursor.executemany(insert_data_query,data1)
db_connection.commit()

