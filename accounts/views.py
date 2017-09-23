from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'accounts/home.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/')
        else:
            return render(request, 'accounts/register.html', {'form': UserCreationForm()})
    else:
        form = UserCreationForm()
        args = {
            'form': form
        }
        return render(request, 'accounts/register.html', args)