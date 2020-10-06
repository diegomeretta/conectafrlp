from pyrogram import Client

def sum(*args)

print(args)

api_id = 1404989
api_hash = "c266364dfa4c11850ff7cd9e6219edcb"

with Client("my_account", api_id, api_hash) as app:
    f = app.send_message(-325948556, "Hola Compañeros de Proyecto")