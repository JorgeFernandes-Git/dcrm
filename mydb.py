import mysql.connector

database = mysql.connector.connect(host="localhost", user="root", passwd="")

# prepare a cursor object
cursor_object = database.cursor()

# Create a database
cursor_object.execute("CREATE DATABASE jorgeco")

print("All done!")
