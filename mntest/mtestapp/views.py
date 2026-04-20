from django.shortcuts import render, redirect, get_object_or_404
from .models import Bookmark
from .forms import BookmarkForm, SignupForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib.auth.views import LoginView

def signup_view(request):
    form = SignupForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('list')
    return render(request, 'mtestapp/signup.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'mtestapp/login.html'


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/login/')

def add_bookmark(request):
    if Bookmark.objects.filter(user=request.user).count() >= 5:
        return render(request, 'mtestapp/error.html', {'msg': 'Limit reached (5 bookmarks only)'})

    form = BookmarkForm(request.POST or None)
    if form.is_valid():
        bookmark = form.save(commit=False)
        bookmark.user = request.user

        if Bookmark.objects.filter(user=request.user, url=bookmark.url).exists():
            return render(request, 'mtestapp/error.html', {'msg': 'Already exists'})

        bookmark.save()
        return redirect('list')

    return render(request, 'mtestapp/add.html', {'form': form})


@login_required(login_url='/login/')

def bookmark_list(request):
    query = request.GET.get('q')
    bookmarks = Bookmark.objects.filter(user=request.user)

    if query:
        bookmarks = bookmarks.filter(title__icontains=query) | bookmarks.filter(url__icontains=query)

    paginator = Paginator(bookmarks.order_by('-created_at'), 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'mtestapp/list.html', {'page_obj': page_obj})


@login_required(login_url='/login/')

def edit_bookmark(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk, user=request.user)
    form = BookmarkForm(request.POST or None, instance=bookmark)

    if form.is_valid():
        form.save()
        return redirect('list')

    return render(request, 'mtestapp/edit.html', {'form': form})


@login_required(login_url='/login/')

def delete_bookmark(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk, user=request.user)
    bookmark.delete()
    return redirect('list')