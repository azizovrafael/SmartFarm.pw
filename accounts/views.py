from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import login, authenticate, logout


def Login_View(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('dash')
    return render(request, 'login.html', {'form': form})


def Logout_View(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        logout(request)
        return redirect('home')
