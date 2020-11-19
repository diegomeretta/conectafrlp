# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from .forms import AltaUsuarioForm, AltaGrupoForm, EditGroupForm, CreateContactForm, SendMessageForm, EditContactForm
from .models import Group, Usuario, Contact, Rol, Message, Subject
from os import system
import os

@login_required(login_url="/login/")
def index(request):
    usuarios = Usuario.objects.filter(username=request.user.username)
    usuario = usuarios.first()
    if usuario:
        return render(request, "index.html",{
            'username': usuario.username,
            'groups': Group.objects.all().count(),
            'users': Contact.objects.all().count(),
            'messages': Message.objects.all().count()
            })
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
            profesores = ""
            for contact in form.cleaned_data.get('contacts'):
                profesores += " " + str(contact)
            print(profesores.lstrip())
            usuarios = Usuario.objects.filter(username=request.user.username)
            usuario = usuarios.first()
            nombre_grupo = request.POST.get('name').replace(" ", "_")
            comando = "python creargrupo.py " + usuario.api_id + " " + usuario.api_hash + " " + nombre_grupo + " " + usuario.telegram_id + " " + profesores
            os.system(comando)
            grupo =form.save()
            archivo = open("creargrupo.txt","r")
            grupo.telegram_id = archivo.read()
            archivo.close()
            grupo.save()
            return redirect('/grupos')
        else:
            print("Form no válido")
            print(form.errors.as_data())
            # form = AltaGrupoForm()

        return render(request, 'create-group.html', { 'form' : form})
    elif request.method == "GET":
        form = AltaGrupoForm()
        return render(request, "create-group.html", { 'form' : form})

@login_required(login_url="/login/")
def get_groups(request):
    groups = Group.objects.all()
    for group in groups:
        subject = Subject.objects.filter(id=group.subject.id).first()
        group.subject_name = subject.name

    paginator = Paginator(groups, 5)
    page = request.GET.get('page')
 
    try:
        group_paginator = paginator.page(page)
    except PageNotAnInteger:
        group_paginator = paginator.page(1)
 
    except EmptyPage:
        group_paginator = paginator.page(paginator.num_pages)

    return render(request, "get-groups.html", {'page': page, 'groups' : group_paginator})

@login_required(login_url="/login/")
def edit_group(request, id):
    group = Group.objects.get(id=id)    
    if request.method == "POST":
        form = EditGroupForm(request.POST, instance=group)
        
        if form.is_valid():
            print("OK\n")
            group = form.save()
            group.save()
            return redirect('/grupos')
        else:
            print(form.errors.as_data())
    elif request.method == "GET":
        form = EditGroupForm(instance=group)

        return render(request, "edit-group.html", {'form': form, 'group':group})

@login_required(login_url="/login/")
def delete_group(request, id):
    try:
        group = Group.objects.get(id=id)
        group.delete()
        messages.add_message(request, messages.WARNING, "Grupo eliminado exitosamente.")
    
    except ObjectDoesNotExist:
        messages.add_message(request, messages.ERROR, 'No encontramos el grupo {id}.'.format(id=id))

    return redirect('/grupos')

@login_required(login_url="/login/")
def create_contact(request):
    if request.method == "POST":
        form = CreateContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            messages.add_message(request, messages.SUCCESS, "Contacto creado exitosamente.")
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

    paginator = Paginator(contactos, 5)
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
    try:
        contact = Contact.objects.get(name=name)

        if request.method == "POST":
            form = EditContactForm(request.POST, instance=contact)
            if form.is_valid():
                contact = form.save()
                contact.save()
                messages.add_message(request, messages.SUCCESS, "Contacto modificado exitosamente.")
                return redirect('/contactos')
        else:
            form = EditContactForm(instance=contact)
            return render(request, 'edit-contact.html', { 'form': form, 'contact': contact })
    
    except ObjectDoesNotExist:
        messages.add_message(request, messages.ERROR, 'No encontramos el contacto @{name}.'.format(name=name))
        return redirect('/contactos')

@login_required(login_url="/login/")
def delete_contact(request, name):
    try:
        contact = Contact.objects.get(name=name)
        contact.delete()
        messages.add_message(request, messages.WARNING, "Contacto eliminado exitosamente.")
    
    except ObjectDoesNotExist:
        messages.add_message(request, messages.ERROR, 'No encontramos el contacto @{name}.'.format(name=name))

    return redirect('/contactos')
 
@login_required(login_url="/login/")
def send_message(request):

    if request.method == "POST":
        form = SendMessageForm(request.POST)
        if form.is_valid():
            usuarios = Usuario.objects.filter(username=request.user.username)
            usuario = usuarios.first()
            texto = request.POST.get('text_message')
            grupo = Group.objects.filter(id=request.POST.get('group')).first()
            mensaje = texto.replace(" ", "_")
            comando = "python mensaje.py " + usuario.api_id + " " + usuario.api_hash + " " + str(grupo.telegram_id) + " " + mensaje
            print(comando)
            respuesta = os.system(comando)
            return redirect('/enviarmensaje')
        else:
            form = SendMessageForm()

        return render(request, "send-message.html", { 'form' : form })
    elif request.method == "GET":
        form = SendMessageForm(request.POST or None)
        groups = Group.objects.all()
        return render(request, "send-message.html", { 'form' : form, 'groups' : groups })


@login_required(login_url="/login/")
def profile(request):
    usuario = Usuario.objects.filter(username=request.user.username).first()
    if usuario==None:
        return redirect('/error-500.html')

    usuario.api_hash = "********************"+usuario.api_hash[20:]
    if request.method == "GET":
        return render(request, "profile.html", {'usuario': usuario})
    elif request.method == "POST":
        return render(request, "profile.html", {'usuario': usuario})

@login_required(login_url="/login/")
def faq(request):
    return render(request, "faq.html")