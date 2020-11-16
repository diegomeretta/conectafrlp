from pyrogram import Client
import sys

api_id = sys.argv[1]
api_hash = sys.argv[2]
group_name = sys.argv[3]

nombre_grupo = group_name.replace("_", " ")

with Client("my_account", api_id, api_hash) as app:
     integrantes = []
     for i in range(4, len(sys.argv)):
          integrantes.append(sys.argv[i])
     chat = app.create_group(nombre_grupo, integrantes)
     archivo = open("creargrupo.txt","w")
     archivo.write(str(chat.id))
     archivo.close()