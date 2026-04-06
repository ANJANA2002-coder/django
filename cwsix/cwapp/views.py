from django.shortcuts import render
from .models import Movie

def movie_form(request):
    message = ""

    if request.method == "POST":
        name = request.POST.get("name")
        year = request.POST.get("year")

        movie = Movie.objects.create(name=name, year=year)

        message = f"Movie saved: {movie.name} ({movie.year})"

    return render(request, "movie_form.html", {"message": message})