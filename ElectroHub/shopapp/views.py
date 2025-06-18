from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import ShopUserCreationForm, ShopUserLoginForm
from django.contrib.auth.decorators import user_passes_test

def index(request):
    return render(request, 'index.html')

def register_view(request):
    if request.method == 'POST':
        form = ShopUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('shop:home')
    else:
        form = ShopUserCreationForm()
    return render(request, 'shopapp/auth/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = ShopUserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('shop:home')
    else:
        form = ShopUserLoginForm()
    return render(request, 'shopapp/auth/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('shop:home')