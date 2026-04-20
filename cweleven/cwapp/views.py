# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Visit

# Signup
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Visit.objects.create(user=user)  # initialize counter
            login(request, user)
            return redirect('counter')
    else:
        form = UserCreationForm()
    return render(request, 'myapp/signup.html', {'form': form})


# Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('counter')
    else:
        form = AuthenticationForm()
    return render(request, 'myapp/login.html', {'form': form})


# Visit Counter (only for logged-in users)
@login_required(login_url='/login/')
def counter_view(request):
    visit, created = Visit.objects.get_or_create(user=request.user)
    visit.count += 1
    visit.save()
    return render(request, 'myapp/counter.html', {'count': visit.count})


# Logout
def logout_view(request):
    logout(request)
    return redirect('login')