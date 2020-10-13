from pyrogram import Client

api_id = arg[0]
api_hash = arg[1]
chat_id = arg[2]

with Client("my_account", api_id, api_hash) as app:
    f = app.send_message(chat_id, "Hola")
    print(f)