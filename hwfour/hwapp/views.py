from django.shortcuts import render
def form_view(request):
    if request.method == 'POST':
     name = request.POST.get('name')
     color = request.POST.get('color')
     return render(request,'form-data.html',{
         'formData':request.POST,
         'name': name,
         'color': color
     })
    return render(request,'index.html')
# Create your views here.
