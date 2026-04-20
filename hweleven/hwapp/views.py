from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required


# Signup
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('welcome')
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
            return redirect('welcome')
    else:
        form = AuthenticationForm()
    return render(request, 'myapp/login.html', {'form': form})


# Welcome Page (Session Counter)
@login_required (LOGIN_URL = '/login/')
def welcome_view(request):
    count = request.session.get('visit_count', 0)
    count += 1
    request.session['visit_count'] = count

    return render(request, 'myapp/welcome.html', {'count': count})


# Logout
def logout_view(request):
    logout(request)
    return redirect('login')