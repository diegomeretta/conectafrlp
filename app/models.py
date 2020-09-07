from django.db import models

class ChatGroup(models.Model):
    name = models.CharField(max_length=30)
    user_chat1 = models.CharField(max_length=30)
    user_chat2 = models.CharField(max_length=30)

