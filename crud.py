import mysql.connector
import mysql.connector

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'ptoorp',
    database = 'valleorotava'
)
cursor = mydb.cursor()

def search_ext(numero):
    sql = "SELECT * FROM llamadas WHERE callfrom = %s OR callto = %s"
    value = (numero, numero)
    cursor.execute(sql, value)
    resultado = cursor.fetchall()
    for x in resultado:
        print (x)

def search_status(status):
    sql = "SELECT * FROM llamadas WHERE status = %s"
    value = (status, )
    cursor.execute(sql, value)
    resultado = cursor.fetchall()
    for x in resultado:
        print (x)

def search_type(type, ext):
    sql = "SELECT * FROM llamadas WHERE type = %s AND callfrom= %s"
    value = (type, ext, )
    cursor.execute(sql, value)
    result = cursor.fetchall()
    for x in result:
        print (x)

# search_ext(1112)
# search_status("NO ANSWER")
search_type("Outbound", 1900)