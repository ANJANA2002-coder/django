from django.shortcuts import render
from .models import Contact

def contact_form(request):
    message = ""

    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")

        Contact.objects.create(
            full_name=full_name,
            email=email,
            phone=phone
        )

        message = f"Thank you, {full_name}"

    return render(request, "contact_form.html", {"message": message})