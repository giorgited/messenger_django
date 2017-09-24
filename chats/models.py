from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class ChatRoom(models.Model):    
    description = models.CharField(max_length = 200, default = '')
    name        = models.CharField(max_length = 99, default = '')
    user        = models.ForeignKey( User)

def create_chat(sender, **kwargs):
    if kwargs['created']: 
        user_profile = ChatRoom.objects.create(user=kwargs['instance'])

post_save.connect(create_chat, sender=User)
