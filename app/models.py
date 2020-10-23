from django.db import models
import datetime

class Usuario(models.Model):
    username = models.CharField(max_length=32)
    api_id = models.CharField(max_length=32)
    api_hash = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)

class Rol(models.Model):
    # Fields
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    # Metadata
    class Meta:
        ordering = ['id', 'name'] 

    # Methods
    def __str__(self):
        return self.description

class Contact(models.Model):
    # Fields
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    name = models.CharField(max_length=100, primary_key=True)
    email = models.EmailField
    contact_rol = models.ForeignKey(Rol, on_delete=models.CASCADE, default=2)

    # Metadata
    class Meta:
        ordering = ['first_name', 'last_name'] 

    # Methods
    def __str__(self):
        return self.name

class Career(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Group(models.Model):
    # Fields
    name = models.CharField(max_length=32)
    contacts = models.ManyToManyField(Contact)
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    comision = models.CharField(max_length=32, default="")
    subject = models.CharField(max_length=50, default="")
    current_year = models.IntegerField(default=datetime.datetime.now().year)

class Message(models.Model):
    text_message = models.CharField(max_length=32)
    id_group = models.CharField(max_length=32)

