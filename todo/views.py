from .models import Todos
from . forms import CreateUserForm
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required

#- authentification models and functions
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def homepage(request):
    return render(request, 'todo/index.html')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    context = {'registerform': form}
    return render(request, 'todo/register.html', context=context)

def my_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, 'todo/my_login.html', {'error': 'Invalid username or password'})

    return render(request, 'todo/my_login.html')

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'todo/dashboard.html')

def logout_user(request):
    logout(request)
    return redirect("")

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
    return render(request, 'todo/todo-list.html', {'todos': todos})


# Marking completed True
def mark_todo(request, pk):
    todo = Todos.objects.get(pk=pk)
    todo.completed = not todo.completed
    todo.save()
    todos = Todos.objects.all().order_by('-id')
    return render(request, 'todo/todo-list.html', {'todos': todos})

# Deleting a Todo
def delete_todo(request, pk):
    todo = Todos.objects.get(pk=pk)
    todo.delete()
    todos = Todos.objects.all().order_by('-id')
    return render(request, 'todo/todo-list.html', {'todos': todos})
