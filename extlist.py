# by : Cristo Emiliano Hernandez Darias 
## Repo API_Yeastar in 10.19.19.16/BonoboGit
## extlis.py toma informacion de data.py y de take_token.py para construir la petición de una lista de 
## extensiones que las almacena en un fichero llamado /json/extlist.json
#importacion de librerias y archivos .py donde se almacenan las variables que necesito

import requests
import json
import urllib3
import os.path
import os
import data
from take_token import gettoken

os.getcwd()
urllib3.disable_warnings()

cadena_json = ""
token = gettoken()

def extlist():
    url = "https://" + data.host + ":8088/api/v1.1.0/extensionlist/query?&token=" + token
    payload = {}
    headers = {
        'Content-Type': 'application/json',
        }

    # Se almacena el la variable el resultado del POST
    list = requests.request("POST", url, headers=headers, data=payload, verify=False)
    global cadena_json
    cadena_json = list.json() #esto es un diccionario
    
    ## Almacenamos la respuesta en un archivo json llamado 'extlist.josn' 
    with open(data.ruta_json_extlist, 'w') as json_file:
        json.dump(cadena_json, json_file)
    return