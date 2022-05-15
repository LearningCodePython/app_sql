import mysql.connector
import hashlib

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'ptoorp',
)
cursor=mydb.cursor()

database_name = ""
table_name =""

def create_database(value):
    cursor.execute(f'CREATE DATABASE {value}')
    global database_name
    database_name = value

def create_table(table):
    cursor.execute(f'USE {database_name}')
    cursor.execute(f'CREATE TABLE {table} (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR (50), host VARCHAR (50), user VARCHAR (50), password VARCHAR (50))')
    global table_name
    table_name = table

def insert(name, host, user, password):
    #Encode password:
    p_encode = password.encode()
    h = hashlib.new("md5", p_encode)
    passwd = (h.hexdigest())
    #Seleccion de base de tados.
    cursor.execute(f'USE {database_name}')
    #Insertar en la base de datos.
    sql = (f'INSERT INTO {table_name} (name, host, user, password) VALUES (%s, %s, %s, %s)')
    values = (name, host, user, passwd)
    cursor.execute(sql, values)

create_database('datos')
create_table('site')

#insert('contel', '192.168.0.45', 'api', '!contel9876')
#insert('dania', '172.16.3.2', 'api', 'asflhhs')

mydb.commit()

print (database_name)
print (table_name)
