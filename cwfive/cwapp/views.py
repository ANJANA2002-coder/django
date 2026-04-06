from django.shortcuts import render
from .forms import LoginForm

def login_view(request):
    message = None

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            message = f"Thank you! You logged in with {email}"
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form, 'message': message})