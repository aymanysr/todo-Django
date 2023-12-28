from django.contrib import admin
from .models import Todos
# Register your models here.
@admin.register(Todos)
class todoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'updated_at', 'created_at')
    verbose_name = ('Todo')
