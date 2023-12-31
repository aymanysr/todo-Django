from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TodoList(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist_owner", default=1)
    user = models.ManyToManyField(User, through="SharedTodoList", related_name="todolist_user")

class Todos(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name="todos")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class SharedTodoList(models.Model):
    title = models.CharField(max_length=100, default="Default title")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
