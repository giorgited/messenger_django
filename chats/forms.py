from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from chats.models import ChatRoom
# class CreateChatForm(forms.Form):
#     name = forms.CharField(max_length=50, required=True)    
#     description = forms.CharField(max_length=200, required=True)    

class CreateChatForm(forms.ModelForm):
    class Meta:
        model = ChatRoom
        fields = ('description', 'name')