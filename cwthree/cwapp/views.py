from django.http import HttpResponse
from django.shortcuts import render

def user_form(request):
    if 'username' in request.GET:
        username = request.GET.get('username')
        data = request.GET.dict()
        return render(request, 'result.html', {'username': username, 'data': data})
    return render(request, 'form.html')