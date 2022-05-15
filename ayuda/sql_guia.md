# Python MySQL

## Create Connection   
Comience por crear una conexión a la base de datos.

Use the username and password from your MySQL database:   

	import mysql.connector

	mydb = mysql.connector.connect(
 	host="localhost",
  	user="yourusername",
  	password="yourpassword"
	)

	print(mydb)  
	
## Creating a Database

To create a database in MySQL, use the `"CREATE DATABASE"` statement:   

	import mysql.connector

	mydb = mysql.connector.connect(
  	host="localhost",
  	user="yourusername",
  	password="yourpassword"
	)

	mycursor = mydb.cursor()

	mycursor.execute("CREATE DATABASE mydatabase")   

### Check if Database Exists

You can check if a database exist by listing all databases in your system by using the `"SHOW DATABASES"` statement:   

	import mysql.connector

	mydb = mysql.connector.connect(
  	host="localhost",
  	user="yourusername",
  	password="yourpassword"
	)

	mycursor = mydb.cursor()

	mycursor.execute("SHOW DATABASES")

	for x in mycursor:
  	print(x)   
  	
## Creating a Table
To create a table in MySQL, use the `"CREATE TABLE"` statement.

Make sure you define the name of the database when you create the connection.   

	import mysql.connector

	mydb = mysql.connector.connect(
  	host="localhost",
  	user="yourusername",
  	password="yourpassword",
  	database="mydatabase"
	)

	mycursor = mydb.cursor()

	mycursor.execute("CREATE TABLE customers (name 	VARCHAR(255), address VARCHAR(255))")   

### Check if Table Exists.   

You can check if a table exist by listing all tables in your database with the `"SHOW TABLES"` statement:   

	import mysql.connector

	mydb = mysql.connector.connect(
  	host="localhost",
  	user="yourusername",
  	password="yourpassword",
  	database="mydatabase"
	)

	mycursor = mydb.cursor()

	mycursor.execute("SHOW TABLES")

	for x in mycursor:
  	print(x)   
  	
### Primary Key.   

When creating a table, you should also create a column with a unique key for each record.

This can be done by defining a PRIMARY KEY.

Usamos la declaración `"INT AUTO_INCREMENT PRIMARY KEY"` which will insert a unique number for each record. Starting at 1, and increased by one for each record.   

	import mysql.connector

	mydb = mysql.connector.connect(
	host="localhost",
  	user="yourusername",
  	password="yourpassword",
  	database="mydatabase"
	)

	mycursor = mydb.cursor()

	mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")