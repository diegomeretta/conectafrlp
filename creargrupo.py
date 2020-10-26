from pyrogram import Client
import sys

api_id = sys.argv[1]
api_hash = sys.argv[2]
group_name = sys.argv[3]
user_id = sys.argv[4]

nombre_grupo = group_name.replace("_", " ")

with Client("my_account", api_id, api_hash) as app:
     chat = app.create_group(nombre_grupo, user_id)
     archivo = open("creargrupo.txt","w")
     archivo.write(chat.id)
     archivo.close()