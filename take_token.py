# by : Cristo Emiliano Hernandez Darias 
#
## Repo en GutHub personal
## La primera parte del proyecto consiste en establecer la conexion con la central y acceder los datos CDR.

import requests
import urllib3
import data
urllib3.disable_warnings()

# La función gettoken captura el toquen necesario para los requests posteriores
def gettoken (): # Función que captura el token para almacenarlo en la variable toke.
  url = "https://" + data.host + ":8088/api/v1.1.0/login"
  payload="{ \"username\":" + data.api_user + ",\"password\":" + data.api_pass+ ",\"port\": \"8260\"}"
  headers = {
    'Content-Type': 'text/plain'
  }
  r = requests.post(url, headers=headers, data=payload, verify=False)
  jsonResponse = r.json()
  token = (jsonResponse["token"]) #Selecciona al valor de la clave "token"
  return token
