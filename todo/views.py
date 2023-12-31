from .models import Todos
from .models import TodoList
from . forms import CreateUserForm
from django.shortcuts import get_object_or_404, render, redirect

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
    todos = Todos.objects.filter(user=request.user).order_by('-id')
    todolist = TodoList.objects.filter(owner=request.user).order_by('-id')
    return render(request, 'todo/dashboard.html', {'todos': todos, 'todolist': todolist})

def logout_user(request):
    logout(request)
    return redirect("")

@login_required(login_url='login')
def create_todolist(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        user = request.user
        todolist = TodoList.objects.create(title=title, owner=user)
        todolist.save()
        todolist = TodoList.objects.filter(owner=request.user).order_by('-id')
        todos = Todos.objects.filter(user=request.user, todolist__in=todolist).order_by('-id')
        return render(request, 'todo/todo-list.html', {'todolist': todolist, 'todos': todos})
    else:
        return render(request, 'todo/create_todolist.html')

def delete_todolist(request, pk):
    todolist = TodoList.objects.get(pk=pk)
    if todolist.owner != request.user:
        return redirect('todo/todo-list.html')
    todolist.delete()
    todolist = TodoList.objects.filter(owner=request.user).order_by('-id')
    todos = Todos.objects.filter(user=request.user).order_by('-id')
    return render(request, 'todo/todo-list.html', {'todolist': todolist, 'todos': todos})


# Creating a new Todo
@login_required(login_url='login')
def create_todo(request, pk):
    todolist = get_object_or_404(TodoList, pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        user = request.user
        todo = Todos.objects.create(title=title, user=user, todolist=todolist)
        todo.save()
        todos = Todos.objects.filter(user=user, todolist=todolist).order_by('-id')
        todolist = TodoList.objects.filter(owner=request.user).order_by('-id')
        return render(request, 'todo/todo-list.html', {'todolist':todolist, 'todos': todos})
    else:
        return render(request, 'todo/create_todo.html', {'pk': pk})


# Marking completed True
def mark_todo(request, pk):
    todo = Todos.objects.get(pk=pk)
    todo.completed = not todo.completed
    todo.save()
    todos = Todos.objects.filter(user=request.user, todolist=todo.todolist).order_by('-id')
    todolist = TodoList.objects.filter(owner=request.user).order_by('-id')
    return render(request, 'todo/todo-list.html', {'todolist': todolist,'todos': todos})

# Deleting a Todo
def delete_todo(request, pk):
    todo = Todos.objects.get(pk=pk)
    if todo.user != request.user:
        return redirect('dashboard')
    todo.delete()
    todos = Todos.objects.filter(user=request.user, todolist=todo.todolist).order_by('-id')
    todolist = TodoList.objects.filter(owner=request.user).order_by('-id')
    return render(request, 'todo/todo-list.html', {'todolist':todolist, 'todos': todos})
