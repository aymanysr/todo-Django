from django.urls import path
from . import views

# Define URL patterns for the todo app
urlpatterns = [
        path('', views.homepage, name=''),  # Endpoint for the todo view
        path('register/', views.register, name='register'),
        path('my_login/', views.my_login, name='login'),
        path('dashboard/', views.dashboard, name='dashboard'),
        path('logout_user/', views.logout_user, name='logout'),
]

htmxpatterns = [
        path('create_todo/', views.create_todo, name='create_todo'),
        path('mark_todo/<int:pk>/', views.mark_todo, name='mark_todo'),
        path('delete_todo/<int:pk>/', views.delete_todo, name='delete_todo'),
]

urlpatterns += htmxpatterns
"""
This module defines the URL patterns for the todo app.

The urlpatterns list contains the following patterns:
- The empty path ('') maps to the TodoView class-based view, which is used to display the todo app.
    It is named 'todo' and can be accessed using the name 'todo' in the templates or views.

Note: This module is used by Django's URL routing system to match the requested URLs with the corresponding views.
"""
