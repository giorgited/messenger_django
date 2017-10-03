from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from chats.forms import CreateChatForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from chats.models import ChatRoom
from accounts.models import User

@login_required
def create_chat(request):
    chatRoom = ChatRoom()
    chatRoom.name = 'test'
    chatRoom.description = 'desc'
    #chatRoom.save()

    if request.method == 'POST':
        form = CreateChatForm(request.POST)   
        form.user = request.user     
        if form.is_valid():
            chat = form.save(commit=False)
            chat.user = request.user
            chat.save()
            return redirect('/chats/chat?chatID=' + str(chat.pk), {'chat':chat})
        else:
            return render(request, 'accounts/home.html', {'form':form})
    else:
        form = CreateChatForm()
        args = {
            'form': form
        }
        return render(request, 'chats/create_chat.html', args)

@login_required
def join_chat(request):
    rooms = ChatRoom.objects.all()
    for room in rooms:
        print (room.name)

    return render(request, 'chats/join_chat.html', {'rooms': rooms, 'user': request.user})

@login_required
def entered_chat(request):
    room = ChatRoom.objects.get(pk = request.GET.get('chatID'))
    return render(request, 'chats/chat.html', {'room' : room})

@login_required
def get_my_user_info(request):
    user = request.user
    request_data = user
    return HttpResponse(user.username)
