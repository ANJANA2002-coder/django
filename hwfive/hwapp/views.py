from django.shortcuts import render
from .forms import RegisterForm

def register_view(request):
    message = None

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['full_name']
            message = f"Thanks for registering, {name}"
    else:
        form = RegisterForm()

    return render(request, "register.html", {
        "form": form,
        "message": message
    })