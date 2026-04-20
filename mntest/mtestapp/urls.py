from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),

    path('', bookmark_list, name='list'),
    path('add/', add_bookmark, name='add'),
    path('edit/<int:pk>/', edit_bookmark, name='edit'),
    path('delete/<int:pk>/', delete_bookmark, name='delete'),
]