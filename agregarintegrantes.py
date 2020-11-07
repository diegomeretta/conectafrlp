from pyrogram import Client
import sys

api_id = sys.argv[1]
api_hash = sys.argv[2]
chat_id = sys.argv[3]

with Client("my_account", api_id, api_hash) as app:
     archivo = open("agregarintegrantes.txt","w")
     integrantes = []
     for i in range(4, len(sys.argv)):
          integrantes.append(sys.argv[i])
     resultado = app.add_chat_members(chat_id, integrantes)
     archivo.write(resultado)
     archivo.close()