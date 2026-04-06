from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
from django.core.paginator import Paginator

# Show all books (with pagination)
def book_list(request):
    books = Book.objects.all().order_by('id')

    paginator = Paginator(books, 5)  # show 5 books per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'page_obj': page_obj})


# Add new book
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookForm()

    return render(request, 'form.html', {'form': form})


# Edit existing book
def edit_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookForm(instance=book)

    return render(request, 'form.html', {'form': form})


# Delete book
def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('/')