from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from .models import *
from .forms import CreateUserForm

def home(request):
    return render(request, 'mypage/home.html')

def project(request):
    return render(request, 'mypage/project.html')

def loginpage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Username or Password is incorrect.")
            return render(request, 'mypage/login.html')

    return render(request, 'mypage/login.html')

def logoutuser(request):
    logout(request)
    return redirect('login')

def registerpage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # user = form.cleaned_date.get('username')
            # messages.success(request, 'Account was created for '+ user)
            return redirect('login')
    context = {'form': form}
    return render(request, 'mypage/register.html', context)
