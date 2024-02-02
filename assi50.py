import mysql.connector

mydb = mysql.connector.connect(
    
    host="localhost", 
    user="root",
    passwd="root",
    database = "mysql"    
    )
cursor= mydb.cursor()
cursor.execute("INSERT ")

