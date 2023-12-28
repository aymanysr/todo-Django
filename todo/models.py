from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TodoList(models.Model):
    title =models.CharField(max_length=100, null=False, blank=False)
    shared_link = models.CharField(max_length=255, unique=True)

class Todos(models.Model):
    TodoList = models.ForeignKey(TodoList, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200, null=False, blank=False)
    completed = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
