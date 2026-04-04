from django.shortcuts import render
def form_view(request):
    if request.GET:
        username = request.GET.get('username')
        return render(request,'form-data.html',{
            'formData':request.GET,
            'username': username
        })
    return render(request,'index.html' )

# Create your views here.
