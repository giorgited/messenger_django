from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from channels import Group
from .settings import MSG_TYPE_MESSAGE
import json

class ChatRoom(models.Model):    
    description = models.CharField(max_length = 200, default = '')
    name        = models.CharField(max_length = 99, default = '')
    user        = models.ForeignKey( User)

    def __str__(self):
        return self.name

    @property
    def websocket_group(self):
        """
        Returns the Channels Group that sockets should subscribe to to get sent
        messages as they are generated.
        """
        return Group("room-%s" % self.id)

    def send_message(self, message, user, msg_type=MSG_TYPE_MESSAGE):
        """
        Called to send a message to the room on behalf of a user.
        """
        final_msg = {'room': str(self.id), 'message': message, 'username': user.username, 'msg_type': msg_type}

        # Send out the message to everyone in the room
        self.websocket_group.send(
            {"text": json.dumps(final_msg)}
        )
def create_chat(sender, **kwargs):
    if kwargs['created']: 
        user_profile = ChatRoom.objects.create(user=kwargs['instance'])

post_save.connect(create_chat, sender=User)
