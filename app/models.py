from django.db import models
import datetime

class Usuario(models.Model):
    username = models.CharField(max_length=32)
    api_id = models.CharField(max_length=32)
    api_hash = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    telegram_id = models.CharField(max_length=32, default="")

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

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    level = models.IntegerField(default=0)
    career = models.ForeignKey(Career, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Commission(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=5)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Group(models.Model):
    # Fields
    name = models.CharField(max_length=32)
    contacts = models.ManyToManyField(Contact, related_name='groups')
    career = models.ForeignKey(Career, default=0, on_delete=models.CASCADE)
    commission = models.ForeignKey(Commission, default=0, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    current_year = models.IntegerField(default=datetime.datetime.now().year)
    telegram_id = models.CharField(max_length=32, default="")

class Message(models.Model):
    text_message = models.CharField(max_length=32)
    id_group = models.CharField(max_length=32)

