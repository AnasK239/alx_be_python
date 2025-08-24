import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Anas2392@",
    database="united_nations"
)


mycursor = mydb.cursor()

mycursor.execute("show databases")

for i in mycursor:
    print(i)