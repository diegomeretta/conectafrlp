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
    path('', views.index, name='home'),
    path('home', views.home, name='index'),
    path('solicitarkeys', views.solicitar_keys, name='solicitarkeys'),
    path('creategroup', views.create_group, name='creategroup'),
    path('createcontact', views.create_contact, name='createcontact'),
]
