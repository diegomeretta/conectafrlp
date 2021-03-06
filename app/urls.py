# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.
    re_path(r'^.*\.html', views.pages, name='pages'),

    # The home page
    path('', views.index, name='index'),
    path('solicitarkeys', views.solicitar_keys, name='solicitarkeys'),
    path('nuevogrupo', views.create_group, name='nuevogrupo'),
    path('grupos', views.get_groups, name='grupos'),
    path('editargrupo/<int:id>', views.edit_group, name='editargrupo'),
    path('eliminargrupo/<int:id>', views.delete_group, name='eliminargrupo'),
    
    path('nuevocontacto', views.create_contact, name='nuevocontacto'),
    path('editarcontacto/<str:name>', views.edit_contact, name='editarcontacto'),
    path('contactos', views.get_contacts, name='contactos'),
    path('eliminarcontacto/<str:name>', views.delete_contact, name='eliminarcontacto'),
  
    path('enviarmensaje', views.send_message, name='enviarmensaje'),

    path('perfil', views.profile, name='perfil'),

    path('ayuda', views.faq, name='ayuda'),
]
