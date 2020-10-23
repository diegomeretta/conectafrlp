from pyrogram import Client
import sys

api_id = sys.argv[1]
api_hash = sys.argv[2]
chat_id = sys.argv[3]
texto = sys.argv[4]

mensaje = texto.replace("_", " ")

with Client("my_account", api_id, api_hash) as app:
     f = app.send_message(chat_id, mensaje)