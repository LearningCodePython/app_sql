from os import link
import requests
import csv

import take_token
import data


# Comienzo almacenando el token de cada consulta en la variabla mytoken.
mytoken = take_token.gettoken()

# Para descarcar el CDR necesito generar otro token ramdom llamado get_ramdom_token
# El post inicial seria asi POST /api/v1.1.0/cdr/get_random?token={token}

token_random = 0
def random():
      url ="https://" + data.host + ":8088/api/v1.1.0/cdr/get_random?token=" + mytoken
      payload="{\"extid\": \"1900\", \"starttime\": \"2022-04-30 00:00:00\", \"endtime\": \"2022-04-30 23:59:59\"}"
      headers={'Content-Type': 'text/plain'}
      r = requests.post(url, headers=headers, data=payload, verify=False)
      cadena_json = r.json()
      clave=(cadena_json["random"])
      global token_random
      token_random = clave
      return

# una vez este el token_random generado lo usaremos para la siguiente consulta.
random()

link_download = "https://" + data.host + ":8088/api/v1.1.0/cdr/download?extid=1900&starttime=2022-04-30 00:00:00&endtime=2022-04-30 23:59:59&token=" + mytoken + "&random=" + str(token_random)
r = requests.get(link_download, allow_redirects=True, verify=False)
open ('datos.csv', 'wb').write(r.content)