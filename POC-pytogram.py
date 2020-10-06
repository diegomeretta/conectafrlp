from pyrogram import Client

api_id = 1404989
api_hash = "c266364dfa4c11850ff7cd9e6219edcb"

with Client("my_account", api_id, api_hash) as app:
    # link = app.export_chat_invite_link(-325948556)
    f = app.send_message(-325948556, "Hola Como estan compañeros de Proyecto?")
    # f = app.promote_chat_member(-325948556, 314956884)
    #app.delete_channel(-325948556)
    print(f)