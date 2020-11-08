# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .forms import AltaUsuarioForm, AltaGrupoForm, CreateContactForm, SendMessageForm, EditContactForm
from .models import Group, Usuario, Contact, Rol
from os import system
import os

@login_required(login_url="/login/")
def index(request):
    usuarios = Usuario.objects.filter(username=request.user.username)
    usuario = usuarios.first()
    if usuario:
        return render(request, "index.html")
    else:
        form = AltaUsuarioForm(request.POST or None)
        return render(request, "solicitar_keys.html", { 'form' : form})

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
            usuarios = Usuario.objects.filter(username=request.user.username)
            usuario = usuarios.first()
            profesor = "nombre_profesor" # TODO seleccionar desplegable
            nombre_grupo = grupo.name.replace(" ", "_")
            comando = "python creargrupo.py " + usuario.api_id + " " + usuario.api_hash + " " + nombre_grupo + " " + usuario.telegram_id + " " + profesor
            os.system(comando)
            archivo = open("creargrupo.txt","r")
            grupo.telegram_id = archivo.read()
            archivo.close()
            grupo.save()
            return redirect('/')
        else:
            form = AltaGrupoForm()

        return render(request, 'create-group.html', {'form':form})
    elif request.method == "GET":
        form = AltaGrupoForm(request.POST or None)
        return render(request, "create-group.html", { 'form' : form})

@login_required(login_url="/login/")
def get_groups(request):
    return render(request, "get-groups.html", {'groups' : Group.objects.all() })

@login_required(login_url="/login/")
def get_group(request, id):
    group = Group.objects.get(id=id)
    contacts = Contact.objects.all()
    return render(request, "get-group.html", {'group':group, 'contacts':contacts})

@login_required(login_url="/login/")
def create_contact(request):
    if request.method == "POST":
        form = CreateContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()

            return redirect('/contactos')
        else:
            form = CreateContactForm()

        return render(request, 'create-contact.html', { 'form' : form })
    elif request.method == "GET":
        form = CreateContactForm(request.POST or None)
        return render(request, "create-contact.html", { 'form' : form })

@login_required(login_url="/login/")
def get_contacts(request):
    contactos = Contact.objects.all()
    for c in contactos:
        rol = Rol.objects.filter(id=c.contact_rol_id).first()
        c.rol_description = rol.description

    paginator = Paginator(contactos, 2)
    page = request.GET.get('page')

    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
 
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    return render(request, "get-contacts.html", {'page': page, 'contacts' : contacts })

@login_required(login_url="/login/")
def edit_contact(request, name):
    contact = Contact.objects.get(name=name)
    if contact==None:
        return redirect('/error-404.html')
    elif request.method == "POST":
        form = EditContactForm(request.POST, instance=contact)
        if form.is_valid():
            contact = form.save()
            contact.save()

            return redirect('/contactos')
    else:
        form = EditContactForm(instance=contact)
        return render(request, 'edit-contact.html', { 'form': form, 'contact': contact })

@login_required(login_url="/login/")
def delete_contact(request, name):
    contact = Contact.objects.get(name=name)
    
    if contact==None:
        return redirect('/error-404.html')
    
    contact.delete()
    return redirect('/contactos')
 
@login_required(login_url="/login/")
def send_message(request):

    if request.method == "POST":
        form = SendMessageForm(request.POST)
        if form.is_valid():
            usuarios = Usuario.objects.filter(username=request.user.username)
            usuario = usuarios.first()
            texto = request.POST.get('text_message')
            grupo = request.POST.get('id_group')
            mensaje = texto.replace(" ", "_")
            comando = "python mensaje.py " + usuario.api_id + " " + usuario.api_hash + " " + str(grupo) + " " + mensaje
            print(comando)
            respuesta = os.system(comando)

            return redirect('/sendmessage')
        else:
            form = SendMessageForm()

        return render(request, "send-message.html", { 'form' : form })
    elif request.method == "GET":
        form = SendMessageForm(request.POST or None)
        return render(request, "send-message.html", { 'form' : form })
