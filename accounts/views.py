from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import (
                    RegistrationForm,
                    EditUserForm,
                    PasswordChangeForm
)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
# Create your views here.
def home(request):
    return render(request, 'accounts/home.html', {'user': request.user})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/')
        else:
            return render(request, 'accounts/register.html', {'form': RegistrationForm()})
    else:
        form = RegistrationForm()
        args = {
            'form': form
        }
        return render(request, 'accounts/register.html', args)


@login_required
def user_info(request):
    if request.method == "POST":
        form = EditUserForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()

        form = EditUserForm(instance = request.user)
        return render(request, 'accounts/userInfo.html', {'user': request.user, 'form': form})
    else:
        form = EditUserForm(instance = request.user)
        return render(request, 'accounts/userInfo.html', {'user': request.user, 'form': form})

def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()

            form = EditUserForm(instance = request.user)
            return render(request, 'accounts/userInfo.html', {'user': request.user, 'form': form})
    else:
        form = PasswordChangeForm(instance=request.user)
        
        return render(request, 'accounts/change_password.html', {'user': request.user, 'form': form})