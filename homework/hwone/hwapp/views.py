from django.shortcuts import render
def gallery(request):
    return render(request,'gallery.html')
def contact(request):
    return render(request,'contact.html')
# Create your views here.
