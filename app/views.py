# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .forms import AltaUsuarioForm, AltaGrupoForm
from .models import Usuario
from os import system


@login_required(login_url="/login/")
def index(request):

    usuarios = Usuario.objects.filter(username=request.user.username)
    if usuarios.first():
        return render(request, "index.html")
    else:
        form = AltaUsuarioForm(request.POST or None)
        return render(request, "solicitar_keys.html", { 'form' : form})

def home(request):
    return render(request, "index.html")

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'error-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'error-500.html' )
        return HttpResponse(html_template.render(context, request))

def solicitar_keys(request):
    if request.method == "POST":
        form = AltaUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.username = request.user.username
            usuario.save()

            return redirect('/')
        else:
            form = AltaUsuarioForm()

        return render(request, 'index.html', {'form':form})

@login_required(login_url="/login/")
def create_group(request):
    if request.method == "POST":
        form = AltaGrupoForm(request.POST)
        if form.is_valid():
            grupo = form.save(commit=False)
            grupo.save()

            return redirect('/')
        else:
            form = AltaGrupoForm()

        return render(request, 'create_group.html', {'form':form})
    elif request.method == "GET":
        form = AltaGrupoForm(request.POST or None)
        return render(request, "create_group.html", { 'form' : form})
