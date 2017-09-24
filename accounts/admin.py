from django.contrib import admin
from accounts.models import UserProfile
from chats.models import ChatRoom

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(ChatRoom)