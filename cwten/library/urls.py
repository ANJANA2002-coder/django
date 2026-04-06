from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list),
    path('add/', views.add_book),
    path('edit/<int:id>/', views.edit_book),
    path('delete/<int:id>/', views.delete_book),
]