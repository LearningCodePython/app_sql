import requests
import mysql.connector
import csv
import os
import take_token
import data


# Comienzo almacenando el token de cada consulta en la variabla mytoken.
mytoken = take_token.gettoken()

# Para descarcar el CDR necesito generar otro token ramdom llamado get_ramdom_token
# El post inicial seria asi POST /api/v1.1.0/cdr/get_random?token={token}

token_random = 0
extid = input("Cual es la extensión?. ")
f_inicio = input("Fecha de inicio de la busqueda AAAA-MM-DD: ")
f_fin = input("Fecha de inicio de la busqueda AAAA-MM-DD: ")
starttime = (f"{f_inicio} 00:00:00")
endtime = (f"{f_fin} 23:59:59")

def random():
    url ="https://" + data.host + ":8088/api/v1.1.0/cdr/get_random?token=" + mytoken
    payload="{\"extid\":\"" + extid + "\", \"starttime\":\"" + starttime + "\", \"endtime\":\"" + endtime + "\"}"
    headers={'Content-Type': 'text/plain'}
    r = requests.post(url, headers=headers, data=payload, verify=False)
    cadena_json = r.json()
    clave=(cadena_json["random"])
    global token_random
    token_random = clave
    # print (cadena_json)
    return

random()
# una vez este el token_random generado lo usaremos para la siguiente consulta.
# Este get nos descarga un fichero csv que lo almaceno con el nombre de 'datos.cvs'
link_download = "https://" + data.host + ":8088/api/v1.1.0/cdr/download?extid=" + extid + "&starttime=" + starttime +"&endtime=" + endtime + "&token=" + mytoken + "&random=" + str(token_random)
r = requests.get(link_download, allow_redirects=True, verify=False)
open ('csv/datos.csv', 'wb').write(r.content)

## Procesado del fichero CSV ##
# 1º se Lee el fichero datos.csv y se abre el fichero outpyt.csv en modo escritura
# 2º se salta la primera liena de datos.csv con la orden 'next(file)
# 3º se recorreo el fichero datos.csv y se escribe cada una de las lineas en el nuevo fichero output.csv.

with open('csv/datos.csv', 'r') as file, open('csv/output.csv', 'w') as file1:
    next(file)
    for line in file:
        file1.write(line)

# Crecion de la conexion a la base de datos y exportacion de los datos obtenidos.
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'ptoorp',
    database = 'valleorotava'
)
cursor=mydb.cursor()

# Recoger los datos del csv y pasarlos a la base de datos ya creada "contel" dentro de la tabla "llamadas".

with open('csv/output.csv', newline='') as csvfile:
    csv_data = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in csv_data:
        cursor.execute('INSERT INTO llamadas(callid,timestart,callfrom,callto,callduraction,talkduraction,srctrunkname,dsttrunkname,status,type,pincode,recording,didnumber,sn) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', row)

mydb.commit()

cursor.close()

os.remove('csv/datos.csv')
os.remove('csv/output.csv')

# Un vez que esta la información almacenada en la base de datos, pasamos a hacerle consultas.
# Ademas es buena opcion integrar esta parte del programa con la app.web

