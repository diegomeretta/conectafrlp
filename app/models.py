from django.db import models

class Usuario(models.Model):
    username = models.CharField(max_length=32)
    api_id = models.CharField(max_length=32)
    api_hash = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)

class Group(models.Model):
    name = models.CharField(max_length=32)
