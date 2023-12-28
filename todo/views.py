from django.shortcuts import render
from django.http import HttpResponse
from .models import Todos

# Create your views here.
def homepage(request):
    return render(request, 'todo/index.html')

def register(request):
    return render(request, 'todo/register.html')

def my_login(request):
    return render(request, 'todo/my_login.html')

def dashboard(request):
    return render(request, 'todo/dashboard.html')

def index(request):
    # todos = Todos.objects.all().order_by('-id')
    # return render(request, 'index.html', {'todos': todos})
    pass

# Creating a new Todo
def create_todo(request):
    title = request.POST.get('title')
    todo = Todos.objects.create(title=title)
    todo.save()
    todos = Todos.objects.all().order_by('-id')
    return render(request, 'todo-list.html', {'todos': todos})


# Marking completed True
def mark_todo(request, pk):
    todo = Todos.objects.get(pk=pk)
    todo.completed = not todo.completed
    todo.save()
    todos = Todos.objects.all().order_by('-id')
    return render(request, 'todo-list.html', {'todos': todos})

# Deleting a Todo
def delete_todo(request, pk):
    todo = Todos.objects.get(pk=pk)
    todo.delete()
    todos = Todos.objects.all().order_by('-id')
    return render(request, 'todo-list.html', {'todos': todos})
