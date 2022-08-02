from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import CreationUserForm
from django.contrib import messages


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def homePage(request):
    context = {}
    
    return render(request, 'accounts/main.html', context)


def registerUser(request):
    
    form = CreationUserForm()
    
    if request.method == 'POST':
        form = CreationUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def loginUser(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_authenticated:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
        
    context = {}
    return render(request, 'accounts/login.html', context)
    